import json
from typing import List

from pxtool.models.input.pydantic_pxmetadata import PxMetadata
from pxtool.models.input.pydantic_pxtoolconfig import Pxtoolconfig
from pxtool.models.input.pydantic_pxcodes import PxCodes
from pxtool.models.input.pydantic_pxstatistics import PxStatistics

from pxtool.models.output.pxfile.px_file_model import PXFileModel


class LoadFromPxmetadata():
   def __init__(self, filename: str, sourceType:str) -> None:
    self._filename = filename
    print(self._filename)

    with open('example_data/pxtoolconfig/ssb_config.json', encoding="utf-8-sig") as f:
        config_json = json.loads(f.read())
    self._config = Pxtoolconfig(**config_json)

    #todo if sourceType==File
    pxmetadataFormat="example_data/pxmetadata/{id}.json"
    pxmetadataFil=pxmetadataFormat.format(id=self._filename)
    with open(pxmetadataFil, encoding="utf-8-sig") as f:
        pxmetadata_json = json.loads(f.read())
    #endif

    self._pxmetadata_model = PxMetadata(**pxmetadata_json)

    #todo if sourceType==File  Hmm må det være enten api eller fil, ikke pxcodes på file og statistics på api?
    pxstatisticsFormat="example_data/pxstatistics/pxstatistics_{id}.json"
    pxstatisticsFil=pxstatisticsFormat.format(id=self._pxmetadata_model.dataset.statistics_id)
    with open(pxstatisticsFil, encoding="utf-8-sig") as f:
        json1 = json.loads(f.read())
    self._pxstatistics = PxStatistics(**json1)

    if self._pxmetadata_model.dataset.coded_dimensions:
      self._resolved_pxcodes_ids={}
      pxcodesFormat="example_data/pxcodes/{id}.json"
      for myVar in self._pxmetadata_model.dataset.coded_dimensions:

        if not myVar.codelist_id in self._resolved_pxcodes_ids:
           tmpPath= pxcodesFormat.format(id=myVar.codelist_id)
           with open(tmpPath, encoding="utf-8-sig") as f:
              json1 = json.loads(f.read())
           self._resolved_pxcodes_ids[myVar.codelist_id] = PxCodes(**json1)


    ## loop in languages
    self._current_lang="no" #todo
    out_model = PXFileModel()
    out_model.language.set(self._current_lang)

    self.MapPxtoolconfigToPXFileModel(self._config, out_model)

    self.AddPxMetadataToPXFileModel(self._pxmetadata_model, out_model)


    if self._pxmetadata_model.dataset.coded_dimensions:
      for my_var in self._pxmetadata_model.dataset.coded_dimensions: 
          
          my_funny_var_id = my_var.label[self._current_lang]
          my_var_code = my_var.code if my_var.code is not None else my_var.column_name
          out_model.variablecode.set(my_var_code, my_funny_var_id ,self._current_lang)
          my_codes:PxCodes = self._resolved_pxcodes_ids[my_var.codelist_id]

          out_codes=[]
          out_values =[]
          #todo  sortert liste
          for code in my_codes.codes:
             out_codes.append(code.code)
             out_values.append(code.label[self._current_lang])

          out_model.values.set(out_values,my_funny_var_id,self._current_lang)   
          out_model.codes.set(out_codes,my_funny_var_id,self._current_lang) 
          
        #self.AddPxCodesToPXFileModel(self._pxmetadata_model, out_model)

    if self._pxmetadata_model.dataset.measurements:
        my_funny_var_id = self._config.contvariable # TODO må ha en dict her 
        out_codes=[]
        out_values =[]
        for my_cont in self._pxmetadata_model.dataset.measurements: 
          my_cont_code = my_cont.code if my_cont.code is not None else my_cont.column_name
          out_codes.append(my_cont_code)
          out_values.append(my_cont.label[self._current_lang])

        out_model.values.set(out_values, my_funny_var_id, self._current_lang)
        out_model.codes.set(out_codes, my_funny_var_id,self._current_lang)  


    #its time
    my_periods = self.GetTimePeriodes(self._pxmetadata_model)


#    self._pxmetadata_model.dataset.time_dimension.column_name
#    self._pxmetadata_model.dataset.time_dimension.label

    my_funny_var_id=self._pxmetadata_model.dataset.time_dimension.label[self._current_lang]
    out_model.values.set(my_periods, my_funny_var_id, self._current_lang)
    out_model.codes.set(my_periods, my_funny_var_id,self._current_lang) 


    print("outmodel:\n",out_model)

    



    #def  AddPxCodesToPXFileModel(self, in_model:PxMetadata , out_model:PXFileModel):
    #  lang=self._current_lang
    #  out_model.tableid.set(in_model.dataset.table_id)
    #  out_model.contents.set(in_model.dataset.base_title[lang],lang)

   def  AddPxMetadataToPXFileModel(self, in_model:PxMetadata , out_model:PXFileModel):
      lang=self._current_lang
      out_model.tableid.set(in_model.dataset.table_id)
      out_model.contents.set(in_model.dataset.base_title[lang],lang)

   def GetTimePeriodes(self, in_model:PxMetadata) -> List[str]:
       #todo: in python 3.11 using best practises, I want to select all distinct values from a given column in a parquet file?
       return ["T1","T2"]

   def MapPxtoolconfigToPXFileModel(self, in_config:Pxtoolconfig , out_model:PXFileModel):

       out_model.axis_version.set(str(in_config.axis_version))
       out_model.charset.set(str(in_config.charset))
       out_model.codepage.set(str(in_config.code_page))

       out_model.descriptiondefault.set((in_config.description_default or False))
       out_model.contvariable.set(str(in_config.contvariable))
       out_model.datasymbol1.set(str(in_config.datasymbol1))
       out_model.datasymbol2.set(str(in_config.datasymbol2))
       out_model.datasymbol3.set(str(in_config.datasymbol3))
       out_model.datasymbol4.set(str(in_config.datasymbol4))
       out_model.datasymbol5.set(str(in_config.datasymbol5))
       out_model.datasymbol6.set(str(in_config.datasymbol6))
       out_model.datasymbolnil.set(str(in_config.datasymbol_nil))
       out_model.datasymbolsum.set(str(in_config.datasymbol_sum))
       #out_model.source.set("en") = ...

        
