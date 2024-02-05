# PxbuildConfig

 Description: Config object

 - admin(*) ND

    Description: These properties does not enter the pxfile directly

     - pxMetadataResource(*) ND

        Description: What resource provides the pxmetdata-json

         - resourceType type: string default: file

            Description: This defaults to file. Which currently is the only working value.

         - adressFormat(*) type: string

            Description: The path or url to the json, given its id ( id is the first argument to LoadFromPxmetadata). Example: example_data/pxmetadata/{id}.json

     - pxStatisticsResource(*) ND

        Description: What resource provides the pxstatistics-json

         - resourceType type: string default: file

         - adressFormat(*) type: string

            Description: The path or url to the json, given its id (id is taken from pxmetadata/dataset/statisticsId.) Example: example_data/pxstatistics/pxstatistics_{id}.json

     - pxCodesResource(*) ND

        Description: What resource provides the pxcodes-json

         - resourceType type: string default: file

         - adressFormat(*) type: string

            Description: The path or url to the json, given its id. Example: example_data/pxcodes/{id}.json

     - pxDataResource(*) ND

        Description: What resource provides the datadata

         - resourceType type: string default: file

         - adressFormat(*) type: string

            Description: The path or url to the json, given its id. Example: example_data/parquet_files/{id}

     - outputDestination(*) ND

        Description: Where to send the output

         - resourceType type: string default: folders

         - pxFolderFormat type: string

            Description: Aplies to resourcetype=folders. The folder where the .px-files are written. id is the tableID. Example: example_data/pxbuild_output/{id}

         - aggFolderFormat type: string

            Description: Aplies to resourcetype=folders. The folder where the .vs- and .agg-files are written. id is the tableID. Example: example_data/pxbuild_output/id}

     - validLanguages(*) type: array

        Description: The 2-letter languagecodes. Probably ISO 639, but the real constraint is that it has to match your pxweb

         - items type: string

     - buildMultilingualFiles type: boolean default: True

        Description: make multilingual PX-files, not one for each language. If true, the first entry in validLanguages will be used for language keyword.

     - skipCreationDate type: boolean default: False

        Description: should the CREATION-DATE keyword be skipped. Usefull (only) for pytests that compare PX-files.

     - theWordAnd(*) ND

     - theWordBy(*) ND

 - charset type: string

    Description: example: ANSI

 - axisVersion type: string

    Description: Version of px-file format.  example: '2013'

 - codePage type: string default: iso-8859-1

    Description: example: iso-8859-1

 - descriptionDefault type: boolean default: False

 - contvariable ND

    Description: Name for content variable

 - contvariableCode type: string default: ContentCode

    Description: Code for content variable

 - timevariableCode type: string default: Time

    Description: Code for the time variable

 - datasymbol1 ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol2 ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol3 ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol4 ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol5 ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol6 ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbolNil ND

    Description: How stored - are shown on screen

 - datasymbolSum ND

    Description: This if used to indicate how a sum of differing numbers of dots will be shown. The sum is stored as “…….”.

 - source ND

    Description: The source for the cubes, shown inside the About table part of PxWeb. Example: Statistics Norway

