from pxtool.model.keywords._charset import _Charset
from pxtool.model.keywords._axis_version import _AxisVersion
from pxtool.model.keywords._codepage import _Codepage
from pxtool.model.keywords._language import _Language
from pxtool.model.keywords._languages import _Languages
from pxtool.model.keywords._creation_date import _CreationDate
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

class PXFileModel:
    """
    This class holds the information of a PxFile
    the setters have all value has first param, and stuff from the keyword-part after, because some of them are optional.
    """

    def __init__(self) -> None:
        self.charset = _Charset("CHARSET")
        self.axis_version = _AxisVersion("AXIS-VERSION")
        self.codepage = _Codepage("CODEPAGE")
        self.language = _Language("LANGUAGE")
        self.languages = _Languages("LANGUAGES")
        self.creation_date = _CreationDate("CREATION-DATE")
        self.next_update = _NextUpdate("NEXT-UPDATE")
        self.px_server = _PxServer("PX-SERVER")
        self.directory_path = _DirectoryPath("DIRECTORY-PATH")
        self.update_frequency = _UpdateFrequency("UPDATE-FREQUENCY")
        self.tableid = _Tableid("TABLEID")
        self.synonyms = _Synonyms("SYNONYMS")
        self.default_graph = _DefaultGraph("DEFAULT-GRAPH")
        self.decimals = _Decimals("DECIMALS")
        self.showdecimals = _Showdecimals("SHOWDECIMALS")
        self.rounding = _Rounding("ROUNDING")
        self.matrix = _Matrix("MATRIX")
        self.aggregallowed = _Aggregallowed("AGGREGALLOWED")
        self.autopen = _Autopen("AUTOPEN")
        self.subject_code = _SubjectCode("SUBJECT-CODE")
        self.subject_area = _SubjectArea("SUBJECT-AREA")
        self.confidential = _Confidential("CONFIDENTIAL")
        self.copyright = _Copyright("COPYRIGHT")
        self.description = _Description("DESCRIPTION")
        self.title = _Title("TITLE")
        self.descriptiondefault = _Descriptiondefault("DESCRIPTIONDEFAULT")
        self.contvariable = _Contvariable("CONTVARIABLE")
        self.contents = _Contents("CONTENTS")
        self.units = _Units("UNITS")
        self.stub = _Stub("STUB")
        self.heading = _Heading("HEADING")
        self.values = _Values("VALUES")
        self.timeval = _Timeval("TIMEVAL")
        self.codes = _Codes("CODES")
        self.doublecolumn = _Doublecolumn("DOUBLECOLUMN")
        self.prestext = _Prestext("PRESTEXT")
        self.domain = _Domain("DOMAIN")
        self.variable_type = _VariableType("VARIABLE-TYPE")
        self.hierarchies = _Hierarchies("HIERARCHIES")
        self.hierarchylevels = _Hierarchylevels("HIERARCHYLEVELS")
        self.hierarchylevelsopen = _Hierarchylevelsopen("HIERARCHYLEVELSOPEN")
        self.hierarchynames = _Hierarchynames("HIERARCHYNAMES")
        self.map = _Map("MAP")
        self.partitioned = _Partitioned("PARTITIONED")
        self.elimination = _Elimination("ELIMINATION")
        self.precision = _Precision("PRECISION")
        self.last_updated = _LastUpdated("LAST-UPDATED")
        self.stockfa = _Stockfa("STOCKFA")
        self.cfprices = _Cfprices("CFPRICES")
        self.dayadj = _Dayadj("DAYADJ")
        self.seasadj = _Seasadj("SEASADJ")
        self.contact = _Contact("CONTACT")
        self.refperiod = _Refperiod("REFPERIOD")
        self.baseperiod = _Baseperiod("BASEPERIOD")
        self.database = _Database("DATABASE")
        self.source = _Source("SOURCE")
        self.official_statistics = _OfficialStatistics("OFFICIAL-STATISTICS")
        self.survey = _Survey("SURVEY")
        self.link = _Link("LINK")
        self.infofile = _Infofile("INFOFILE")
        self.info = _Info("INFO")
        self.notex = _Notex("NOTEX")
        self.note = _Note("NOTE")
        self.valuenotex = _Valuenotex("VALUENOTEX")
        self.valuenote = _Valuenote("VALUENOTE")
        self.datanote = _Datanote("DATANOTE")
        self.cellnotex = _Cellnotex("CELLNOTEX")
        self.cellnote = _Cellnote("CELLNOTE")
        self.datasymbol1 = _Datasymbol1("DATASYMBOL1")
        self.datasymbol2 = _Datasymbol2("DATASYMBOL2")
        self.datasymbol3 = _Datasymbol3("DATASYMBOL3")
        self.datasymbol4 = _Datasymbol4("DATASYMBOL4")
        self.datasymbol5 = _Datasymbol5("DATASYMBOL5")
        self.datasymbol6 = _Datasymbol6("DATASYMBOL6")
        self.datasymbolnil = _Datasymbolnil("DATASYMBOLNIL")
        self.datasymbolsum = _Datasymbolsum("DATASYMBOLSUM")
        self.datanotecell = _Datanotecell("DATANOTECELL")
        self.datanotesum = _Datanotesum("DATANOTESUM")
        self.keys = _Keys("KEYS")
        self.attribute_id = _AttributeId("ATTRIBUTE-ID")
        self.attribute_text = _AttributeText("ATTRIBUTE-TEXT")
        self.attributes = _Attributes("ATTRIBUTES")
        self.variablecode = _Variablecode("VARIABLECODE")
        self.meta_id = _MetaId("META-ID")
        self.data = _Data("DATA")

    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)
