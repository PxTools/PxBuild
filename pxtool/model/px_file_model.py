from pxtool.model.keywords._charset import _Charset
from pxtool.model.keywords._axis_version import _AxisVersion
from pxtool.model.keywords._codepage import _Codepage
from pxtool.model.keywords._language import _Language
from pxtool.model.keywords._languages import _Languages
from pxtool.model.keywords._creation_date import _CreationDate
from pxtool.model.keywords._first_published import _FirstPublished
from pxtool.model.keywords._next_update import _NextUpdate
from pxtool.model.keywords._px_server import _PxServer
from pxtool.model.keywords._directory_path import _DirectoryPath
from pxtool.model.keywords._update_frequency import _UpdateFrequency
from pxtool.model.keywords._tableid import _Tableid
from pxtool.model.keywords._synonyms import _Synonyms
from pxtool.model.keywords._default_graph import _DefaultGraph
from pxtool.model.keywords._decimals import _Decimals
from pxtool.model.keywords._showdecimals import _Showdecimals
from pxtool.model.keywords._rounding import _Rounding
from pxtool.model.keywords._matrix import _Matrix
from pxtool.model.keywords._aggregallowed import _Aggregallowed
from pxtool.model.keywords._autopen import _Autopen
from pxtool.model.keywords._subject_code import _SubjectCode
from pxtool.model.keywords._subject_area import _SubjectArea
from pxtool.model.keywords._confidential import _Confidential
from pxtool.model.keywords._copyright import _Copyright
from pxtool.model.keywords._description import _Description
from pxtool.model.keywords._title import _Title
from pxtool.model.keywords._descriptiondefault import _Descriptiondefault
from pxtool.model.keywords._contvariable import _Contvariable
from pxtool.model.keywords._contents import _Contents
from pxtool.model.keywords._units import _Units
from pxtool.model.keywords._stub import _Stub
from pxtool.model.keywords._heading import _Heading
from pxtool.model.keywords._values import _Values
from pxtool.model.keywords._timeval import _Timeval
from pxtool.model.keywords._codes import _Codes
from pxtool.model.keywords._doublecolumn import _Doublecolumn
from pxtool.model.keywords._prestext import _Prestext
from pxtool.model.keywords._domain import _Domain
from pxtool.model.keywords._variable_type import _VariableType
from pxtool.model.keywords._hierarchies import _Hierarchies
from pxtool.model.keywords._hierarchylevels import _Hierarchylevels
from pxtool.model.keywords._hierarchylevelsopen import _Hierarchylevelsopen
from pxtool.model.keywords._hierarchynames import _Hierarchynames
from pxtool.model.keywords._map import _Map
from pxtool.model.keywords._partitioned import _Partitioned
from pxtool.model.keywords._elimination import _Elimination
from pxtool.model.keywords._precision import _Precision
from pxtool.model.keywords._last_updated import _LastUpdated
from pxtool.model.keywords._stockfa import _Stockfa
from pxtool.model.keywords._cfprices import _Cfprices
from pxtool.model.keywords._dayadj import _Dayadj
from pxtool.model.keywords._seasadj import _Seasadj
from pxtool.model.keywords._contact import _Contact
from pxtool.model.keywords._refperiod import _Refperiod
from pxtool.model.keywords._baseperiod import _Baseperiod
from pxtool.model.keywords._database import _Database
from pxtool.model.keywords._source import _Source
from pxtool.model.keywords._official_statistics import _OfficialStatistics
from pxtool.model.keywords._survey import _Survey
from pxtool.model.keywords._link import _Link
from pxtool.model.keywords._infofile import _Infofile
from pxtool.model.keywords._info import _Info
from pxtool.model.keywords._notex import _Notex
from pxtool.model.keywords._note import _Note
from pxtool.model.keywords._valuenotex import _Valuenotex
from pxtool.model.keywords._valuenote import _Valuenote
from pxtool.model.keywords._datanote import _Datanote
from pxtool.model.keywords._cellnotex import _Cellnotex
from pxtool.model.keywords._cellnote import _Cellnote
from pxtool.model.keywords._datasymbol1 import _Datasymbol1
from pxtool.model.keywords._datasymbol2 import _Datasymbol2
from pxtool.model.keywords._datasymbol3 import _Datasymbol3
from pxtool.model.keywords._datasymbol4 import _Datasymbol4
from pxtool.model.keywords._datasymbol5 import _Datasymbol5
from pxtool.model.keywords._datasymbol6 import _Datasymbol6
from pxtool.model.keywords._datasymbolnil import _Datasymbolnil
from pxtool.model.keywords._datasymbolsum import _Datasymbolsum
from pxtool.model.keywords._datanotecell import _Datanotecell
from pxtool.model.keywords._datanotesum import _Datanotesum
from pxtool.model.keywords._keys import _Keys
from pxtool.model.keywords._attribute_id import _AttributeId
from pxtool.model.keywords._attribute_text import _AttributeText
from pxtool.model.keywords._attributes import _Attributes
from pxtool.model.keywords._variablecode import _Variablecode
from pxtool.model.keywords._meta_id import _MetaId
from pxtool.model.keywords._data import _Data
from pxtool.model.util._px_super import _SuperKeyword

class PXFileModel:
    """
    This class holds the information of a PxFile
    the setters have all value has first param, and stuff from the keyword-part after, because some of them are optional.
    """

    def __init__(self) -> None:
        self.charset = _Charset("CHARSET")
        """Not in use"""
        self.axis_version = _AxisVersion("AXIS-VERSION")
        """Not in use. Version number for PC-Axis """
        self.codepage = _Codepage("CODEPAGE")
        """Not in use"""
        self.language = _Language("LANGUAGE")
        """Language-code with 2 letters,sv for Swedish, en for English etc. Default language"""
        self.languages = _Languages("LANGUAGES")
        """List of Language-codes used in file."""
        self.creation_date = _CreationDate("CREATION-DATE")
        """Date in 'Px Format'"""
        self.first_published = _FirstPublished("FIRST-PUBLISHED")
        """In use?"""
        self.next_update = _NextUpdate("NEXT-UPDATE")
        """Not in use. Date in 'Px  format'"""
        self.px_server = _PxServer("PX-SERVER")
        """Not in use"""
        self.directory_path = _DirectoryPath("DIRECTORY-PATH")
        """Not in use"""
        self.update_frequency = _UpdateFrequency("UPDATE-FREQUENCY")
        """Not in use"""
        self.tableid = _Tableid("TABLEID")
        """Id of table"""
        self.synonyms = _Synonyms("SYNONYMS")
        """In use?"""
        self.default_graph = _DefaultGraph("DEFAULT-GRAPH")
        """Not in use"""
        self.decimals = _Decimals("DECIMALS")
        """Number of desimals in stored data."""
        self.showdecimals = _Showdecimals("SHOWDECIMALS")
        """Number of desimals to display. May be overridden by Precision"""
        self.rounding = _Rounding("ROUNDING")
        """Not in normal use"""
        self.matrix = _Matrix("MATRIX")
        """The name of the matrix. Is suggested as file name when the file is fetched."""
        self.aggregallowed = _Aggregallowed("AGGREGALLOWED")
        """False if the contents of the table cannot be aggregated"""
        self.autopen = _Autopen("AUTOPEN")
        """Not is use."""
        self.subject_code = _SubjectCode("SUBJECT-CODE")
        """Subject area code. It is used to create files with tables available in PC-Axis. The text must not exceed 20 characters """
        self.subject_area = _SubjectArea("SUBJECT-AREA")
        """Text  for Subject area code"""
        self.confidential = _Confidential("CONFIDENTIAL")
        """Not in use.  """
        self.copyright = _Copyright("COPYRIGHT")
        """If true the copyright refers to the organization given in SOURCE"""
        self.description = _Description("DESCRIPTION")
        """Use title instead?"""
        self.title = _Title("TITLE")
        """The title of the table, reflecting its contents and variables"""
        self.descriptiondefault = _Descriptiondefault("DESCRIPTIONDEFAULT")
        """Not in normal use."""
        self.contvariable = _Contvariable("CONTVARIABLE")
        """which variable is the content variable"""
        self.contents = _Contents("CONTENTS")
        """Sort of a base title?"""
        self.units = _Units("UNITS")
        """Unit text, e.g. ton, NOK"""
        self.stub = _Stub("STUB")
        """Variables in stub"""
        self.heading = _Heading("HEADING")
        """Variables in heading"""
        self.values = _Values("VALUES")
        """Labels of the values for the variable."""
        self.timeval = _Timeval("TIMEVAL")
        """See pdf. TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”; """
        self.codes = _Codes("CODES")
        """Codes of the values for the variable."""
        self.doublecolumn = _Doublecolumn("DOUBLECOLUMN")
        """This keyword is used to get code and text in separate columns for the specified variable """
        self.prestext = _Prestext("PRESTEXT")
        """0 - Display only the value code. 1 - Display only the value text. 2 - Display first the code then the value text. 3 - Display first the value text then the value code."""
        self.domain = _Domain("DOMAIN")
        """Can occur once for each variable. Is used to determine which value sets are of interest, and thus which aggregation lists can be used. """
        self.variable_type = _VariableType("VARIABLE-TYPE")
        """Currently free-text. Suggestion: T for Time, G for Geo, C for Content """
        self.hierarchies = _Hierarchies("HIERARCHIES")
        """Not in normal use. See pdf"""
        self.hierarchylevels = _Hierarchylevels("HIERARCHYLEVELS")
        """Not in normal use. See pdf"""
        self.hierarchylevelsopen = _Hierarchylevelsopen("HIERARCHYLEVELSOPEN")
        """Not in normal use. See pdf"""
        self.hierarchynames = _Hierarchynames("HIERARCHYNAMES")
        """Not in normal use. See pdf"""
        self.map = _Map("MAP")
        """Used for a geographic variable for which maps can be made. Example: "Sweden_municipality"."""
        self.partitioned = _Partitioned("PARTITIONED")
        """string , int (,int) , see pdf"""
        self.elimination = _Elimination("ELIMINATION")
        """bool eller string"""
        self.precision = _Precision("PRECISION")
        """Determines that the value shall be presented with a number of decimals that differs from the keyword SHOWDECIMALS"""
        self.last_updated = _LastUpdated("LAST-UPDATED")
        """latest update  in pxdate format"""
        self.stockfa = _Stockfa("STOCKFA")
        """Indicates if data is stock, flow or average.  Used characters: S (stock), F (flow) and A (average) """
        self.cfprices = _Cfprices("CFPRICES")
        """Indicates if data is in current or fixed prices. C is used for Current and F for Fixed prices"""
        self.dayadj = _Dayadj("DAYADJ")
        """data is adjusted e.g. to take into account the number of working days"""
        self.seasadj = _Seasadj("SEASADJ")
        """Is  the data seasonally adjusted"""
        self.contact = _Contact("CONTACT")
        """Is written in the form name, organization, telephone, fax, e-mail. Several persons can be stated in the same text string and are then divided by the #-sign"""
        self.refperiod = _Refperiod("REFPERIOD")
        """Text with information on the exact period for the statistics."""
        self.baseperiod = _Baseperiod("BASEPERIOD")
        """Base period for, for instance index series"""
        self.database = _Database("DATABASE")
        """The name of the database from where the statistics is retrieved"""
        self.source = _Source("SOURCE")
        """States the organization which is responsible for the statistics"""
        self.official_statistics = _OfficialStatistics("OFFICIAL-STATISTICS")
        """Indicates if the data table is included in the official statistics of the organization."""
        self.survey = _Survey("SURVEY")
        """Hmm, try, pdf says: Is shown on information screen in PX-web if installation parameter true."""
        self.link = _Link("LINK")
        """Not in use?"""
        self.infofile = _Infofile("INFOFILE")
        """Name of a file containing more information for the statistics. Working?"""
        self.info = _Info("INFO")
        """Not in use"""
        self.notex = _Notex("NOTEX")
        """Mandatory footnote for variable or table if no variable is given"""
        self.note = _Note("NOTE")
        """non-mandatory footnote for variable or table if no variable is given"""
        self.valuenotex = _Valuenotex("VALUENOTEX")
        """Mandatory footnote for value in variable"""
        self.valuenote = _Valuenote("VALUENOTE")
        """Non-mandatory footnote for value in variable"""
        self.datanote = _Datanote("DATANOTE")
        """"""
        self.cellnotex = _Cellnotex("CELLNOTEX")
        """As CELLNOTE but shown mandatory as for NOTEX."""
        self.cellnote = _Cellnote("CELLNOTE")
        """Footnote for a single cell or a group of cells. Which cell it refers to is given by values and variables. If a value is given as * the note refers to all values for that variable. Only one value can be given for each variable. T"""
        self.datasymbol1 = _Datasymbol1("DATASYMBOL1")
        """Should be in config?"""
        self.datasymbol2 = _Datasymbol2("DATASYMBOL2")
        """Should be in config?"""
        self.datasymbol3 = _Datasymbol3("DATASYMBOL3")
        """Should be in config?"""
        self.datasymbol4 = _Datasymbol4("DATASYMBOL4")
        """Should be in config?"""
        self.datasymbol5 = _Datasymbol5("DATASYMBOL5")
        """Should be in config?"""
        self.datasymbol6 = _Datasymbol6("DATASYMBOL6")
        """Should be in config?"""
        self.datasymbolnil = _Datasymbolnil("DATASYMBOLNIL")
        """"""
        self.datasymbolsum = _Datasymbolsum("DATASYMBOLSUM")
        """"""
        self.datanotecell = _Datanotecell("DATANOTECELL")
        """"""
        self.datanotesum = _Datanotesum("DATANOTESUM")
        """"""
        self.keys = _Keys("KEYS")
        """"""
        self.attribute_id = _AttributeId("ATTRIBUTE-ID")
        """Not in normal use. See pdf"""
        self.attribute_text = _AttributeText("ATTRIBUTE-TEXT")
        """Not in normal use. See pdf"""
        self.attributes = _Attributes("ATTRIBUTES")
        """Not in normal use. See pdf"""
        self.variablecode = _Variablecode("VARIABLECODE")
        """"""
        self.meta_id = _MetaId("META-ID")
        """The META-ID keyword is used to reference a external meta information about a table, variable or value. Requires a separate file to resolve to urls"""
        self.unknown_keywords = ""
        self.data = _Data("DATA")
        """Numbers and quoted dots"""

    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)

    def get_attribute(self, name:str) -> _SuperKeyword:
        return getattr(self, name)
