from pxtool.model.keywords._charset import Charset
from pxtool.model.keywords._axis_version import AxisVersion
from pxtool.model.keywords._codepage import Codepage
from pxtool.model.keywords._language import Language
from pxtool.model.keywords._languages import Languages
from pxtool.model.keywords._creation_date import CreationDate
from pxtool.model.keywords._next_update import NextUpdate
from pxtool.model.keywords._px_server import PxServer
from pxtool.model.keywords._directory_path import DirectoryPath
from pxtool.model.keywords._update_frequency import UpdateFrequency
from pxtool.model.keywords._tableid import Tableid
from pxtool.model.keywords._synonyms import Synonyms
from pxtool.model.keywords._default_graph import DefaultGraph
from pxtool.model.keywords._decimals import Decimals
from pxtool.model.keywords._showdecimals import Showdecimals
from pxtool.model.keywords._rounding import Rounding
from pxtool.model.keywords._matrix import Matrix
from pxtool.model.keywords._aggregallowed import Aggregallowed
from pxtool.model.keywords._autopen import Autopen
from pxtool.model.keywords._subject_code import SubjectCode
from pxtool.model.keywords._subject_area import SubjectArea
from pxtool.model.keywords._confidential import Confidential
from pxtool.model.keywords._copyright import Copyright
from pxtool.model.keywords._description import Description
from pxtool.model.keywords._title import Title
from pxtool.model.keywords._descriptiondefault import Descriptiondefault
from pxtool.model.keywords._contvariable import Contvariable
from pxtool.model.keywords._contents import Contents
from pxtool.model.keywords._units import Units
from pxtool.model.keywords._stub import Stub
from pxtool.model.keywords._heading import Heading
from pxtool.model.keywords._values import Values
from pxtool.model.keywords._timeval import Timeval
from pxtool.model.keywords._codes import Codes
from pxtool.model.keywords._doublecolumn import Doublecolumn
from pxtool.model.keywords._prestext import Prestext
from pxtool.model.keywords._domain import Domain
from pxtool.model.keywords._variable_type import VariableType
from pxtool.model.keywords._hierarchies import Hierarchies
from pxtool.model.keywords._hierarchylevels import Hierarchylevels
from pxtool.model.keywords._hierarchylevelsopen import Hierarchylevelsopen
from pxtool.model.keywords._hierarchynames import Hierarchynames
from pxtool.model.keywords._map import Map
from pxtool.model.keywords._partitioned import Partitioned
from pxtool.model.keywords._elimination import Elimination
from pxtool.model.keywords._precision import Precision
from pxtool.model.keywords._last_updated import LastUpdated
from pxtool.model.keywords._stockfa import Stockfa
from pxtool.model.keywords._cfprices import Cfprices
from pxtool.model.keywords._dayadj import Dayadj
from pxtool.model.keywords._seasadj import Seasadj
from pxtool.model.keywords._contact import Contact
from pxtool.model.keywords._refperiod import Refperiod
from pxtool.model.keywords._baseperiod import Baseperiod
from pxtool.model.keywords._database import Database
from pxtool.model.keywords._source import Source
from pxtool.model.keywords._official_statistics import OfficialStatistics
from pxtool.model.keywords._survey import Survey
from pxtool.model.keywords._link import Link
from pxtool.model.keywords._infofile import Infofile
from pxtool.model.keywords._info import Info
from pxtool.model.keywords._notex import Notex
from pxtool.model.keywords._note import Note
from pxtool.model.keywords._valuenotex import Valuenotex
from pxtool.model.keywords._valuenote import Valuenote
from pxtool.model.keywords._datanote import Datanote
from pxtool.model.keywords._cellnotex import Cellnotex
from pxtool.model.keywords._cellnote import Cellnote
from pxtool.model.keywords._datasymbol1 import Datasymbol1
from pxtool.model.keywords._datasymbol2 import Datasymbol2
from pxtool.model.keywords._datasymbol3 import Datasymbol3
from pxtool.model.keywords._datasymbol4 import Datasymbol4
from pxtool.model.keywords._datasymbol5 import Datasymbol5
from pxtool.model.keywords._datasymbol6 import Datasymbol6
from pxtool.model.keywords._datasymbolnil import Datasymbolnil
from pxtool.model.keywords._datasymbolsum import Datasymbolsum
from pxtool.model.keywords._datanotecell import Datanotecell
from pxtool.model.keywords._datanotesum import Datanotesum
from pxtool.model.keywords._keys import Keys
from pxtool.model.keywords._attribute_id import AttributeId
from pxtool.model.keywords._attribute_text import AttributeText
from pxtool.model.keywords._attributes import Attributes
from pxtool.model.keywords._variablecode import Variablecode
from pxtool.model.keywords._meta_id import MetaId
from pxtool.model.keywords._data import Data

class PXFileModel:
    """
    This class holds the information of a PxFile
    the setters have all value has first param, and stuff from the keyword-part after, because some of them are optional.
    """

    def __init__(self) -> None:
        self.charset = Charset("CHARSET")
        self.axis_version = AxisVersion("AXIS-VERSION")
        self.codepage = Codepage("CODEPAGE")
        self.language = Language("LANGUAGE")
        self.languages = Languages("LANGUAGES")
        self.creation_date = CreationDate("CREATION-DATE")
        self.next_update = NextUpdate("NEXT-UPDATE")
        self.px_server = PxServer("PX-SERVER")
        self.directory_path = DirectoryPath("DIRECTORY-PATH")
        self.update_frequency = UpdateFrequency("UPDATE-FREQUENCY")
        self.tableid = Tableid("TABLEID")
        self.synonyms = Synonyms("SYNONYMS")
        self.default_graph = DefaultGraph("DEFAULT-GRAPH")
        self.decimals = Decimals("DECIMALS")
        self.showdecimals = Showdecimals("SHOWDECIMALS")
        self.rounding = Rounding("ROUNDING")
        self.matrix = Matrix("MATRIX")
        self.aggregallowed = Aggregallowed("AGGREGALLOWED")
        self.autopen = Autopen("AUTOPEN")
        self.subject_code = SubjectCode("SUBJECT-CODE")
        self.subject_area = SubjectArea("SUBJECT-AREA")
        self.confidential = Confidential("CONFIDENTIAL")
        self.copyright = Copyright("COPYRIGHT")
        self.description = Description("DESCRIPTION")
        self.title = Title("TITLE")
        self.descriptiondefault = Descriptiondefault("DESCRIPTIONDEFAULT")
        self.contvariable = Contvariable("CONTVARIABLE")
        self.contents = Contents("CONTENTS")
        self.units = Units("UNITS")
        self.stub = Stub("STUB")
        self.heading = Heading("HEADING")
        self.values = Values("VALUES")
        self.timeval = Timeval("TIMEVAL")
        self.codes = Codes("CODES")
        self.doublecolumn = Doublecolumn("DOUBLECOLUMN")
        self.prestext = Prestext("PRESTEXT")
        self.domain = Domain("DOMAIN")
        self.variable_type = VariableType("VARIABLE-TYPE")
        self.hierarchies = Hierarchies("HIERARCHIES")
        self.hierarchylevels = Hierarchylevels("HIERARCHYLEVELS")
        self.hierarchylevelsopen = Hierarchylevelsopen("HIERARCHYLEVELSOPEN")
        self.hierarchynames = Hierarchynames("HIERARCHYNAMES")
        self.map = Map("MAP")
        self.partitioned = Partitioned("PARTITIONED")
        self.elimination = Elimination("ELIMINATION")
        self.precision = Precision("PRECISION")
        self.last_updated = LastUpdated("LAST-UPDATED")
        self.stockfa = Stockfa("STOCKFA")
        self.cfprices = Cfprices("CFPRICES")
        self.dayadj = Dayadj("DAYADJ")
        self.seasadj = Seasadj("SEASADJ")
        self.contact = Contact("CONTACT")
        self.refperiod = Refperiod("REFPERIOD")
        self.baseperiod = Baseperiod("BASEPERIOD")
        self.database = Database("DATABASE")
        self.source = Source("SOURCE")
        self.official_statistics = OfficialStatistics("OFFICIAL-STATISTICS")
        self.survey = Survey("SURVEY")
        self.link = Link("LINK")
        self.infofile = Infofile("INFOFILE")
        self.info = Info("INFO")
        self.notex = Notex("NOTEX")
        self.note = Note("NOTE")
        self.valuenotex = Valuenotex("VALUENOTEX")
        self.valuenote = Valuenote("VALUENOTE")
        self.datanote = Datanote("DATANOTE")
        self.cellnotex = Cellnotex("CELLNOTEX")
        self.cellnote = Cellnote("CELLNOTE")
        self.datasymbol1 = Datasymbol1("DATASYMBOL1")
        self.datasymbol2 = Datasymbol2("DATASYMBOL2")
        self.datasymbol3 = Datasymbol3("DATASYMBOL3")
        self.datasymbol4 = Datasymbol4("DATASYMBOL4")
        self.datasymbol5 = Datasymbol5("DATASYMBOL5")
        self.datasymbol6 = Datasymbol6("DATASYMBOL6")
        self.datasymbolnil = Datasymbolnil("DATASYMBOLNIL")
        self.datasymbolsum = Datasymbolsum("DATASYMBOLSUM")
        self.datanotecell = Datanotecell("DATANOTECELL")
        self.datanotesum = Datanotesum("DATANOTESUM")
        self.keys = Keys("KEYS")
        self.attribute_id = AttributeId("ATTRIBUTE-ID")
        self.attribute_text = AttributeText("ATTRIBUTE-TEXT")
        self.attributes = Attributes("ATTRIBUTES")
        self.variablecode = Variablecode("VARIABLECODE")
        self.meta_id = MetaId("META-ID")
        self.data = Data("DATA")

    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)
