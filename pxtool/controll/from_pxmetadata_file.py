import json
from datetime import datetime
import time
import pandas as pd
import numpy as np
from typing import List, Dict

from pxtool.models.input.pydantic_pxmetadata import PxMetadata
from pxtool.models.input.pydantic_pxtoolconfig import Pxtoolconfig
from pxtool.models.input.pydantic_pxcodes import PxCodes
from pxtool.models.input.helper_pxcodes import HelperPxCodes
from pxtool.models.input.pydantic_pxstatistics import PxStatistics

from pxtool.models.output.pxfile.px_file_model import PXFileModel
from pxtool.models.output.agg_vs.vs_file_model import _VSFileModel

from .helpers.parquet_datasource import ParquetDatasource
from .helpers.for_get_data import ForGetData
from .helpers.data_formatter import DataFormatter

class LoadFromPxmetadata():
   LabelConstructionOptionDict={"LabelConstructionOption.code":0,"LabelConstructionOption.text":1, "LabelConstructionOption.code_text":2, "LabelConstructionOption.text_code":3}



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
        self._pxcodes_helper = {}
        pxcodesFormat="example_data/pxcodes/{id}.json"
        for myVar in self._pxmetadata_model.dataset.coded_dimensions:

          if not myVar.codelist_id in self._resolved_pxcodes_ids:
             tmpPath= pxcodesFormat.format(id=myVar.codelist_id)
             with open(tmpPath, encoding="utf-8-sig") as f:
                json1 = json.loads(f.read())
             self._resolved_pxcodes_ids[myVar.codelist_id] = PxCodes(**json1)
             self._pxcodes_helper[myVar.codelist_id] = HelperPxCodes(self._resolved_pxcodes_ids[myVar.codelist_id])

    

      data_file_path_format="example_data/parquet_files/output_file{id}.parquet"
      data_file_path=data_file_path_format.format(id=self._pxmetadata_model.dataset.data_file)

      #filePath='example_data/parquet_files/output_file03024.parquet' 
      self._parquet = ParquetDatasource(data_file_path)
      #self._parquet.PrintColumns()

      self._for_get_data_by_varid:Dict[str, ForGetData] = dict()
      
     

   
      ##################
      ## loop in languages

      self._current_lang="no" #todo
      self._contact_string = self.GetContactString(self._pxstatistics)
      self._last_updated = self.GetLastUpdated(self._pxstatistics) 
      self._stub=[]
      self._heading=[self._config.contvariable[self._current_lang] ]

      self._metaid_table:List[str]=[]
      self._metaid_valiable:dict={}
      

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


      self.AddMetaIds(out_model)
      

  #    self.GetData(out_model)
      
      temp_tabid= self._filename
      out_file= 'example_data/pxtool_output/output_'+temp_tabid+'/tab_'+temp_tabid+'.px'
      with open(out_file, 'w') as f:
             print(out_model, file=f)

      print("File written to:",out_file)
      
      #out_vs_model=_VSFileModel()
      #self.makeVsFile(out_vs_model)

      self.makeVsFile()      




          
   def CalculateFactor(self) -> int:
      variables_in_output_order = self.GetVariList()
      curr_factor = 1 
      for vari in reversed(variables_in_output_order):
         temp_for_get_data:ForGetData = self._for_get_data_by_varid[vari]
         temp_for_get_data.factor = curr_factor
         prevN = temp_for_get_data._length_of_codelist
         curr_factor = curr_factor*prevN 

      array_size = curr_factor

      return array_size
   


   def GetData(self, out_model:PXFileModel) -> None:
      
    #/// MINDEX:
    #/// We need to convert a point(one value for each variable) in 
    #/// the cube to a number(the index of the array).
    #///
    #/// k,j, i... 1-based counters
    #/// Nx number of values for x
    #/// Factor_k=Nj*Ni
    #/// Factor_j= Ni
    #/// Factor_i = 1
    #/// index = Factor_k*(k-1) + Factor_j*(j-1) + Factor_i(i-1) </remarks>
    #  in python things are zero-based but the idea is the same
    #/// </summary>
      start_GetData = time.time()

      matrix_size = self.CalculateFactor()

      init_value = self._pxmetadata_model.dataset.row_missing
      missing_cell_symbol = self._pxmetadata_model.dataset.cell_missing

    
      column_code_map = self.GetMeasurementColumnCodeMapping()

      start_tidy = time.time()
      df =  self._parquet.GetTidyDF(self._config.contvariable_code, column_code_map)
 
      end_tidy = time.time()
      time_used_tidy = end_tidy-start_tidy
      print('Time: GetTidyDF:', time_used_tidy)

      self.add_out_index(df)
      self.add_out_value(missing_cell_symbol, df)
      merged_df = self.add_missing_rows(matrix_size, init_value, df)

      out_data = merged_df['out_value'].tolist()

      merged_df = merged_df.sort_values(by=['out_index'])
      formatter = DataFormatter(self._heading, self._for_get_data_by_varid)
      number_of_columns_per_line = formatter.CalculateLineBreak()

      out_model.data.set(out_data, number_of_columns_per_line)

      end_GetData = time.time()
      time_used_GetData = end_GetData-start_GetData
      print('Time: GetData:', time_used_GetData)

   def add_missing_rows(self, matrix_size, init_value, df):
       matrix_df = pd.DataFrame({'out_index': range(matrix_size)})


      # Merge the two DataFrames
       merged_df = pd.merge(matrix_df, df, on='out_index', how='left')

      # Fill missing values with "MISSING"
       merged_df['out_value'].fillna(init_value, inplace=True)
       return merged_df

   def add_out_value(self, missing_cell_symbol, df):
       conditions = [df['VALUE'] != "", 
                    df['SYMBOL'] != ""
                    ]

       choices = [
         df['VALUE'].astype(str),
         df['SYMBOL'].astype(str)
      ]

       start = time.time()
       df['out_value'] = np.select(conditions, choices, missing_cell_symbol)
       end = time.time()
       time_used = end-start
       print('Time: numpy select in:', time_used)

   def add_out_index(self, df):
       columns_to_sum = []
       for col in self._for_get_data_by_varid.values():
         # Mapping the values using the dictionary 
          contribColName=  'int_'+col._colname_in_dataframe
          df[contribColName] = df[col._colname_in_dataframe].map(col._position_of_value) * col.factor
          columns_to_sum.append(contribColName)
       df['out_index'] = df[columns_to_sum].sum(axis=1)

   def AddMetaIds(self, out_model:PXFileModel) -> None:
     
     if self._metaid_table:
       out_model.meta_id.set( " ".join(self._metaid_table) )
     
     for vari in self._metaid_valiable:
        out_model.meta_id.set(" ".join(self._metaid_valiable[vari]),vari, None,self._current_lang)


   def GetVariList(self) -> List[str]:
      return self._stub + self._heading  

   def GetMeasurementColumnCodeMapping(self) -> dict:
      column_code_map = {}
      for measurement_var in self._pxmetadata_model.dataset.measurements:
         column_code_map[measurement_var.column_name] = measurement_var.code

      return column_code_map

   def MapAggregallowed(self, out_model:PXFileModel):
      # Check if all values in the array are True
      all_true = all(instance.aggregation_allowed for instance in self._pxmetadata_model.dataset.measurements)
      out_model.aggregallowed.set(all_true)

   def MapTitle(self, out_model:PXFileModel):
      lang = self._current_lang
      model = self._pxmetadata_model.dataset 

      vari_list = self.GetVariList()

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

      for_get_data = ForGetData(self._pxmetadata_model.dataset.time_dimension.column_name,  my_periods)
      self._for_get_data_by_varid[my_funny_var_id] = for_get_data 

   def MapCodedDimensions(self, out_model:PXFileModel):
      if self._pxmetadata_model.dataset.coded_dimensions:
        lang = self._current_lang
        for my_var in self._pxmetadata_model.dataset.coded_dimensions: 
          my_funny_var_id = my_var.label[lang]
          self._stub.append(my_funny_var_id)
          my_var_code = my_var.code if my_var.code is not None else my_var.column_name
          out_model.variablecode.set(my_var_code, my_funny_var_id, lang)
          my_codes:PxCodes = self._resolved_pxcodes_ids[my_var.codelist_id]

          my_pxcodes_helper = self._pxcodes_helper[my_var.codelist_id]

          temp_codes = my_pxcodes_helper.getCodes(lang)
          out_model.codes.set(temp_codes,my_funny_var_id, lang) 

          temp_values = my_pxcodes_helper.getLabels(lang)
          out_model.values.set(temp_values,my_funny_var_id, lang)   
          if my_codes.groupings:
             
             my_domain_id=MakeDomainId(my_var.codelist_id,self._current_lang)
             out_model.domain.set(my_domain_id,my_funny_var_id,self._current_lang)
          


          if my_var.is_geo_variable_type:
             out_model.variable_type.set("G", my_funny_var_id, lang) 
          else:
             out_model.variable_type.set("N", my_funny_var_id, lang) 

          out_model.prestext.set( self.LabelConstructionOptionDict[str(my_var.label_construction_option)], my_funny_var_id, lang) 
           
          if not my_pxcodes_helper.elimination_possible:
             out_model.elimination.set("NO", my_funny_var_id, lang)
          else:
             label = my_pxcodes_helper.getEliminationLabel( lang)
             if label:
               out_model.elimination.set(label, my_funny_var_id, lang)
             else:
                out_model.elimination.set("YES", my_funny_var_id, lang)
         
          if my_var.meta_id:
             if not my_funny_var_id in self._metaid_valiable:
                self._metaid_valiable[my_funny_var_id] = []

             self._metaid_valiable[my_funny_var_id] += my_var.meta_id

          #Note on variable
          if my_var.notes:
             for note in my_var.notes:
               if note.is_mandatory:
                  out_model.notex.set(note.text[lang], my_funny_var_id, lang)
               else:
                  out_model.note.set(note.text[lang], my_funny_var_id, lang)
          #Note on a value in variale
          my_value_notes = my_pxcodes_helper.getNotes(lang)
          if my_value_notes:
              for code in my_value_notes: 
                  for note in my_value_notes[code]:
                     if note.is_mandatory:
                        out_model.valuenotex.set(note.text[lang], my_funny_var_id, code, lang)
                     else:
                        out_model.valuenote.set(note.text[lang], my_funny_var_id, code, lang)

          for_get_data = ForGetData(my_var.column_name, my_pxcodes_helper.getCodes( lang))
          self._for_get_data_by_varid[my_funny_var_id] = for_get_data 


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

      for_get_data = ForGetData(self._config.contvariable_code, out_codes)
      self._for_get_data_by_varid[my_funny_var_id] = for_get_data 

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
      
      if len(in_model.upcoming_releases) < 1:
         return last_updated_date
      

      last_updated_date = in_model.upcoming_releases[0]
 
      formatted_string = ConvertToPxdateString(last_updated_date, f"%Y-%m-%d %H:%M:%S.%f")

      return formatted_string

   def AddPxStatisticsToPXFileModel(self, in_model:PxStatistics , out_model:PXFileModel):
      lang=self._current_lang
      
      out_model.subject_area.set(in_model.subject_text[lang],lang)
      out_model.subject_code.set(in_model.subject_code)

      
      self._metaid_table += in_model.meta_id
       

      #out_model.update_frequency.set() Hmm ikke lang dep i pdf


   def  AddPxMetadataToPXFileModel(self, in_model:PxMetadata , out_model:PXFileModel):
      lang=self._current_lang
      out_model.tableid.set(in_model.dataset.table_id)
      out_model.matrix.set("tab_"+in_model.dataset.table_id)
      out_model.contents.set( in_model.dataset.table_id + ": " + in_model.dataset.base_title[lang]+",",lang)
      


   def MapPxtoolconfigToPXFileModel(self, in_config:Pxtoolconfig , out_model:PXFileModel):

       out_model.axis_version.set(str(in_config.axis_version))
       out_model.charset.set(str(in_config.charset))
       out_model.codepage.set(str(in_config.code_page))

       out_model.descriptiondefault.set((in_config.description_default or False))
       out_model.contvariable.set(str(in_config.contvariable[self._current_lang] ))

       if in_config.datasymbol1 and in_config.datasymbol1[self._current_lang]:
         out_model.datasymbol1.set(str(in_config.datasymbol1[self._current_lang]),self._current_lang)
       if in_config.datasymbol2 and in_config.datasymbol2[self._current_lang]:
         out_model.datasymbol2.set(str(in_config.datasymbol2[self._current_lang]),self._current_lang)
       if in_config.datasymbol3 and in_config.datasymbol3[self._current_lang]:
         out_model.datasymbol3.set(str(in_config.datasymbol3[self._current_lang]),self._current_lang)
       if in_config.datasymbol4 and in_config.datasymbol4[self._current_lang]:
         out_model.datasymbol4.set(str(in_config.datasymbol4[self._current_lang]),self._current_lang)     
       if in_config.datasymbol5 and in_config.datasymbol5[self._current_lang]:
         out_model.datasymbol5.set(str(in_config.datasymbol5[self._current_lang]),self._current_lang)  
       if in_config.datasymbol6 and in_config.datasymbol6[self._current_lang]:
         out_model.datasymbol6.set(str(in_config.datasymbol6[self._current_lang]),self._current_lang)  
       if in_config.datasymbol_nil and in_config.datasymbol_nil[self._current_lang]:
         out_model.datasymbolnil.set(str(in_config.datasymbol_nil[self._current_lang]),self._current_lang)     
       if in_config.datasymbol_sum and in_config.datasymbol_sum[self._current_lang]:
         out_model.datasymbolsum.set(str(in_config.datasymbol_sum[self._current_lang]),self._current_lang)  


       out_model.source.set(in_config.source[self._current_lang],self._current_lang)  
   #def makeVsFile(self,out_vs_model:_VSFileModel):
   def makeVsFile(self):
          if self._pxmetadata_model.dataset.coded_dimensions:             
            for my_var in self._pxmetadata_model.dataset.coded_dimensions: 
               out_vs_model= _VSFileModel()
               my_var_code = my_var.code
               #out_model.variablecode.set(my_var_code, my_funny_var_id ,self._current_lang)
               my_codes:PxCodes = self._resolved_pxcodes_ids[my_var.codelist_id]
               if my_codes.groupings:
                  my_funny_var_id = my_var.label[self._current_lang]
                  vs_name= MakeDomainId(my_var.codelist_id,self._current_lang)
                  vs_type = "G" if my_var.is_geo_variable_type else "V"
                  out_vs_model.description.set("Name",vs_name)
                  out_vs_model.description.set("Type",vs_type)
                  # if my_codes.groupings:
                  group_conter=0
                  for groups in my_codes.groupings:
                     group_conter = group_conter +1
                     group_key = str(group_conter)
                     out_vs_model.aggreg.set(group_key,groups.filename_base + "_" + self._current_lang + ".agg")
                  my_domain =MakeDomainId(my_var.codelist_id,self._current_lang)  
                  out_vs_model.domain.set("1",my_domain) 
                  
                  my_sorted_value_items = self._pxcodes_helper[my_var.codelist_id] 
                  value_item_counter=0
                  for my_item in my_sorted_value_items._sorted_valueitems[self._current_lang]:
                     value_item_counter = value_item_counter+1
                     value_item_key = str(value_item_counter)
                     my_stripped_code=my_item.code.strip("'")
                     out_vs_model.valuecode.set(value_item_key,my_stripped_code)
                     my_stripped_text = my_item.label[self._current_lang].strip("'")
                     out_vs_model.valuetext.set(value_item_key,my_stripped_text)
                  out_file= 'example_data/pxtool_output/' + my_codes.id + "_" + self._current_lang + ".vs"
                  with open(out_file, 'w', encoding="utf-8") as f:
                     print(out_vs_model, file=f)
                     print("File written to:",out_file)               


      

        
def ConvertToPxdateString(date_string:str, date_format:str) -> str:
   dtm_date = datetime.strptime(date_string, date_format)
   px_date_string = dtm_date.strftime(f"%Y%m%d %H:%M")
   
   return px_date_string

def MakeDomainId(code_list_id:str, lang:str) -> str:
   domain_id = code_list_id + "_" + lang 
   return domain_id 