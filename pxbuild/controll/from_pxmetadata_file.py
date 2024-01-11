import json
from datetime import datetime
import time
import pandas as pd
import numpy as np
from typing import List, Dict

from pxbuild.models.input.pydantic_pxmetadata import PxMetadata
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.input.pydantic_pxcodes import PxCodes
from pxbuild.models.input.pydantic_pxcodes import Grouping
from pxbuild.models.input.helper_pxcodes import HelperPxCodes
from pxbuild.models.input.pydantic_pxstatistics import PxStatistics

from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.models.output.agg_vs.vs_file_model import _VSFileModel
from pxbuild.models.output.agg.agg_file_model import AggFileModel

from .helpers.datadatasource import Datadatasource
from .helpers.for_get_data import ForGetData
from .helpers.data_formatter import DataFormatter
from .helpers.loaded_jsons import LoadedJsons 


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
            self._resolved_pxcodes_ids = self._loaded_jsons.get_resolved_pxcodes_ids()
            self._pxcodes_helper:Dict[str, HelperPxCodes] =  {}

            for codelist_id in self._resolved_pxcodes_ids:
                self._pxcodes_helper[codelist_id] = HelperPxCodes(
                        self._resolved_pxcodes_ids[codelist_id], self._config.admin.valid_languages
                )

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

            self.map_coded_dimensions_to_pxfile(out_model)
            self.map_measurements_to_pxfile(out_model)
            self.map_decimals_to_pxfile(out_model)
            self.map_time_dimension_to_pxfile(out_model)
            self.map_stub_heading_to_pxfile(out_model)
            self.map_title_to_pxfile(out_model)
            self.map_aggregallowed_to_pxfile(out_model)

            self.add_metaid_to_pxfile(out_model)


            #fixdata = FixData()
            #fixdata.get_data(out_model)
            self.get_data(out_model)




            if not self._config.admin.build_multilingual_files: 
                write_output(self._pxmetadata_id, self._config.admin.output_destination.px_folder_format, out_model, language)
                
                self.models_for_pytest[language] = out_model 
                out_model = PXFileModel()
            else:
                self._add_language_independent = False     

        if self._config.admin.build_multilingual_files: 
            write_output(self._pxmetadata_id, self._config.admin.output_destination.px_folder_format, out_model)
            self.models_for_pytest["multi"] = out_model 

        self.make_vs_file()

    def calculate_factor(self) -> int:
        variables_in_output_order = self.get_variable_list()
        curr_factor = 1
        for vari in reversed(variables_in_output_order):
            temp_for_get_data: ForGetData = self._for_get_data_by_varid[vari]
            temp_for_get_data.factor = curr_factor
            prev_number = temp_for_get_data._length_of_codelist
            curr_factor = curr_factor * prev_number

        array_size = curr_factor

        return array_size

    def get_data(self, out_model: PXFileModel) -> None:
        # /// MINDEX:
        # /// We need to convert a point(one value for each variable) in
        # /// the cube to a number(the index of the array).
        # ///
        # /// k,j, i... 1-based counters
        # /// Nx number of values for x
        # /// Factor_k=Nj*Ni
        # /// Factor_j= Ni
        # /// Factor_i = 1
        # /// index = Factor_k*(k-1) + Factor_j*(j-1) + Factor_i(i-1) </remarks>
        #  in python things are zero-based but the idea is the same
        # /// </summary>
        if not self._add_language_independent:
           return
        
        start_get_data = time.time()

        matrix_size = self.calculate_factor()

        missing_row_symbol = self._pxmetadata_model.dataset.row_missing
        missing_cell_symbol = self._pxmetadata_model.dataset.cell_missing

        column_code_map = self.get_measurement_column_code_mapping()

        start_tidy = time.time()
        df = self._datadata.GetTidyDF(self._config.contvariable_code, column_code_map)

        end_tidy = time.time()
        time_used_tidy = end_tidy - start_tidy
        print("Time: GetTidyDF:", time_used_tidy)

        self.add_out_index(df)
        self.add_out_value(missing_cell_symbol, df)
        merged_df = self.add_missing_rows(matrix_size, missing_row_symbol, df)

        out_data = merged_df["out_value"].tolist()

        merged_df = merged_df.sort_values(by=["out_index"])
        formatter = DataFormatter(self._heading, self._for_get_data_by_varid)
        number_of_columns_per_line = formatter.calculate_line_break()

        out_model.data.set(out_data, number_of_columns_per_line)

        end_get_data = time.time()
        time_used_get_data = end_get_data - start_get_data
        print("Time: GetData:", time_used_get_data)

    def add_missing_rows(self, matrix_size, missing_row_symbol, df):
        matrix_df = pd.DataFrame({"out_index": range(matrix_size)})

        # Merge the two DataFrames
        merged_df = pd.merge(matrix_df, df, on="out_index", how="left")

        # Fill missing values with "MISSING"
        merged_df["out_value"].fillna(missing_row_symbol, inplace=True)
        return merged_df

    def add_out_value(self, missing_cell_symbol, df):
        conditions = [df["VALUE"] != "", df["SYMBOL"] != ""]

        choices = [df["VALUE"].astype(str), df["SYMBOL"].astype(str)]

        start = time.time()
        df["out_value"] = np.select(conditions, choices, missing_cell_symbol)
        end = time.time()
        time_used = end - start
        print("Time: numpy select in:", time_used)

    def add_out_index(self, df):
        columns_to_sum = []
        for col in self._for_get_data_by_varid.values():
            # Mapping the values using the dictionary
            contrib_col_name = "int_" + col._colname_in_dataframe
            df[contrib_col_name] = df[col._colname_in_dataframe].map(col._position_of_value) * col.factor
            columns_to_sum.append(contrib_col_name)
        df["out_index"] = df[columns_to_sum].sum(axis=1)

    def add_metaid_to_pxfile(self, out_model: PXFileModel) -> None:
        if self._add_language_independent:
            if self._metaid_table:
                out_model.meta_id.set(" ".join(self._metaid_table))

        for vari in self._metaid_valiable:
            out_model.meta_id.set(" ".join(self._metaid_valiable[vari]), vari, None, self._current_lang)

    def get_variable_list(self) -> List[str]:
        return self._stub + self._heading

    def get_measurement_column_code_mapping(self) -> dict:
        column_code_map = {}
        for measurement_var in self._pxmetadata_model.dataset.measurements:
            column_code_map[measurement_var.column_name] = measurement_var.code

        return column_code_map
    

    def map_aggregallowed_to_pxfile(self, out_model: PXFileModel):
        # Check if all values in the array are True
        if self._add_language_independent:
            all_true = all(instance.aggregation_allowed for instance in self._pxmetadata_model.dataset.measurements)
            out_model.aggregallowed.set(all_true)

    def map_title_to_pxfile(self, out_model: PXFileModel):
        lang = self._current_lang
        model = self._pxmetadata_model.dataset

        vari_list = self.get_variable_list()

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

    def map_time_dimension_to_pxfile(self, out_model: PXFileModel):
        my_periods = self._datadata.GetTimePeriodes(self._pxmetadata_model.dataset.time_dimension.column_name)

        my_funny_var_id = self._pxmetadata_model.dataset.time_dimension.label[self._current_lang]

        self._heading.append(my_funny_var_id)
        out_model.values.set(my_periods, my_funny_var_id, self._current_lang)
        out_model.codes.set(my_periods, my_funny_var_id, self._current_lang)
        out_model.variablecode.set(self._config.timevariable_code, my_funny_var_id, self._current_lang)
        out_model.variable_type.set("T", my_funny_var_id, self._current_lang)

        for_get_data = ForGetData(self._pxmetadata_model.dataset.time_dimension.column_name, my_periods)
        self._for_get_data_by_varid[my_funny_var_id] = for_get_data

    def map_coded_dimensions_to_pxfile(self, out_model: PXFileModel):
        if self._pxmetadata_model.dataset.coded_dimensions:
            lang = self._current_lang
            for my_var in self._pxmetadata_model.dataset.coded_dimensions:
                my_funny_var_id = my_var.label[lang]
                self._stub.append(my_funny_var_id)
                my_var_code = my_var.code if my_var.code is not None else my_var.column_name
                out_model.variablecode.set(my_var_code, my_funny_var_id, lang)
                my_codes: PxCodes = self._resolved_pxcodes_ids[my_var.codelist_id]

                my_pxcodes_helper = self._pxcodes_helper[my_var.codelist_id]

                temp_codes = my_pxcodes_helper.getCodes(lang)
                out_model.codes.set(temp_codes, my_funny_var_id, lang)

                temp_values = my_pxcodes_helper.getLabels(lang)
                out_model.values.set(temp_values, my_funny_var_id, lang)
                if my_codes.groupings:
                    my_domain_id = make_domain_id(my_var.codelist_id, self._current_lang)
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

    def map_measurements_to_pxfile(self, out_model: PXFileModel):
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



    # def makeVsFile(self,out_vs_model:_VSFileModel):
    def make_vs_file(self):
        if not self._pxmetadata_model.dataset.coded_dimensions:
            return
        
        for language in self._config.admin.valid_languages:

            for my_var in self._pxmetadata_model.dataset.coded_dimensions:

                out_vs_model = _VSFileModel()
                my_codes: PxCodes = self._resolved_pxcodes_ids[my_var.codelist_id]
                if my_codes.groupings:
                    vs_name = make_domain_id(my_var.codelist_id, language)
                    #vs_type = "G" if my_var.is_geo_variable_type else "V"
                    vs_type = "V" # TODO type could be V,H or N
                    out_vs_model.description.set("Name", vs_name)
                    out_vs_model.description.set("Type", vs_type)

                    my_pxcodes_helper = self._pxcodes_helper[my_var.codelist_id]
                    group_conter = 0
                    for groups in my_codes.groupings:
                        group_conter = group_conter + 1
                        group_key = str(group_conter)
                        out_vs_model.aggreg.set(group_key, groups.filename_base + "_" + language + ".agg")
                        self.make_agg_file(groups, vs_name, my_pxcodes_helper, language)
                    my_domain = make_domain_id(my_var.codelist_id, language)
                    out_vs_model.domain.set("1", my_domain)

                    
                    value_item_counter = 0
                    for my_item in my_pxcodes_helper._sorted_valueitems[language]:
                        value_item_counter = value_item_counter + 1
                        value_item_key = str(value_item_counter)
                        my_stripped_code = my_item.code.strip("'")
                        out_vs_model.valuecode.set(value_item_key, my_stripped_code)
                        my_stripped_text = my_item.label[language].strip("'")
                        out_vs_model.valuetext.set(value_item_key, my_stripped_text)

                    out_folder_format: str = self._config.admin.output_destination.agg_folder_format
                    out_folder = out_folder_format.format(id=self._pxmetadata_id)
                    out_file = out_folder + "/" + my_codes.id + "_" + language + ".vs"

                    with open(out_file, "w") as f:
                        print(out_vs_model, file=f)
                        print("File written to:", out_file)

    def make_agg_file(self, grouping: Grouping, vs_name: str, my_pxcodes_helper:HelperPxCodes, language:str):
        out_agg_model = AggFileModel()
        #aggreg_name = grouping.filename_base + "_" + language
        aggreg_name = grouping.label[language]
        out_agg_model.set("Aggreg", "Name", aggreg_name)
        out_agg_model.set("Aggreg", "Valueset", vs_name)
        item_counter = 0
        # section= "Aggreg"
        for item in grouping.valueitems:
            item_counter = item_counter + 1
            item_key = str(item_counter)
            groupcode = item.code
            valuetext = item.label[language]
            out_agg_model.set("Aggreg", item_key, groupcode)
            out_agg_model.set("Aggtext", item_key, valuetext)

            child_code_conter = 0
            #ordered_children = [code for code in my_pxcodes_helper.getCodes(language) if item.unordered_children and code in item.unordered_children]

            ordered_children:List[str] = []
            for code in my_pxcodes_helper.getCodes(language):
                if item.unordered_children and code in item.unordered_children:
                   ordered_children.append(code) 
            
            for child_code in ordered_children:
                child_code_conter = child_code_conter + 1
                child_code_key = str(child_code_conter)
                out_agg_model.set(groupcode, child_code_key, child_code)

        out_file = "example_data/pxbuild_output/" + str(grouping.filename_base) + "_" + language + ".agg"
        with open(out_file, "w") as f:
            print(out_agg_model, file=f)
            print("File written to:", out_file)
        print("i agg")
        print(grouping.filename_base)


def convert_to_pxdate_string(date_string: str, date_format: str) -> str:
    dtm_date = datetime.strptime(date_string, date_format)
    px_date_string = dtm_date.strftime(f"%Y%m%d %H:%M")

    return px_date_string


def make_domain_id(code_list_id: str, lang: str) -> str:
    domain_id = code_list_id + "_" + lang
    return domain_id

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

