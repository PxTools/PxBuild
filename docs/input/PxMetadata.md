# PxMetadata

    Description: Outer class

 - dataset(*) ND ND

    Description: Payload

     - tableId(*) type: string ND

        Description: example: '07459' To be used as id in PxWeb Url

     - storedDecimals type: integer ND

        Description: How many decimals should be stored in the PxFile. Default is the max number of decimals shown.

     - statisticsId type: string ND

        Description: Id of group of tables in the registry of statistics. example: '8765'

     - dataFile type: string ND

        Description: TODO: Er dette en filsti eller en url. required? Adress to the parquet-file with datadata

     - baseTitle(*) ND ND

        Description: Text to which tableid is prefixed and _by_ variable list is appended. Is used for the CONTENTS keyword. example: no Utenrikshandel med varer

     - searchKeywords ND ND

        Description: Array of keywords by language for search. Is used for the SYNONYMS keyword. example:'{en: [External trade, export]}'

     - notes ND ND

        ND

        is a [Notes](#notes)
     - cellNotes type: array ND

        ND

     - timeDimension(*) ND ND

        ND

         - columnName type: string ND

            Description: name of column in dataset

         - timePeriodFormat type: string ND

            Description: example: yyyy

         - label ND ND

            ND

            is a [StringByLanguage](#stringbylanguage)
     - codedDimensions type: array ND

        Description: Also known as classification variables

     - measurements(*) type: array ND

        Description: Also known as content variables

     - metaId type: array ND

        Description: For MetaId keyword

     - rowMissing type: string default: .

        Description: Value to insert in data when row is missing.

     - cellMissing type: string default: .

        Description: Value to insert in data when cell is missing.

     - officialStatistics type: boolean default: False

        ND

     - copyright type: boolean default: False

        ND

     - firstPublished type: string ND

        Description: The date when the data cube was first published in the format CCYYMMDD hh:mm

     - attributes type: array ND

        ND

# CodedDimension

    ND

 - columnName(*) type: string ND

    Description: name of column in dataset

 - code type: string ND

    Description: the code of the dimention( aka variable). Defaults to columName if missing

 - isGeoVariableType type: boolean default: False

    Description: Geo variable or not

 - codelistId(*) type: string ND

    Description: A Link to a PxCodes document

 - labelConstructionOption type: string default: text

    Description: Construct label for codelist entry as text or code or text then code or code then text

 - label ND ND

    ND

    is a [StringByLanguage](#stringbylanguage)
 - doublecolumn type: boolean default: False

    Description: Applies only to some of the file-export formats. See DOUBLECOLUMN-keyword

 - notes ND ND

    ND

    is a [Notes](#notes)
 - metaId type: array ND

    Description: For MetaId keyword

# Measurement

    ND

 - columnName(*) type: string ND

    Description: name of column in dataset

 - code type: string ND

    Description: the code of the measurement. Defaults to columName if missing

 - label(*) ND ND

    ND

    is a [StringByLanguage](#stringbylanguage)
 - showDecimals(*) type: integer ND

    Description: number of decimal to use in output

 - priceType type: string ND

    Description: Empty if not a price

 - isSeasonallyAdjusted type: boolean default: False

    ND

 - isWorkingdaysAdjusted type: boolean default: False

    ND

 - aggregationAllowed(*) type: boolean ND

    Description: Is it meaningfull to sum this measurement

 - basePeriod ND ND

    Description: For index example: '1. kvartal 2010'

 - referencePeriod ND ND

    Description: Text with information on the reference period for the statistics.

 - rank ND ND

    Description: Sort order for measurement in dimension, document order is default

 - unitOfMeasure(*) ND ND

    Description: Text including unit multiplier

 - notes ND ND

    ND

    is a [Notes](#notes)
 - metaId type: array ND

    Description: For MetaId keyword

# CellNote

    Description: Still TODO

 - attachment(*) type: array ND

    Description: Attaches the text on a point/subcube of the cube. The array has one or zero entries for each dimension. No entry for a dimension means everything.

 - text(*) ND ND

    ND

    is a [StringByLanguage](#stringbylanguage)
 - isMandatory(*) type: boolean ND

    ND

# Notes

    ND

# Note

    ND

 - text(*) ND ND

    ND

    is a [StringByLanguage](#stringbylanguage)
 - isMandatory(*) type: boolean ND

    ND

# StringByLanguage

    ND

