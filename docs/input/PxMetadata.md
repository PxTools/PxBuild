# PxMetadata

 Description: Outer class

 - dataset(*) ND

    Description: Payload

     - tableId(*) type: string

        Description: example: '07459' To be used as id in PxWeb Url

     - storedDecimals type: integer

        Description: How many decimals should be stored in the PxFile. Default is the max number of decimals shown.

     - statisticsId type: string

        Description: Id of group of tables in the registry of statistics. example: '8765'

     - dataFile type: string

        Description: TODO: Er dette en filsti eller en url. required? Adress to the parquet-file with datadata

     - baseTitle(*) ND

        Description: Text to which tableid is prefixed and _by_ variable list is appended. Is used for the CONTENTS keyword. example: no Utenrikshandel med varer

     - searchKeywords ND

        Description: Array of keywords by language for search. Is used for the SYNONYMS keyword. example:'{en: [External trade, export]}'

     - notes type:  [Notes](#notes)

     - cellNotes type: array

         - items type:  [CellNote](#cellnote)

     - timeDimension(*) ND

         - columnName type: string

            Description: name of column in dataset

         - timePeriodFormat type: string

            Description: example: yyyy

         - label type:  [StringByLanguage](#stringbylanguage)

     - codedDimensions type: array

        Description: Also known as classification variables

         - items type:  [CodedDimension](#codeddimension)

     - measurements(*) type: array

        Description: Also known as content variables

         - items type:  [Measurement](#measurement)

     - metaId type: array

        Description: For MetaId keyword

         - items type: string

     - rowMissing type: string default: .

        Description: Value to insert in data when row is missing.

     - cellMissing type: string default: .

        Description: Value to insert in data when cell is missing.

     - officialStatistics type: boolean default: False

     - copyright type: boolean default: False

     - firstPublished type: string

        Description: The date when the data cube was first published in the format CCYYMMDD hh:mm

     - attributes type: array

         - items ND

             - columnName type: string

                Description: name of column in dataset

             - code type: string

                Description: the code of the measurement

             - codelistId type: string

                Description: A Link to a PxCodes document

# CodedDimension



 - columnName(*) type: string

    Description: name of column in dataset

 - code type: string

    Description: the code of the dimention( aka variable). Defaults to columName if missing

 - isGeoVariableType type: boolean default: False

    Description: Geo variable or not

 - codelistId(*) type: string

    Description: A Link to a PxCodes document

 - labelConstructionOption type: string default: text

    Description: Construct label for codelist entry as text or code or text then code or code then text

 - label type:  [StringByLanguage](#stringbylanguage)

 - doublecolumn type: boolean default: False

    Description: Applies only to some of the file-export formats. See DOUBLECOLUMN-keyword

 - notes type:  [Notes](#notes)

 - metaId type: array

    Description: For MetaId keyword

     - items type: string

# Measurement



 - columnName(*) type: string

    Description: name of column in dataset

 - code type: string

    Description: the code of the measurement. Defaults to columName if missing

 - label(*) type:  [StringByLanguage](#stringbylanguage)

 - showDecimals(*) type: integer

    Description: number of decimal to use in output

 - priceType type: string

    Description: Empty if not a price

 - isSeasonallyAdjusted type: boolean default: False

 - isWorkingdaysAdjusted type: boolean default: False

 - aggregationAllowed(*) type: boolean

    Description: Is it meaningfull to sum this measurement

 - basePeriod ND

    Description: For index example: '1. kvartal 2010'

 - referencePeriod ND

    Description: Text with information on the reference period for the statistics.

 - rank ND

    Description: Sort order for measurement in dimension, document order is default

 - unitOfMeasure(*) ND

    Description: Text including unit multiplier

 - notes type:  [Notes](#notes)

 - metaId type: array

    Description: For MetaId keyword

     - items type: string

# CellNote

 Description: Still TODO

 - attachment(*) type: array

    Description: Attaches the text on a point/subcube of the cube. The array has one or zero entries for each dimension. No entry for a dimension means everything.

     - items ND

         - dimensionCode(*) type: string

            Description: The code of the dimension (found in config for time and measure)

         - valueCode(*) type: string

            Description: The code of the Value

 - text(*) type:  [StringByLanguage](#stringbylanguage)

 - isMandatory(*) type: boolean

# Notes



 - items type:  [Note](#note)

# Note



 - text(*) type:  [StringByLanguage](#stringbylanguage)

 - isMandatory(*) type: boolean

# StringByLanguage



