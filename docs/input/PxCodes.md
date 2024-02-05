# PxCodes

    Description: For one variable, this should hold all the information needed for the VALUES and CODES px-keywords (aka the codelist), and to create any vs and agg files (aka the groupings) if such is desired. In addition this contains partial information on elimination.

 - id(*) type: string ND

    Description: Id of this document, example: 123234a

 - admin ND ND

    ND

     - isFinal type: boolean ND

        Description: todo. ignored for now

     - tags type: array ND

        ND

     - todoCreation type: string ND

        ND

 - sortValueitemsOn(*) ND ND

    Description: How the items in the codelist is sorted.

    is a [SortValueitemsOn](#sortvalueitemson)
 - label ND ND

    Description: Texts for 'the dropdown' where you select which grouping to use or return to this codelist

    is a [StringByLanguage](#stringbylanguage)
 - valueitems(*) type: array ND

    Description: These are the 'root-entries' describe what is in the data.

 - eliminationPossible(*) type: boolean ND

    Description: May this variable be eliminnated. If True and eliminationCode is empty use Sum.

 - eliminationCode type: string ND

    Description: example: 'tot'. Value of the code to use for eliminnating the variable. Must be from root-entries, not from a grouping.

 - sortGroupingsOn type: string ND

    Description: Sets the order of the groupings in the dropdown. (So only needed if you have groupings.

 - groupings type: array ND

    Description: List where an element is a grouping. A grouping is a list of mothers. The code of a mother must not be present in the root-valueitems. The children of a mother must be present in the root-valueitems and must be a unique list. The child may have many mothers.

# Valueitem

    ND

 - code type: string ND

    Description: Code of the item example: 123234a

 - unorderedChildren type: array ND

    Description: Any children in random order. The children MUST exist in root-valueitems and will be sorted as they are there.

 - label ND ND

    Description: Texts of the item example: en:Total, no: I alt

    is a [StringByLanguage](#stringbylanguage)
 - rank ND ND

    Description: Strings to sort by when code or label is not sufficient

    is a [StringByLanguage](#stringbylanguage)
 - notes ND ND

    Description: Any fotnotes

    is a [Notes](#notes)
# Notes

    ND

# Note

    ND

 - text(*) ND ND

    ND

    is a [StringByLanguage](#stringbylanguage)
 - isMandatory(*) type: boolean ND

    ND

# SortValueitemsOn

    ND

# StringByLanguage

    ND

