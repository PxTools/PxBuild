import json

from pxtool.models.input.pydantic_pxmetadata import PxMetadata
from pxtool.models.input.pydantic_pxtoolconfig import Pxtoolconfig
from pxtool.models.input.pydantic_pxcodes import PxCodes
from pxtool.models.input.pydantic_pxstatistics import PxStatistics

from pxtool.models.output.pxfile.px_file_model import PXFileModel


class LoadFromPxmetadata():
   
    
   def __init__(self, filename: str, sourceType:str) -> None:
    self._filename = filename

    out_model = PXFileModel()

    with open('example_data/pxtoolconfig/ssb_config.json', encoding="utf-8-sig") as f:
        config_json = json.loads(f.read())
    self._config = Pxtoolconfig(**config_json)

    

    self.GetKeywordsFromConfig(self._config, out_model)
## test

    with open('example_data/pxcodes/tab07459_AlleAldre00B.json', encoding="utf-8-sig") as f:
        json1 = json.loads(f.read())
   # print("pxcodes:", PxCodes(**json1) )
    with open('example_data/pxstatistics/pxstatistics_8246.json', encoding="utf-8-sig") as f:
        json1 = json.loads(f.read())
    print("pxstatistics:", PxStatistics(**json1) )


## end test


    #print("Config pre:", config_json)
    #print("Config:", self._config)
    print(self._filename)
    with open('example_data/pxmetadata/'+ self._filename +'.json', encoding="utf-8-sig") as f:
        pxmetadata_json = json.loads(f.read())

    pxmetadata_model = PxMetadata(**pxmetadata_json)

    pxmetadata_model.dataset.table_id
    pxmetadata_model.dataset.documnet_id


   def GetKeywordsFromConfig(self, in_config:Pxtoolconfig , out_model:PXFileModel):
       out_model.axis_version.set(str(in_config.axis_version))
       out_model.charset.set(str(in_config.charset))
       out_model.codepage.set(str(in_config.code_page))

       myBool:bool = in_config.description_default or False

       out_model.descriptiondefault.set(myBool)
    
       print("outmodel:",out_model ) 
