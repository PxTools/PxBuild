# PxStatistics

    Description: Holds information of a publishing system nature, or registry of statistics if you like. The asumption behind subjectCode and subjectText is that your tables may be put in a menu tree. Subject is the first level in that tree.

 - id(*) type: string ND

    Description: Id of a group of tables in the registry of statistics. example: 8765

 - updateFrequency ND ND

    Description: Must mean the same in all languages. example: Quarterly

 - metaId type: array ND

    Description: Will be added to metaid on table level. 'KORTNAVN:kpi' lead to https://www.ssb.no/en/priser-og-prisindekser/konsumpriser/statistikk/konsumprisindeksen#om-statistikken 

 - subjectCode(*) type: string ND

    Description: example: be

 - subjectText(*) ND ND

    Description: example en:Population

 - upcomingReleases type: array ND

    Description: example: 2024-02-05 08:00:00.0 TODO sjekk at dato i riktig format

 - contacts(*) type: array ND

    ND

