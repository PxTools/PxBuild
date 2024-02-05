# PxCodes

 Description: For one variable, this should hold all the information needed for the VALUES and CODES px-keywords (aka the codelist), and to create any vs and agg files (aka the groupings) if such is desired. In addition this contains partial information on elimination.

 - id(*) type: string

    Description: Id of this document, example: 123234a

 - admin ND

    Description: To do, not is use yet.

     - isFinal type: boolean

        Description: todo. ignored for now

     - tags type: array

         - items type: string

     - todoCreation type: string

 - sortValueitemsOn(*) type:  [SortValueitemsOn](#sortvalueitemson)

    Description: How the items in the codelist is sorted.

 - label type:  [StringByLanguage](#stringbylanguage)

    Description: Texts for 'the dropdown' where you select which grouping to use or return to this codelist

 - valueitems(*) type: array

    Description: These are the 'root-entries' describe what is in the data.

     - items type:  [Valueitem](#valueitem)

        Description: Denne er en sibbling av ref.

 - eliminationPossible(*) type: boolean

    Description: May this variable be eliminnated. If True and eliminationCode is empty use Sum.

 - eliminationCode type: string

    Description: example: 'tot'. Value of the code to use for eliminnating the variable. Must be from root-entries, not from a grouping.

 - sortGroupingsOn type: string

    Description: Sets the order of the groupings in the dropdown. (So only needed if you have groupings.

 - groupings type: array

    Description: List where an element is a grouping. A grouping is a list of mothers. The code of a mother must not be present in the root-valueitems. The children of a mother must be present in the root-valueitems and must be a unique list. The child may have many mothers.

     - items ND

         - filenameBase type: string

            Description: To this filenameBase the language and filetype will be added.

         - label type:  [StringByLanguage](#stringbylanguage)

            Description: Texts for 'the dropdown' where you select which grouping to use

         - rank type:  [StringByLanguage](#stringbylanguage)

            Description: Strings to sort by when code or label is not sufficient

         - sortValueitemsOn type:  [SortValueitemsOn](#sortvalueitemson)

            Description: How to sort the list of mothers. The children will be sorted by the root-sortValueitemsOn

         - valueitems type: array

            Description: The list of mothers.

             - items type:  [Valueitem](#valueitem)

# Valueitem



 - code type: string

    Description: Code of the item example: 123234a

 - unorderedChildren type: array

    Description: Any children in random order. The children MUST exist in root-valueitems and will be sorted as they are there.

     - items type: string

 - label type:  [StringByLanguage](#stringbylanguage)

    Description: Texts of the item example: en:Total, no: I alt

 - rank type:  [StringByLanguage](#stringbylanguage)

    Description: Strings to sort by when code or label is not sufficient

 - notes type:  [Notes](#notes)

    Description: Any fotnotes

# Notes



 - items type:  [Note](#note)

# Note



 - text(*) type:  [StringByLanguage](#stringbylanguage)

 - isMandatory(*) type: boolean

# SortValueitemsOn



# StringByLanguage



