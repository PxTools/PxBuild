# disclaimer
This is WORK IN PROGRESS and is be no means ready for production.
# pxbuild
Purpose: Creating px-files (.px, .vs and .agg -files), which is one of the datasource-types for the awesome PxWeb ( see https://github.com/statisticssweden/PxWeb ) 

The basic idea: the information needed to be a table in PxWeb is split in 5 parts: 
- config, which is common to all tables for an organisation, e.g. organisation name
- zero or more codelists, for coded variables , often shared by other tables.  
- stuff like subject-area and possible dates of publication. CMS/publication-prosess type of info. The tables typically share these properties with their sibling tables.
- the rest of the metadata, table specific information, e.g. title
- the datadata, a parquet-file (or for testing csv) with the data and implisitt the codelist for time.    

Each part, except the datadata, has a json-schema, named: pxbuildconfig, pxcodes, pxstatistics and pxmetadata.

So, you supply data and the jsons and pxbuild generates the px-files.

```mermaid
flowchart TD
   subgraph M["pxmetadata.json (Startingpoint)"]
     M1["Stuff like title and decimals\n and also link to dataFile and Ids for the 'api' for shared info"]
   end 
   subgraph S["'api' for Pxstatistics-jsons"]
     PX_SR("Storage of Pxstatistics-json files,\n in a file folder\n or live call to backend")
   end
   subgraph C["'api' for Pxcodes-jsons"]
     D("Storage of Pxcodes-json files\n or live call to backend")
   end

   subgraph T["Pxbuild"]
     T1["Generate PXfiles"]
   end
   subgraph O["Output"]
     O1["px-files \n vs-files \n agg-files"]
   end
   M --> |starting with a pxmetadata-file| T
   S <--> | one of these| T
   C <--> T
   C <--> | one for each\n coded variable | T
   Config --> T
   Datafile --> T
   T --> O

``` 
## First usage
The px_client2.py inside the demo folder, is probably a good starting point

## Developer notes

### Requirements
* Python 3.11
* [Poetry](https://python-poetry.org/)


### Install and test
```
poetry env use 3.11
poetry install
poetry run pytest
```