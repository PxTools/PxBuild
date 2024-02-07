from datetime import datetime
from typing import List, Dict

from pxbuild.models.input.pydantic_pxmetadata import PxMetadata, AttachmentItem
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.input.pydantic_pxstatistics import PxStatistics

from pxbuild.models.output.pxfile.px_file_model import PXFileModel

from .helpers.datadata_helpers.datadatasource import Datadatasource
from .helpers.datadata_helpers.main_data import MapData
from .helpers.loaded_jsons import LoadedJsons
from .helpers.support_files import SupportFiles

from pxbuild.models.middle.dims import Dims


class LoadFromPxmetadata:
    LabelConstructionOptionDict = {
        "LabelConstructionOption.code": 0,
        "LabelConstructionOption.text": 1,
        "LabelConstructionOption.code_text": 2,
        "LabelConstructionOption.text_code": 3,
    }

    PriceTypeDict = {"PriceType.current": "C", "PriceType.fixed": "F"}

    def __init__(self, pxmetadata_id: str, config_file: str) -> None:
        self._pxmetadata_id = pxmetadata_id

        self._loaded_jsons: LoadedJsons = LoadedJsons(pxmetadata_id, config_file)

        self._config = self._loaded_jsons.get_config()
        self._pxmetadata_model = self._loaded_jsons.get_pxmetadata()
        self._pxstatistics = self._loaded_jsons.get_pxstatistics()

        self._datadata = Datadatasource(self._pxmetadata_model.dataset.data_file, self._config)

        self._dims = Dims(self._loaded_jsons, self._datadata)

        ##################
        self.models_for_pytest: dict = {}  # Todo make perfect reader, and let the pytest read the files

        self._last_updated = self.get_last_updated(self._pxstatistics)

        out_model = PXFileModel()

        # loop in languages
        self._add_language_independent = True  # like AXIS_VERSION
        for language in self._config.admin.valid_languages:

            self._current_lang = language
            self._contact_string = self.get_contact_string(self._pxstatistics, language)

            self.map_pxbuildconfig_to_pxfile(self._config, language, out_model)
            self.map_pxmetadata_to_pxfile(self._pxmetadata_model, out_model)
            self.map_pxstatistics_to_pxfile(self._pxstatistics, out_model)

            self.map_coded_dimensions_to_pxfile(out_model)
            self.map_measurements_to_pxfile(out_model)
            self.map_decimals_to_pxfile(out_model)
            self.map_time_dimension_to_pxfile(out_model)
            self.map_stub_heading_to_pxfile(out_model)
            self.map_title_to_pxfile(out_model)
            self.map_aggregallowed_to_pxfile(out_model)

            self.map_metaid_to_pxfile(out_model)
            self.map_cellnote_to_pxfile(out_model)

            fixdata = MapData(self._datadata, self._pxmetadata_model, self._config, self._dims, self._current_lang)
            fixdata.map_data(out_model)

            if not self._config.admin.build_multilingual_files:
                write_output(
                    self._pxmetadata_id, self._config.admin.output_destination.px_folder_format, out_model, language
                )

                self.models_for_pytest[language] = out_model
                out_model = PXFileModel()
            else:
                self._add_language_independent = False

        if self._config.admin.build_multilingual_files:
            write_output(self._pxmetadata_id, self._config.admin.output_destination.px_folder_format, out_model)
            self.models_for_pytest["multi"] = out_model

        support = SupportFiles(self._pxmetadata_model, self._config, self._dims, self._pxmetadata_id)
        support.make_vs_file()

    def map_metaid_to_pxfile(self, out_model: PXFileModel) -> None:
        if self._add_language_independent:
            metaid_table: List[str] = []
            if self._pxmetadata_model.dataset.meta_id:
                metaid_table += self._pxmetadata_model.dataset.meta_id
            if self._pxstatistics.meta_id:
                metaid_table += self._pxstatistics.meta_id
            if metaid_table:
                out_model.meta_id.set(" ".join(metaid_table))

        lang = self._current_lang
        if self._dims.coded_dimensions:
            for n_var in self._dims.coded_dimensions:
                my_var = n_var.get_pydantic()
                if my_var.meta_id:
                    out_model.meta_id.set(" ".join(my_var.meta_id), n_var.get_label(lang), None, lang)

        contdim = self._dims.contdim
        for my_cont in self._pxmetadata_model.dataset.measurements:
            if my_cont.meta_id:
                out_model.meta_id.set(
                    " ".join(my_cont.meta_id), contdim.get_label(lang), my_cont.label[self._current_lang], lang
                )

    def map_cellnote_to_pxfile(self, out_model: PXFileModel) -> None:
        if not self._pxmetadata_model.dataset.cell_notes:
            return
        # the input is code-based , the output is dimension-order and label-based
        lang = self._current_lang

        dimension_in_order = self._dims.get_dims_in_output_order()

        for cellnote in self._pxmetadata_model.dataset.cell_notes:
            valueCodeBydimensionCode = self.get_valueCode_by_dimensionCode(cellnote.attachment)
            valueTextsForSubkey: List[str] = []
            for dim in dimension_in_order:
                dimCode = dim.get_code()
                if dimCode in valueCodeBydimensionCode:
                    valueCode = valueCodeBydimensionCode[dimCode]
                    valueText = dim.get_valuelabel(lang, valueCode)
                    valueTextsForSubkey.append(valueText)
                else:
                    valueTextsForSubkey.append("*")

            if cellnote.is_mandatory:
                out_model.cellnotex.set(cellnote.text[lang], valueTextsForSubkey, lang)
            else:
                out_model.cellnote.set(cellnote.text[lang], valueTextsForSubkey, lang)

    def get_valueCode_by_dimensionCode(self, attachments: List[AttachmentItem]) -> Dict[str, str]:
        my_out: Dict[str, str] = {}
        for attachment in attachments:
            my_out[attachment.dimension_code] = attachment.value_code

        return my_out

    def map_aggregallowed_to_pxfile(self, out_model: PXFileModel):
        # Check if all values in the array are True
        if self._add_language_independent:
            all_true = all(instance.aggregation_allowed for instance in self._pxmetadata_model.dataset.measurements)
            out_model.aggregallowed.set(all_true)

    def map_title_to_pxfile(self, out_model: PXFileModel):
        lang = self._current_lang
        model = self._pxmetadata_model.dataset

        tmp_list = self._dims.get_dimcodes_in_output_order()
        vari_list = self._dims.get_as_lables(tmp_list, lang)

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
        lang = self._current_lang
        seen = False
        if self._dims.get_headingcodes():

            my_headings: List[str] = self._dims.get_as_lables(self._dims.get_headingcodes(), lang)
            out_model.heading.set(my_headings, lang)
            seen = True

        if self._dims.get_stubcodes():
            my_stubs: List[str] = self._dims.get_as_lables(self._dims.get_stubcodes(), lang)

            out_model.stub.set(my_stubs, lang)
            seen = True

        if not seen:
            raise Exception("Sorry, both stub and heading are empty.")

    def map_time_dimension_to_pxfile(self, out_model: PXFileModel):
        time = self._dims.time
        lang = self._current_lang

        out_model.values.set(time.get_labels(lang), time.get_label(lang), lang)
        out_model.codes.set(time.get_codes(), time.get_label(lang), lang)
        out_model.variablecode.set(time.get_code(), time.get_label(lang), lang)
        out_model.variable_type.set(time.get_variabletype(), time.get_label(lang), lang)

    def map_coded_dimensions_to_pxfile(self, out_model: PXFileModel):

        if self._dims.coded_dimensions:
            lang = self._current_lang
            for n_var in self._dims.coded_dimensions:

                out_model.variablecode.set(n_var.get_code(), n_var.get_label(lang), lang)
                out_model.variable_type.set(n_var.get_variabletype(), n_var.get_label(lang), lang)
                out_model.codes.set(n_var.get_codes(lang), n_var.get_label(lang), lang)
                out_model.values.set(n_var.get_labels(lang), n_var.get_label(lang), lang)

                my_var = n_var.get_pydantic()
                my_funny_var_id = n_var.get_label(lang)

                if n_var.groupings():
                    out_model.domain.set(n_var.get_domain_id(lang), my_funny_var_id, lang)

                out_model.prestext.set(
                    self.LabelConstructionOptionDict[str(my_var.label_construction_option)], my_funny_var_id, lang
                )

                if not n_var.elimination_possible:
                    out_model.elimination.set("NO", my_funny_var_id, lang)
                else:
                    label = n_var.get_elimination_label(lang)
                    if label:
                        out_model.elimination.set(label, my_funny_var_id, lang)
                    else:
                        out_model.elimination.set("YES", my_funny_var_id, lang)

                if my_var.doublecolumn:
                    out_model.doublecolumn.set(my_var.doublecolumn, my_funny_var_id, lang)

                # Note on variable
                if my_var.notes:
                    for note in my_var.notes:
                        if note.is_mandatory:
                            out_model.notex.set(note.text[lang], my_funny_var_id, lang)
                        else:
                            out_model.note.set(note.text[lang], my_funny_var_id, lang)

                # Note on a value in variale
                my_value_notes = n_var.get_valuenotes()
                if my_value_notes:
                    for valuecode in my_value_notes:
                        for note in my_value_notes[valuecode]:
                            valuelabel = n_var.get_valuelabel(lang, valuecode)
                            if note.is_mandatory:
                                out_model.valuenotex.set(note.text[lang], n_var.get_label(lang), valuelabel, lang)
                            else:
                                out_model.valuenote.set(note.text[lang], n_var.get_label(lang), valuelabel, lang)

    def map_measurements_to_pxfile(self, out_model: PXFileModel):
        contdim = self._dims.contdim
        lang = self._current_lang
        out_model.units.set(
            "Hi, it seems this has to be here to aviod a crash. For multi-content at least.", None, lang
        )

        for my_cont in self._pxmetadata_model.dataset.measurements:

            my_funny_cont_id = my_cont.label[self._current_lang]

            out_model.seasadj.set(my_cont.is_seasonally_adjusted or False, my_funny_cont_id, lang)
            out_model.dayadj.set(my_cont.is_workingdays_adjusted or False, my_funny_cont_id, lang)
            out_model.units.set(my_cont.unit_of_measure[self._current_lang], my_funny_cont_id, lang)
            out_model.contact.set(self._contact_string, my_funny_cont_id, lang)
            out_model.last_updated.set(self._last_updated, my_funny_cont_id, lang)

            if my_cont.reference_period and my_cont.reference_period[lang]:
                out_model.refperiod.set(my_cont.reference_period[lang], my_funny_cont_id, lang)

            if my_cont.base_period and my_cont.base_period[lang]:
                out_model.baseperiod.set(my_cont.base_period[self._current_lang], my_funny_cont_id, lang)

            if my_cont.show_decimals > 0:
                out_model.precision.set(my_cont.show_decimals, contdim.get_label(lang), my_funny_cont_id, lang)

            # optional with no default
            if my_cont.price_type:
                out_model.cfprices.set(self.PriceTypeDict[str(my_cont.price_type)], my_funny_cont_id, lang)

            # Note on a contentvalue
            if my_cont.notes:
                for note in my_cont.notes:
                    if note.is_mandatory:
                        out_model.valuenotex.set(note.text[lang], contdim.get_label(lang), my_funny_cont_id, lang)
                    else:
                        out_model.valuenote.set(note.text[lang], contdim.get_label(lang), my_funny_cont_id, lang)

        out_model.values.set(contdim.get_labels(lang), contdim.get_label(lang), lang)
        out_model.codes.set(contdim.get_codes(), contdim.get_label(lang), lang)
        out_model.variablecode.set(contdim.get_code(), contdim.get_label(lang), lang)
        out_model.variable_type.set(contdim.get_variabletype(), contdim.get_label(lang), lang)

    def map_decimals_to_pxfile(self, out_model: PXFileModel):
        if self._add_language_independent:
            show_decimals_values = [instance.show_decimals for instance in self._pxmetadata_model.dataset.measurements]

            if self._pxmetadata_model.dataset.stored_decimals:
                out_model.decimals.set(max(self._pxmetadata_model.dataset.stored_decimals, max(show_decimals_values)))
            else:
                out_model.decimals.set(max(show_decimals_values))

            out_model.showdecimals.set(min(show_decimals_values))

    def get_contact_string(self, in_data: PxStatistics, language: str) -> str:
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

        formatted_string = convert_to_pxdate_string(last_updated_date, self._pxstatistics.upcoming_releases_dateformat)

        return formatted_string

    def get_next_update(self, in_model: PxStatistics) -> str:
        last_updated_date = ""
        if in_model.upcoming_releases is None:
            return last_updated_date

        if len(in_model.upcoming_releases) < 2:
            return last_updated_date

        last_updated_date = in_model.upcoming_releases[1]

        formatted_string = convert_to_pxdate_string(last_updated_date, self._pxstatistics.upcoming_releases_dateformat)

        return formatted_string

    def map_pxstatistics_to_pxfile(self, in_model: PxStatistics, out_model: PXFileModel):
        lang = self._current_lang

        out_model.subject_area.set(in_model.subject_text[lang], lang)
        if self._add_language_independent:
            out_model.subject_code.set(in_model.subject_code)

            next_update = self.get_next_update(self._pxstatistics)
            if next_update:
                out_model.next_update.set(next_update)

        # out_model.update_frequency.set() Hmm is not listed as language dependent in pdf

    def map_pxmetadata_to_pxfile(self, in_model: PxMetadata, out_model: PXFileModel):
        lang = self._current_lang
        if self._add_language_independent:
            out_model.tableid.set(in_model.dataset.table_id)
            out_model.matrix.set("tab_" + in_model.dataset.table_id)
            if in_model.dataset.official_statistics:
                out_model.official_statistics.set(in_model.dataset.official_statistics)
            if in_model.dataset.copyright:
                out_model.copyright.set(in_model.dataset.copyright)
            if in_model.dataset.first_published:
                out_model.first_published.set(in_model.dataset.first_published)

            # The SYNONYMS keyword is language independent. So, all langs go into one for multilingual_files.
            temp_tags: List[str] = []
            if self._config.admin.build_multilingual_files:
                for language in self._config.admin.valid_languages:
                    temp_tags += in_model.dataset.search_keywords[language]
            else:
                temp_tags = in_model.dataset.search_keywords[lang]
            if temp_tags:
                out_model.synonyms.set(" ".join(temp_tags))

        out_model.contents.set(in_model.dataset.table_id + ": " + in_model.dataset.base_title[lang] + ",", lang)
        if in_model.dataset.notes:
            for note in in_model.dataset.notes:
                if note.is_mandatory:
                    out_model.notex.set(note.text[lang], None, lang)
                else:
                    out_model.note.set(note.text[lang], None, lang)

    def map_pxbuildconfig_to_pxfile(self, in_config: PxbuildConfig, current_lang: str, out_model: PXFileModel):
        if self._add_language_independent:
            out_model.language.set(current_lang)
            if in_config.admin.build_multilingual_files:
                out_model.languages.set(in_config.admin.valid_languages)
            out_model.axis_version.set(str(in_config.axis_version))
            out_model.charset.set(str(in_config.charset))
            out_model.codepage.set(str(in_config.code_page))
            out_model.descriptiondefault.set((in_config.description_default or False))
            if not in_config.admin.skip_creation_date:
                out_model.creation_date.set(get_current_time())

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


def get_current_time() -> str:
    """
    Returns the current time as a string in the format CCYYMMDD hh:mm
    """
    from datetime import datetime

    return datetime.now().strftime("%Y%m%d %H:%M")


def write_output(
    pxmetadata_id: str, px_folder_format: str, out_model: PXFileModel, language: str | None = None
) -> None:
    temp_tabid = pxmetadata_id
    out_folder = px_folder_format.format(id=temp_tabid)
    language_part = ""
    if language:
        language_part = "_" + language

    out_file = f"{out_folder}/tab_{temp_tabid}{language_part}.px"

    with open(out_file, "w", encoding="cp1252") as f:
        print(out_model, file=f)

    print("File written to:", out_file)
