import json

from typing import Dict

from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.input.pydantic_pxmetadata import PxMetadata
from pxbuild.models.input.pydantic_pxstatistics import PxStatistics
from pxbuild.models.input.pydantic_pxcodes import PxCodes

# Class for loading all jsons into pydantic. And nothing else.
class LoadedJsons:
    """
    Class for loading all jsons into pydantic. And nothing else.
    """

    def __init__(self, pxmetadata_id: str, config_file: str) -> None:
        self._pxmetadata_id = pxmetadata_id
        print("For pxmetadata_id:", self._pxmetadata_id, ", with config:", config_file)

        self._config = LoadedJsons.load_config(config_file)

        # todo if sourceType==File
        #      pxmetadataFormat="example_data/pxmetadata/{id}.json"
        pxmetadata_format = self._config.admin.px_metadata_resource.adress_format
        pxmetadata_file = pxmetadata_format.format(id=self._pxmetadata_id)

        with open(pxmetadata_file, encoding="utf-8-sig") as f:
            pxmetadata_json = json.loads(f.read())
        # endif

        self._pxmetadata_model = PxMetadata(**pxmetadata_json)

        # pxstatisticsFormat="example_data/pxstatistics/pxstatistics_{id}.json"
        pxstatistics_format = self._config.admin.px_statistics_resource.adress_format
        pxstatistics_file = pxstatistics_format.format(id=self._pxmetadata_model.dataset.statistics_id)

        with open(pxstatistics_file, encoding="utf-8-sig") as f:
            json1 = json.loads(f.read())
        self._pxstatistics = PxStatistics(**json1)

        self._resolved_pxcodes_ids: Dict[str, PxCodes] = {}

        if self._pxmetadata_model.dataset.coded_dimensions:

            # pxcodesFormat="example_data/pxcodes/{id}.json"
            pxcodes_format = self._config.admin.px_codes_resource.adress_format
            for dimension in self._pxmetadata_model.dataset.coded_dimensions:

                if dimension.codelist_id not in self._resolved_pxcodes_ids:
                    tmp_path = pxcodes_format.format(id=dimension.codelist_id)
                    with open(tmp_path, encoding="utf-8-sig") as f:
                        json1 = json.loads(f.read())

                    self._resolved_pxcodes_ids[dimension.codelist_id] = PxCodes(**json1)

    def get_config(self) -> PxbuildConfig:
        return self._config

    def get_pxmetadata(self) -> PxMetadata:
        return self._pxmetadata_model

    def get_pxstatistics(self) -> PxStatistics:
        return self._pxstatistics

    def get_resolved_pxcodes_ids(self) -> Dict[str, PxCodes]:
        """
        PxCodes as a function of codelist_id.

        Parameters:
        a (int): The first number to add.
        b (int): The second number to add.

        Returns: Empty if the dataset has no coded_dimensions
        """
        return self._resolved_pxcodes_ids

    @staticmethod
    def load_config(config_file: str) -> PxbuildConfig:
        with open(config_file, encoding="utf-8-sig") as f:
            config_json = json.loads(f.read())
        return PxbuildConfig(**config_json)
