import pytest
from pxbuild.controll.helpers.datadata_helpers.datadatasource import Datadatasource, PxDataSourceError
from pxbuild.controll.helpers.loaded_jsons import LoadedJsons


class TestDatadataValidation:
    def test_duplicate_column_name_raises(self):
        with pytest.raises(PxDataSourceError):
            Datadatasource("duplicate_column_name.csv", LoadedJsons.load_config("testdata/BadData/test_config.json"))

    def test_has_status_column_but_no_measure_column_raises(self):
        with pytest.raises(PxDataSourceError):
            Datadatasource(
                "has_status_column_but_no_measure_column.csv",
                LoadedJsons.load_config("testdata/BadData/test_config.json"),
            )

    def test_bad_value_in_status_column_raises(self):
        with pytest.raises(PxDataSourceError):
            Datadatasource(
                "bad_value_in_status_column.csv", LoadedJsons.load_config("testdata/BadData/test_config.json")
            )
