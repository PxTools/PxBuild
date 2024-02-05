# PxbuildConfig

    Description: Config object

 - admin(*) ND ND

    Description: These properties does not enter the pxfile directly

     - pxMetadataResource(*) ND ND

        Description: What resource provides the pxmetdata-json

         - resourceType type: string default: file

            Description: This defaults to file. Which currently is the only working value.

         - adressFormat(*) type: string ND

            Description: The path or url to the json, given its id ( id is the first argument to LoadFromPxmetadata). Example: example_data/pxmetadata/{id}.json

     - pxStatisticsResource(*) ND ND

        Description: What resource provides the pxstatistics-json

         - resourceType type: string default: file

            ND

         - adressFormat(*) type: string ND

            Description: The path or url to the json, given its id (id is taken from pxmetadata/dataset/statisticsId.) Example: example_data/pxstatistics/pxstatistics_{id}.json

     - pxCodesResource(*) ND ND

        Description: What resource provides the pxcodes-json

         - resourceType type: string default: file

            ND

         - adressFormat(*) type: string ND

            Description: The path or url to the json, given its id. Example: example_data/pxcodes/{id}.json

     - pxDataResource(*) ND ND

        Description: What resource provides the datadata

         - resourceType type: string default: file

            ND

         - adressFormat(*) type: string ND

            Description: The path or url to the json, given its id. Example: example_data/parquet_files/{id}

     - outputDestination(*) ND ND

        Description: Where to send the output

         - resourceType type: string default: folders

            ND

         - pxFolderFormat type: string ND

            Description: Aplies to resourcetype=folders. The folder where the .px-files are written. id is the tableID. Example: example_data/pxbuild_output/{id}

         - aggFolderFormat type: string ND

            Description: Aplies to resourcetype=folders. The folder where the .vs- and .agg-files are written. id is the tableID. Example: example_data/pxbuild_output/id}

     - validLanguages(*) type: array ND

        Description: The 2-letter languagecodes. Probably ISO 639, but the real constraint is that it has to match your pxweb

     - buildMultilingualFiles type: boolean default: True

        Description: make multilingual PX-files, not one for each language. If true, the first entry in validLanguages will be used for language keyword.

     - skipCreationDate type: boolean default: False

        Description: should the CREATION-DATE keyword be skipped. Usefull (only) for pytests that compare PX-files.

     - theWordAnd(*) ND ND

        ND

     - theWordBy(*) ND ND

        ND

 - charset type: string ND

    Description: example: ANSI

 - axisVersion type: string ND

    Description: Version of px-file format.  example: '2013'

 - codePage type: string default: iso-8859-1

    Description: example: iso-8859-1

 - descriptionDefault type: boolean default: False

    ND

 - contvariable ND ND

    Description: Name for content variable

 - contvariableCode type: string default: ContentCode

    Description: Code for content variable

 - timevariableCode type: string default: Time

    Description: Code for the time variable

 - datasymbol1 ND ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol2 ND ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol3 ND ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol4 ND ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol5 ND ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbol6 ND ND

    Description: How 1-6 dots in data, are shown on screen

 - datasymbolNil ND ND

    Description: How stored - are shown on screen

 - datasymbolSum ND ND

    Description: This if used to indicate how a sum of differing numbers of dots will be shown. The sum is stored as “…….”.

 - source ND ND

    Description: The source for the cubes, shown inside the About table part of PxWeb. Example: Statistics Norway

