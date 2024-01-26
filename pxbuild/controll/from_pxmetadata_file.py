from datetime import datetime
from typing import List, Dict

from pxbuild.models.input.pydantic_pxmetadata import PxMetadata
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.input.helper_pxcodes import HelperPxCodes
from pxbuild.models.input.pydantic_pxstatistics import PxStatistics

from pxbuild.models.output.pxfile.px_file_model import PXFileModel

from .helpers.small_static_functions import Commons

from .helpers.datadata_helpers.datadatasource import Datadatasource
from .helpers.datadata_helpers.for_get_data import ForGetData
from .helpers.datadata_helpers.main_data import MapData
from .helpers.loaded_jsons import LoadedJsons
from .helpers.support_files import SupportFiles 


class LoadFromPxmetadata:
    LabelConstructionOptionDict = {
        "LabelConstructionOption.code": 0,
        "LabelConstructionOption.text": 1,
        "LabelConstructionOption.code_text": 2,
        "LabelConstructionOption.text_code": 3,
    }

    def __init__(self, pxmetadata_id: str, config_file: str) -> None:
        self._pxmetadata_id = pxmetadata_id
       
        self._loaded_jsons:LoadedJsons =  LoadedJsons (pxmetadata_id, config_file) 
       
        self._config = self._loaded_jsons.get_config()
        self._pxmetadata_model = self._loaded_jsons.get_pxmetadata()
        self._pxstatistics = self._loaded_jsons.get_pxstatistics()

        if self._pxmetadata_model.dataset.coded_dimensions:
            self._pxcodes_helper:Dict[str, HelperPxCodes] = self.get_pxcodes_helpers()

        self._datadata = Datadatasource(self._pxmetadata_model.dataset.data_file, self._config)

        self._for_get_data_by_varid: Dict[str, ForGetData] = dict()

        ##################

        self.models_for_pytest: dict = {}   #Todo make perfect reader, and let the pytest read the files

        self._last_updated = self.get_last_updated(self._pxstatistics)
        out_model = PXFileModel()
        # loop in languages
        self._add_language_independent = True  # like AXIS_VERSION
        for language in self._config.admin.valid_languages:
           
            self._current_lang = language
            self._contact_string = self.get_contact_string(self._pxstatistics, language)
            
            self._stub = []
            self._heading = [self._config.contvariable[language]]

            self._metaid_table: List[str] = []
            self._metaid_valiable: dict = {}

            self.map_pxbuildconfig_to_pxfile(self._config, language , out_model)
            self.map_pxmetadata_to_pxfile(self._pxmetadata_model, out_model)
            self.add_pxstatistics_to_pxfile(self._pxstatistics, out_model)

            self.add_coded_dimensions_to_pxfile(out_model)
            self.add_measurements_to_pxfile(out_model)
            self.map_decimals_to_pxfile(out_model)
            self.add_time_dimension_to_pxfile(out_model)
            self.map_stub_heading_to_pxfile(out_model)
            self.map_title_to_pxfile(out_model)
            self.map_aggregallowed_to_pxfile(out_model)

            self.map_metaid_to_pxfile(out_model)


            fixdata = MapData(self._datadata, self._pxmetadata_model, self._config, self._for_get_data_by_varid, self._stub , self._heading)
            fixdata.map_data(out_model)



            if not self._config.admin.build_multilingual_files: 
                write_output(self._pxmetadata_id, self._config.admin.output_destination.px_folder_format, out_model, language)
                
                self.models_for_pytest[language] = out_model 
                out_model = PXFileModel()
            else:
                self._add_language_independent = False     

        if self._config.admin.build_multilingual_files: 
            write_output(self._pxmetadata_id, self._config.admin.output_destination.px_folder_format, out_model)
            self.models_for_pytest["multi"] = out_model 

        support = SupportFiles(self._pxmetadata_model,self._config, self._pxcodes_helper,self._pxmetadata_id)
        support.make_vs_file()


    # naming convention:get_  gets a value, map_  sets on outModel, add_  changes self and sets on outModel 

    def get_pxcodes_helpers(self) -> Dict[str, HelperPxCodes]:
        my_out:Dict[str, HelperPxCodes] =  {}
        resolved_pxcodes_ids = self._loaded_jsons.get_resolved_pxcodes_ids()
        for codelist_id in resolved_pxcodes_ids:
            my_out[codelist_id] = HelperPxCodes(resolved_pxcodes_ids[codelist_id], self._config.admin.valid_languages)

        return my_out

    def map_metaid_to_pxfile(self, out_model: PXFileModel) -> None:
        if self._add_language_independent:
            if self._metaid_table:
                out_model.meta_id.set(" ".join(self._metaid_table))

        for vari in self._metaid_valiable:
            out_model.meta_id.set(" ".join(self._metaid_valiable[vari]), vari, None, self._current_lang)

   

    def map_aggregallowed_to_pxfile(self, out_model: PXFileModel):
        # Check if all values in the array are True
        if self._add_language_independent:
            all_true = all(instance.aggregation_allowed for instance in self._pxmetadata_model.dataset.measurements)
            out_model.aggregallowed.set(all_true)

    def map_title_to_pxfile(self, out_model: PXFileModel):
        lang = self._current_lang
        model = self._pxmetadata_model.dataset

        vari_list =  Commons.get_variable_list(self._stub, self._heading ) 
        tmp_string = ", ".join(vari_list[:-1])

        title = (
            model.table_id
            + ": "
            + model.base_title[lang]
            + ", "
            + self._config.admin.the_word_by[lang]
            + " "
            + tmp_string
            + " "
            + self._config.admin.the_word_and[lang]
            + " "
            + vari_list[-1]
        )

        out_model.title.set(title, self._current_lang)

    def map_stub_heading_to_pxfile(self, out_model: PXFileModel):
        if self._heading:
            out_model.heading.set(self._heading, self._current_lang)

        if self._stub:
            out_model.stub.set(self._stub, self._current_lang)

        if not self._stub and not self._heading:
            raise Exception("Sorry, both stub and heading are empty.")

    def add_time_dimension_to_pxfile(self, out_model: PXFileModel):
        my_periods = self._datadata.GetTimePeriodes(self._pxmetadata_model.dataset.time_dimension.column_name)

        my_funny_var_id = self._pxmetadata_model.dataset.time_dimension.label[self._current_lang]

        self._heading.append(my_funny_var_id)
        out_model.values.set(my_periods, my_funny_var_id, self._current_lang)
        out_model.codes.set(my_periods, my_funny_var_id, self._current_lang)
        out_model.variablecode.set(self._config.timevariable_code, my_funny_var_id, self._current_lang)
        out_model.variable_type.set("T", my_funny_var_id, self._current_lang)

        for_get_data = ForGetData(self._pxmetadata_model.dataset.time_dimension.column_name, my_periods)
        self._for_get_data_by_varid[my_funny_var_id] = for_get_data

    def add_coded_dimensions_to_pxfile(self, out_model: PXFileModel):
        if self._pxmetadata_model.dataset.coded_dimensions:
            lang = self._current_lang
            for my_var in self._pxmetadata_model.dataset.coded_dimensions:
                my_funny_var_id = my_var.label[lang]
                self._stub.append(my_funny_var_id)
                my_var_code = my_var.code if my_var.code is not None else my_var.column_name
                out_model.variablecode.set(my_var_code, my_funny_var_id, lang)

                my_pxcodes_helper = self._pxcodes_helper[my_var.codelist_id]

                temp_codes = my_pxcodes_helper.getCodes(lang)
                out_model.codes.set(temp_codes, my_funny_var_id, lang)

                temp_values = my_pxcodes_helper.getLabels(lang)
                out_model.values.set(temp_values, my_funny_var_id, lang)
                if my_pxcodes_helper.groupings():
                    my_domain_id = Commons.make_domain_id(my_var.codelist_id, self._current_lang)
                    out_model.domain.set(my_domain_id, my_funny_var_id, self._current_lang)

                if my_var.is_geo_variable_type:
                    out_model.variable_type.set("G", my_funny_var_id, lang)
                else:
                    out_model.variable_type.set("N", my_funny_var_id, lang)

                out_model.prestext.set(
                    self.LabelConstructionOptionDict[str(my_var.label_construction_option)], my_funny_var_id, lang
                )

                if not my_pxcodes_helper.elimination_possible:
                    out_model.elimination.set("NO", my_funny_var_id, lang)
                else:
                    label = my_pxcodes_helper.getEliminationLabel(lang)
                    if label:
                        out_model.elimination.set(label, my_funny_var_id, lang)
                    else:
                        out_model.elimination.set("YES", my_funny_var_id, lang)

                if my_var.meta_id:
                    if my_funny_var_id not in self._metaid_valiable:
                        self._metaid_valiable[my_funny_var_id] = []

                    self._metaid_valiable[my_funny_var_id] += my_var.meta_id

                # Note on variable
                if my_var.notes:
                    for note in my_var.notes:
                        if note.is_mandatory:
                            out_model.notex.set(note.text[lang], my_funny_var_id, lang)
                        else:
                            out_model.note.set(note.text[lang], my_funny_var_id, lang)
                # Note on a value in variale
                my_value_notes = my_pxcodes_helper.getNotes(lang)
                if my_value_notes:
                    for code in my_value_notes:
                        for note in my_value_notes[code]:
                            if note.is_mandatory:
                                out_model.valuenotex.set(note.text[lang], my_funny_var_id, code, lang)
                            else:
                                out_model.valuenote.set(note.text[lang], my_funny_var_id, code, lang)

                for_get_data = ForGetData(my_var.column_name, my_pxcodes_helper.getCodes(lang))
                self._for_get_data_by_varid[my_funny_var_id] = for_get_data

    def add_measurements_to_pxfile(self, out_model: PXFileModel):
        if not self._pxmetadata_model.dataset.measurements:
            raise Exception("Sorry, dataset is missing measurment.")

        my_funny_var_id = self._config.contvariable[self._current_lang]

        out_codes = []
        out_values = []
        for my_cont in self._pxmetadata_model.dataset.measurements:
            my_funny_cont_id = my_cont.label[self._current_lang]
            my_cont_code = my_cont.code if my_cont.code is not None else my_cont.column_name
            out_codes.append(my_cont_code)
            out_values.append(my_cont.label[self._current_lang])
            out_model.seasadj.set(my_cont.is_seasonally_adjusted or False, my_funny_cont_id, self._current_lang)
            out_model.dayadj.set(my_cont.is_workingdays_adjusted or False, my_funny_cont_id, self._current_lang)
            out_model.units.set(my_cont.unit_of_measure[self._current_lang], my_funny_cont_id, self._current_lang)
            out_model.contact.set(self._contact_string, my_funny_cont_id, self._current_lang)
            out_model.last_updated.set(self._last_updated, my_funny_cont_id, self._current_lang)

            if my_cont.reference_period[self._current_lang]:
                out_model.refperiod.set(
                    my_cont.reference_period[self._current_lang], my_funny_cont_id, self._current_lang
                )

            if my_cont.show_decimals > 0:
                out_model.precision.set(my_cont.show_decimals, my_funny_var_id, my_funny_cont_id, self._current_lang)

            # optional with no default
            if my_cont.price_type:
                # todo str(my_cont.price_type) should yield C or F
                out_model.cfprices.set(str(my_cont.price_type), my_funny_cont_id, self._current_lang)

        out_model.values.set(out_values, my_funny_var_id, self._current_lang)
        out_model.codes.set(out_codes, my_funny_var_id, self._current_lang)
        out_model.variablecode.set(self._config.contvariable_code, my_funny_var_id, self._current_lang)
        out_model.variable_type.set("C", my_funny_var_id, self._current_lang)

        for_get_data = ForGetData(self._config.contvariable_code, out_codes)
        self._for_get_data_by_varid[my_funny_var_id] = for_get_data

    def map_decimals_to_pxfile(self, out_model: PXFileModel):
        if self._add_language_independent:
            show_decimals_values = [instance.show_decimals for instance in self._pxmetadata_model.dataset.measurements]

            if self._pxmetadata_model.dataset.stored_decimals:
                out_model.decimals.set(max(self._pxmetadata_model.dataset.stored_decimals, max(show_decimals_values)))
            else:
                out_model.decimals.set(max(show_decimals_values))

            out_model.showdecimals.set(min(show_decimals_values))

    def get_contact_string(self, in_data: PxStatistics, language:str) -> str:
        contact_string = ""

        if in_data.contacts is None:
            return contact_string

        for contact in in_data.contacts:
            if contact.name is None:
                return contact_string
            contact_string += f"{contact.name[language]}#{contact.phone}#{contact.email}##"

        return contact_string[:-2]

    def get_last_updated(self, in_model: PxStatistics) -> str:
        last_updated_date = ""
        if in_model.upcoming_releases is None:
            return last_updated_date

        if len(in_model.upcoming_releases) < 1:
            return last_updated_date

        last_updated_date = in_model.upcoming_releases[0]

        formatted_string = convert_to_pxdate_string(last_updated_date, f"%Y-%m-%d %H:%M:%S.%f")

        return formatted_string

    def add_pxstatistics_to_pxfile(self, in_model: PxStatistics, out_model: PXFileModel):
        lang = self._current_lang

        out_model.subject_area.set(in_model.subject_text[lang], lang)
        if self._add_language_independent:
            out_model.subject_code.set(in_model.subject_code)

            self._metaid_table += in_model.meta_id

        # out_model.update_frequency.set() Hmm is not listed as language dependent in pdf

    def map_pxmetadata_to_pxfile(self, in_model: PxMetadata, out_model: PXFileModel):
        lang = self._current_lang
        if self._add_language_independent:
            out_model.tableid.set(in_model.dataset.table_id)
            out_model.matrix.set("tab_" + in_model.dataset.table_id)
        out_model.contents.set(in_model.dataset.table_id + ": " + in_model.dataset.base_title[lang] + ",", lang)

    def map_pxbuildconfig_to_pxfile(self, in_config: PxbuildConfig, current_lang:str , out_model: PXFileModel):
        if self._add_language_independent:
            out_model.language.set(current_lang)
            if in_config.admin.build_multilingual_files:
                out_model.languages.set(in_config.admin.valid_languages)
            out_model.axis_version.set(str(in_config.axis_version))
            out_model.charset.set(str(in_config.charset))
            out_model.codepage.set(str(in_config.code_page))
            out_model.descriptiondefault.set((in_config.description_default or False))

        out_model.contvariable.set(str(in_config.contvariable[current_lang]), current_lang)

        if in_config.datasymbol1 and in_config.datasymbol1[self._current_lang]:
            out_model.datasymbol1.set(str(in_config.datasymbol1[self._current_lang]), self._current_lang)
        if in_config.datasymbol2 and in_config.datasymbol2[self._current_lang]:
            out_model.datasymbol2.set(str(in_config.datasymbol2[self._current_lang]), self._current_lang)
        if in_config.datasymbol3 and in_config.datasymbol3[self._current_lang]:
            out_model.datasymbol3.set(str(in_config.datasymbol3[self._current_lang]), self._current_lang)
        if in_config.datasymbol4 and in_config.datasymbol4[self._current_lang]:
            out_model.datasymbol4.set(str(in_config.datasymbol4[self._current_lang]), self._current_lang)
        if in_config.datasymbol5 and in_config.datasymbol5[self._current_lang]:
            out_model.datasymbol5.set(str(in_config.datasymbol5[self._current_lang]), self._current_lang)
        if in_config.datasymbol6 and in_config.datasymbol6[self._current_lang]:
            out_model.datasymbol6.set(str(in_config.datasymbol6[self._current_lang]), self._current_lang)
        if in_config.datasymbol_nil and in_config.datasymbol_nil[self._current_lang]:
            out_model.datasymbolnil.set(str(in_config.datasymbol_nil[self._current_lang]), self._current_lang)
        if in_config.datasymbol_sum and in_config.datasymbol_sum[self._current_lang]:
            out_model.datasymbolsum.set(str(in_config.datasymbol_sum[self._current_lang]), self._current_lang)

        out_model.source.set(in_config.source[self._current_lang], self._current_lang)




def convert_to_pxdate_string(date_string: str, date_format: str) -> str:
    dtm_date = datetime.strptime(date_string, date_format)
    px_date_string = dtm_date.strftime(f"%Y%m%d %H:%M")

    return px_date_string

def write_output(pxmetadata_id:str, px_folder_format:str, out_model:PXFileModel, language:str | None = None) -> None:
    temp_tabid = pxmetadata_id
    out_folder = px_folder_format.format(id=temp_tabid)
    language_part=""
    if language:
        language_part="_"+language

    out_file = f"{out_folder}/tab_{temp_tabid}{language_part}.px"

    with open(out_file, "w") as f:
        print(out_model, file=f)

    print("File written to:", out_file)

