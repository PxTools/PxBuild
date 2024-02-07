# from .pydantic_pxcodes import PxCodes, Grouping, Valueitem, Note
from pxbuild.controll.helpers.datadata_helpers.datadatasource import Datadatasource
from pxbuild.controll.helpers.loaded_jsons import LoadedJsons

from typing import Dict, List, Optional

from .time_dim import TimeDim
from .cont_dim import ContDim
from .coded_dim import CodedDim
from .abstract_dim import AbstractDim

from pxbuild.models.input.helper_pxcodes import HelperPxCodes


class Dims:
    def __init__(self, in_loaded_jsons: LoadedJsons, in_datadatasource: Datadatasource) -> None:

        meta = in_loaded_jsons.get_pxmetadata().dataset

        self.dim_by_code: Dict[str, AbstractDim] = {}
        self._stubCodes: List[str] = []
        self._headingCodes: List[str] = []

        self.coded_dimensions: List[CodedDim] = []

        # CodedDimensions
        if meta.coded_dimensions:
            # In input 2 CodedDimensions can share a codelist. This cannot be expressed in output.
            pxcodes_by_codelist_id = in_loaded_jsons.get_resolved_pxcodes_ids()
            pxcodes_helper_by_codelist_id: Dict[str, HelperPxCodes] = {}
            for codelist_id in pxcodes_by_codelist_id:
                pxcodes_helper_by_codelist_id[codelist_id] = HelperPxCodes(
                    pxcodes_by_codelist_id[codelist_id], in_loaded_jsons.get_config().admin.valid_languages
                )

            for n_dim in meta.coded_dimensions:
                n_dim.codelist_id
                tempCD = CodedDim(n_dim, pxcodes_helper_by_codelist_id[n_dim.codelist_id], in_loaded_jsons)
                n_code = tempCD.get_code()
                self._stubCodes.append(n_code)
                self.dim_by_code[n_code] = tempCD
                self.coded_dimensions.append(tempCD)

        # CONT
        self.contdim: ContDim = ContDim(in_loaded_jsons)
        contdim_code = self.contdim.get_code()
        self._headingCodes.append(contdim_code)
        self.dim_by_code[contdim_code] = self.contdim

        # TIME
        self.time: TimeDim = TimeDim(in_loaded_jsons, in_datadatasource)
        time_code = self.time.get_code()
        self._headingCodes.append(time_code)
        self.dim_by_code[time_code] = self.time

    def get_dims_in_output_order(self) -> List[AbstractDim]:
        my_out: List[AbstractDim] = []
        for code in self._stubCodes + self._headingCodes:
            my_out.append(self.dim_by_code[code])
        return my_out

    def get_stubcodes(self) -> List[str]:
        return self._stubCodes

    def get_headingcodes(self) -> List[str]:
        return self._headingCodes

    def get_dimcodes_in_output_order(self) -> List[str]:
        return self._stubCodes + self._headingCodes

    def get_as_lables(self, codes: List[str], language: str) -> List[str]:
        my_out: List[str] = []
        for code in codes:
            my_out.append(self.dim_by_code[code].label_by_lang[language])
        return my_out
