import json
from datetime import datetime
from typing import List

from pxtool.models.input.pydantic_pxmetadata import PxMetadata
from pxtool.models.input.pydantic_pxtoolconfig import Pxtoolconfig
from pxtool.models.input.pydantic_pxcodes import PxCodes
from pxtool.models.input.pydantic_pxstatistics import PxStatistics

from pxtool.models.output.pxfile.px_file_model import PXFileModel

from .datafile import ParquetDatasource

class LoadFromPxmetadata():
   LabelConstructionOptionDict={"LabelConstructionOption.text":0, "LabelConstructionOption.code":1,"LabelConstructionOption.text_code":3, "LabelConstructionOption.code_text":2}


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

    
      filePath='example_data/parquet_files/output_file03024.parquet' 
      self._parquet = ParquetDatasource(filePath)
      #self._parquet.PrintColumns()

      ##################
      ## loop in languages
      self._current_lang="no" #todo
      self._contact_string = self.GetContactString(self._pxstatistics)
      self._last_updated = self.GetLastUpdated(self._pxstatistics) 
      self._stub=[]
      self._heading=[self._config.contvariable[self._current_lang] ]

      out_model = PXFileModel()
      out_model.language.set(self._current_lang)

      self.MapPxtoolconfigToPXFileModel(self._config, out_model)

      self.AddPxMetadataToPXFileModel(self._pxmetadata_model, out_model)

      self.AddPxStatisticsToPXFileModel(self._pxstatistics, out_model)

      self.MapCodedDimensions(out_model)

      self.MapMeasurements(out_model)
   
      self.MapDecimals(out_model)

      self.MapTimeDimension(out_model)

      self.MapStubHeading(out_model)

      self.MapTitle(out_model)

      self.MapAggregallowed(out_model)
      
      print("outmodel:\n",out_model)

   def MapAggregallowed(self, out_model:PXFileModel):
      # Check if all values in the array are True
      all_true = all(instance.aggregation_allowed for instance in self._pxmetadata_model.dataset.measurements)
      out_model.aggregallowed.set(all_true)

   def MapTitle(self, out_model:PXFileModel):
      lang = self._current_lang
      model = self._pxmetadata_model.dataset 

      vari_list = self._stub + self._heading 

      tmp_string = ", ".join(vari_list[:-1]) 

      title = model.table_id + ": " + model.base_title[lang] + ", " +self._config.admin.the_word_by[lang]+ " " + tmp_string +" " + self._config.admin.the_word_and[lang] + " "+ vari_list[-1];  

      out_model.title.set(title,self._current_lang)

   def MapStubHeading(self, out_model:PXFileModel):
      if self._heading:
         out_model.heading.set(self._heading, self._current_lang)

      if self._stub:
         out_model.stub.set(self._stub, self._current_lang)

      if not self._stub and not self._heading:
         raise Exception("Sorry, both stub and heading are empty.")
      
   def MapTimeDimension(self, out_model:PXFileModel):
      my_periods = self._parquet.GetTimePeriodes(self._pxmetadata_model.dataset.time_dimension.column_name) 

      my_funny_var_id=self._pxmetadata_model.dataset.time_dimension.label[self._current_lang]

      self._heading.append(my_funny_var_id)
      out_model.values.set(my_periods, my_funny_var_id, self._current_lang)
      out_model.codes.set(my_periods, my_funny_var_id,self._current_lang) 
      out_model.variablecode.set(self._config.timevariable_code, my_funny_var_id, self._current_lang)  
      out_model.variable_type.set("T", my_funny_var_id,self._current_lang)  

   def MapCodedDimensions(self, out_model:PXFileModel):
      if self._pxmetadata_model.dataset.coded_dimensions:
        for my_var in self._pxmetadata_model.dataset.coded_dimensions: 
          my_funny_var_id = my_var.label[self._current_lang]
          self._stub.append(my_funny_var_id)
          my_var_code = my_var.code if my_var.code is not None else my_var.column_name
          out_model.variablecode.set(my_var_code, my_funny_var_id ,self._current_lang)
          my_codes:PxCodes = self._resolved_pxcodes_ids[my_var.codelist_id]

          out_codes=[]
          out_values =[]
          #todo  sortert liste
          for code in my_codes.valueitems:
             out_codes.append(code.code)
             out_values.append(code.label[self._current_lang])

          out_model.values.set(out_values,my_funny_var_id,self._current_lang)   
          out_model.codes.set(out_codes,my_funny_var_id,self._current_lang) 
          if my_var.is_geo_variable_type:
             out_model.variable_type.set("G", my_funny_var_id,self._current_lang) 
          else:
             out_model.variable_type.set("N", my_funny_var_id,self._current_lang) 

          out_model.prestext.set( self.LabelConstructionOptionDict[str(my_var.label_construction_option)], my_funny_var_id,self._current_lang) 

   def MapMeasurements(self, out_model:PXFileModel):
      if not self._pxmetadata_model.dataset.measurements:
         raise Exception("Sorry, dataset is missing measurment.")
      
      my_funny_var_id = self._config.contvariable[self._current_lang]
         
      out_codes=[]
      out_values =[]
      for my_cont in self._pxmetadata_model.dataset.measurements: 
         my_funny_cont_id = my_cont.label[self._current_lang]
         my_cont_code = my_cont.code if my_cont.code is not None else my_cont.column_name
         out_codes.append(my_cont_code)
         out_values.append(my_cont.label[self._current_lang])
         out_model.seasadj.set(my_cont.is_seasonally_adjusted or False,  my_funny_cont_id,self._current_lang)
         out_model.dayadj.set(my_cont.is_workingdays_adjusted or False,  my_funny_cont_id,self._current_lang)
         out_model.units.set(my_cont.unit_of_measure[self._current_lang], my_funny_cont_id,self._current_lang)
         out_model.contact.set(self._contact_string, my_funny_cont_id,self._current_lang) 
         out_model.last_updated.set(self._last_updated, my_funny_cont_id,self._current_lang) 

         if my_cont.reference_period[self._current_lang]:
            out_model.refperiod.set(my_cont.reference_period[self._current_lang], my_funny_cont_id,self._current_lang)

         if my_cont.show_decimals > 0 :
            out_model.precision.set(my_cont.show_decimals, my_funny_var_id,  my_funny_cont_id,self._current_lang)

         #optional with no default
         if my_cont.price_type:
            #todo str(my_cont.price_type) should yield C or F
            out_model.cfprices.set(str(my_cont.price_type),  my_funny_cont_id,self._current_lang)

      out_model.values.set(out_values, my_funny_var_id, self._current_lang)
      out_model.codes.set(out_codes, my_funny_var_id,self._current_lang)
      out_model.variablecode.set(self._config.contvariable_code, my_funny_var_id, self._current_lang) 
      out_model.variable_type.set("C", my_funny_var_id, self._current_lang) 

   def MapDecimals(self, out_model:PXFileModel):
      show_decimals_values = [instance.show_decimals for instance in self._pxmetadata_model.dataset.measurements]

      if self._pxmetadata_model.dataset.stored_decimals:
         out_model.decimals.set( max(self._pxmetadata_model.dataset.stored_decimals,max(show_decimals_values)) )
      else: 
         out_model.decimals.set(max(show_decimals_values))

      out_model.showdecimals.set(min(show_decimals_values)) 

   def GetContactString(self, in_model:PxStatistics) -> str:
       contact_string = ""

       if(in_model.contacts is None):
         return contact_string
       
       for contact in in_model.contacts:
          if(contact.name is None):
            return contact_string
          contact_string += f"{contact.name[self._current_lang]}#{contact.phone}#{contact.email}##"

       return contact_string[:-2]
   
   def GetLastUpdated(self, in_model:PxStatistics) -> str:
      last_updated_date = ""
      if in_model.upcoming_releases is None:
         return last_updated_date
      
      last_updated_date = in_model.upcoming_releases[0]
 
      formatted_string = ConvertToPxdateString(last_updated_date, f"%Y-%m-%d %H:%M:%S.%f")

      return formatted_string

   def AddPxStatisticsToPXFileModel(self, in_model:PxStatistics , out_model:PXFileModel):
      lang=self._current_lang
      out_model.subject_area.set("Todo: get from PxStatistics",lang)
      out_model.subject_code.set("Todo: get from PxStatistics")

      #out_model.update_frequency.set() Hmm ikke lang dep i pdf
    #  out_model.tableid.set(in_model.dataset.table_id)
    #  out_model.contents.set(in_model.dataset.base_title[lang],lang)

   def  AddPxMetadataToPXFileModel(self, in_model:PxMetadata , out_model:PXFileModel):
      lang=self._current_lang
      out_model.tableid.set(in_model.dataset.table_id)
      out_model.matrix.set("tab_"+in_model.dataset.table_id)
      out_model.contents.set( in_model.dataset.table_id + ":" + in_model.dataset.base_title[lang]+",",lang)


   def MapPxtoolconfigToPXFileModel(self, in_config:Pxtoolconfig , out_model:PXFileModel):

       out_model.axis_version.set(str(in_config.axis_version))
       out_model.charset.set(str(in_config.charset))
       out_model.codepage.set(str(in_config.code_page))

       out_model.descriptiondefault.set((in_config.description_default or False))
       out_model.contvariable.set(str(in_config.contvariable[self._current_lang] ))
       out_model.datasymbol1.set(str(in_config.datasymbol1))
       out_model.datasymbol2.set(str(in_config.datasymbol2))
       out_model.datasymbol3.set(str(in_config.datasymbol3))
       out_model.datasymbol4.set(str(in_config.datasymbol4))
       out_model.datasymbol5.set(str(in_config.datasymbol5))
       out_model.datasymbol6.set(str(in_config.datasymbol6))
       out_model.datasymbolnil.set(str(in_config.datasymbol_nil))
       out_model.datasymbolsum.set(str(in_config.datasymbol_sum))
       #out_model.source.set("en") = ...

        
def ConvertToPxdateString(date_string:str, date_format:str) -> str:
   dtm_date = datetime.strptime(date_string, date_format)
   px_date_string = dtm_date.strftime(f"%Y%m%d %H:%M")
   
   return px_date_string