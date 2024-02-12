from typing import List

from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.input.pydantic_pxmetadata import PxMetadata
from pxbuild.models.input.helper_pxcodes import HelperPxCodes
from pxbuild.models.input.pydantic_pxcodes import Grouping
from pxbuild.models.middle.dims import Dims

from pxbuild.models.output.agg_vs.vs_file_model import _VSFileModel
from pxbuild.models.output.agg.agg_file_model import AggFileModel


# Class for making agg and vs files
class SupportFiles:
    def __init__(self, pxmetadata: PxMetadata, config: PxbuildConfig, dims: Dims, pxmetadata_id: str) -> None:
        self._pxmetadata_model = pxmetadata
        self._config = config
        self._dims = dims
        self._pxmetadata_id = pxmetadata_id

    def make_vs_file(self):
        if not self._pxmetadata_model.dataset.coded_dimensions:
            return

        for language in self._config.admin.valid_languages:
            for n_var in self._dims.coded_dimensions:

                # my_var = n_var.get_pydantic()
                out_vs_model = _VSFileModel()
                my_codes: HelperPxCodes = n_var.get_helper_pxcodes()
                if n_var.groupings():
                    vs_name = n_var.get_domain_id(language)
                    # vs_type = "G" if my_var.is_geo_variable_type else "V"
                    vs_type = "V"  # TODO type could be V,H or N
                    out_vs_model.description.set("Name", vs_name)
                    out_vs_model.description.set("Type", vs_type)

                    group_conter = 0
                    for groups in n_var.groupings():
                        group_conter = group_conter + 1
                        group_key = str(group_conter)
                        out_vs_model.aggreg.set(group_key, groups.filename_base + "_" + language + ".agg")
                        self.make_agg_file(groups, vs_name, my_codes, language)

                    out_vs_model.domain.set("1", vs_name)

                    value_item_counter = 0
                    for my_item in my_codes._sorted_valueitems[language]:
                        value_item_counter = value_item_counter + 1
                        value_item_key = str(value_item_counter)
                        my_stripped_code = my_item.code.strip("'")
                        out_vs_model.valuecode.set(value_item_key, my_stripped_code)
                        my_stripped_text = my_item.label[language].strip("'")
                        out_vs_model.valuetext.set(value_item_key, my_stripped_text)

                    out_folder_format: str = self._config.admin.output_destination.agg_folder_format
                    out_folder = out_folder_format.format(id=self._pxmetadata_id)
                    out_file = out_folder + "/" + my_codes.id() + "_" + language + ".vs"

                    with open(out_file, "w") as f:
                        print(out_vs_model, file=f)
                        print("File written to:", out_file)

    def make_agg_file(self, grouping: Grouping, vs_name: str, my_pxcodes_helper: HelperPxCodes, language: str):
        out_agg_model = AggFileModel()
        # aggreg_name = grouping.filename_base + "_" + language
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
            ordered_children: List[str] = []
            for code in my_pxcodes_helper.get_codes(language):
                if item.unordered_children and code in item.unordered_children:
                    ordered_children.append(code)

            for child_code in ordered_children:
                child_code_conter = child_code_conter + 1
                child_code_key = str(child_code_conter)
                out_agg_model.set(groupcode, child_code_key, child_code)

        out_folder_format: str = self._config.admin.output_destination.agg_folder_format
        out_folder = out_folder_format.format(id=self._pxmetadata_id)
        out_file = out_folder + "/" + str(grouping.filename_base) + "_" + language + ".agg"
        with open(out_file, "w") as f:
            print(out_agg_model, file=f)
            print("File written to:", out_file)
        print("i agg")
        print(grouping.filename_base)
