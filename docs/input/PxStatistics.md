# PxStatistics

 Description: Holds information of a publishing system nature, or registry of statistics if you like. The asumption behind subjectCode and subjectText is that your tables may be put in a menu tree. Subject is the first level in that tree.

 - id(*) type: string

    Description: Id of a group of tables in the registry of statistics. example: 8765

 - updateFrequency ND

    Description: Not in use. Must mean the same in all languages. example: Quarterly

 - metaId type: array

    Description: Will be added to METAID on table level. 'KORTNAVN:kpi' lead to https://www.ssb.no/en/priser-og-prisindekser/konsumpriser/statistikk/konsumprisindeksen#om-statistikken

     - items type: string

 - subjectCode(*) type: string

    Description: example: be

 - subjectText(*) ND

    Description: example en:Population

 - upcomingReleases type: array

    Description: List of dates. The first will be used for LAST-UPDATE, the next will be used for NEXT-UPDATE. example format: 2024-02-05 08:00:00.0 (to do)

     - items type: string

 - contacts(*) type: array

    Description: Will be used for CONTACT

     - items ND

         - phone type: string

         - email type: string

            Description: Personal or functional

         - name ND

            Description: Name of contact in all languages. Personal or functional

         - raw ND

            Description: If this has value it replaces the 3 other fields, so they are ignored. Anything, will be put under contact as is.
