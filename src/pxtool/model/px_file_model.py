from model.keywords._charset import _PX_CHARSET
from model.keywords._axis_version import _PX_AXIS_VERSION
from model.keywords._codepage import _PX_CODEPAGE
from model.keywords._language import _PX_LANGUAGE
from model.keywords._languages import _PX_LANGUAGES
from model.keywords._creation_date import _PX_CREATION_DATE
from model.keywords._next_update import _PX_NEXT_UPDATE
from model.keywords._px_server import _PX_PX_SERVER
from model.keywords._directory_path import _PX_DIRECTORY_PATH
from model.keywords._update_frequency import _PX_UPDATE_FREQUENCY
from model.keywords._tableid import _PX_TABLEID
from model.keywords._synonyms import _PX_SYNONYMS
from model.keywords._default_graph import _PX_DEFAULT_GRAPH
from model.keywords._decimals import _PX_DECIMALS
from model.keywords._showdecimals import _PX_SHOWDECIMALS
from model.keywords._rounding import _PX_ROUNDING
from model.keywords._matrix import _PX_MATRIX
from model.keywords._aggregallowed import _PX_AGGREGALLOWED
from model.keywords._autopen import _PX_AUTOPEN
from model.keywords._subject_code import _PX_SUBJECT_CODE
from model.keywords._subject_area import _PX_SUBJECT_AREA
from model.keywords._confidential import _PX_CONFIDENTIAL
from model.keywords._copyright import _PX_COPYRIGHT
from model.keywords._description import _PX_DESCRIPTION
from model.keywords._title import _PX_TITLE
from model.keywords._descriptiondefault import _PX_DESCRIPTIONDEFAULT
from model.keywords._contvariable import _PX_CONTVARIABLE
from model.keywords._contents import _PX_CONTENTS
from model.keywords._units import _PX_UNITS
from model.keywords._stub import _PX_STUB
from model.keywords._heading import _PX_HEADING
from model.keywords._values import _PX_VALUES
from model.keywords._timeval import _PX_TIMEVAL
from model.keywords._codes import _PX_CODES
from model.keywords._doublecolumn import _PX_DOUBLECOLUMN
from model.keywords._prestext import _PX_PRESTEXT
from model.keywords._domain import _PX_DOMAIN
from model.keywords._variable_type import _PX_VARIABLE_TYPE
from model.keywords._hierarchies import _PX_HIERARCHIES
from model.keywords._hierarchylevels import _PX_HIERARCHYLEVELS
from model.keywords._hierarchylevelsopen import _PX_HIERARCHYLEVELSOPEN
from model.keywords._hierarchynames import _PX_HIERARCHYNAMES
from model.keywords._map import _PX_MAP
from model.keywords._partitioned import _PX_PARTITIONED
from model.keywords._elimination import _PX_ELIMINATION
from model.keywords._precision import _PX_PRECISION
from model.keywords._last_updated import _PX_LAST_UPDATED
from model.keywords._stockfa import _PX_STOCKFA
from model.keywords._cfprices import _PX_CFPRICES
from model.keywords._dayadj import _PX_DAYADJ
from model.keywords._seasadj import _PX_SEASADJ
from model.keywords._contact import _PX_CONTACT
from model.keywords._refperiod import _PX_REFPERIOD
from model.keywords._baseperiod import _PX_BASEPERIOD
from model.keywords._database import _PX_DATABASE
from model.keywords._source import _PX_SOURCE
from model.keywords._survey import _PX_SURVEY
from model.keywords._link import _PX_LINK
from model.keywords._infofile import _PX_INFOFILE
from model.keywords._info import _PX_INFO
from model.keywords._notex import _PX_NOTEX
from model.keywords._note import _PX_NOTE
from model.keywords._valuenotex import _PX_VALUENOTEX
from model.keywords._valuenote import _PX_VALUENOTE
from model.keywords._datanote import _PX_DATANOTE
from model.keywords._cellnotex import _PX_CELLNOTEX
from model.keywords._cellnote import _PX_CELLNOTE
from model.keywords._datasymbol1 import _PX_DATASYMBOL1
from model.keywords._datasymbol2 import _PX_DATASYMBOL2
from model.keywords._datasymbol3 import _PX_DATASYMBOL3
from model.keywords._datasymbol4 import _PX_DATASYMBOL4
from model.keywords._datasymbol5 import _PX_DATASYMBOL5
from model.keywords._datasymbol6 import _PX_DATASYMBOL6
from model.keywords._datasymbolnil import _PX_DATASYMBOLNIL
from model.keywords._datasymbolsum import _PX_DATASYMBOLSUM
from model.keywords._datanotecell import _PX_DATANOTECELL
from model.keywords._datanotesum import _PX_DATANOTESUM
from model.keywords._keys import _PX_KEYS
from model.keywords._attribute_id import _PX_ATTRIBUTE_ID
from model.keywords._attribute_text import _PX_ATTRIBUTE_TEXT
from model.keywords._attributes import _PX_ATTRIBUTES
from model.keywords._variable_code import _PX_VARIABLE_CODE
from model.keywords._meta_id import _PX_META_ID
from model.keywords._data import _PX_DATA

class PXFileModel:
    """
    This class holds the information of a PxFile
    the setters have all value has first param, and stuff from the keyword-part after, because some of them are optional.
    """

    def __init__(self) -> None:
        self.charset = _PX_CHARSET("CHARSET")
        self.axis_version = _PX_AXIS_VERSION("AXIS-VERSION")
        self.codepage = _PX_CODEPAGE("CODEPAGE")
        self.language = _PX_LANGUAGE("LANGUAGE")
        self.languages = _PX_LANGUAGES("LANGUAGES")
        self.creation_date = _PX_CREATION_DATE("CREATION-DATE")
        self.next_update = _PX_NEXT_UPDATE("NEXT-UPDATE")
        self.px_server = _PX_PX_SERVER("PX-SERVER")
        self.directory_path = _PX_DIRECTORY_PATH("DIRECTORY-PATH")
        self.update_frequency = _PX_UPDATE_FREQUENCY("UPDATE-FREQUENCY")
        self.tableid = _PX_TABLEID("TABLEID")
        self.synonyms = _PX_SYNONYMS("SYNONYMS")
        self.default_graph = _PX_DEFAULT_GRAPH("DEFAULT-GRAPH")
        self.decimals = _PX_DECIMALS("DECIMALS")
        self.showdecimals = _PX_SHOWDECIMALS("SHOWDECIMALS")
        self.rounding = _PX_ROUNDING("ROUNDING")
        self.matrix = _PX_MATRIX("MATRIX")
        self.aggregallowed = _PX_AGGREGALLOWED("AGGREGALLOWED")
        self.autopen = _PX_AUTOPEN("AUTOPEN")
        self.subject_code = _PX_SUBJECT_CODE("SUBJECT-CODE")
        self.subject_area = _PX_SUBJECT_AREA("SUBJECT-AREA")
        self.confidential = _PX_CONFIDENTIAL("CONFIDENTIAL")
        self.copyright = _PX_COPYRIGHT("COPYRIGHT")
        self.description = _PX_DESCRIPTION("DESCRIPTION")
        self.title = _PX_TITLE("TITLE")
        self.descriptiondefault = _PX_DESCRIPTIONDEFAULT("DESCRIPTIONDEFAULT")
        self.contvariable = _PX_CONTVARIABLE("CONTVARIABLE")
        self.contents = _PX_CONTENTS("CONTENTS")
        self.units = _PX_UNITS("UNITS")
        self.stub = _PX_STUB("STUB")
        self.heading = _PX_HEADING("HEADING")
        self.values = _PX_VALUES("VALUES")
        self.timeval = _PX_TIMEVAL("TIMEVAL")
        self.codes = _PX_CODES("CODES")
        self.doublecolumn = _PX_DOUBLECOLUMN("DOUBLECOLUMN")
        self.prestext = _PX_PRESTEXT("PRESTEXT")
        self.domain = _PX_DOMAIN("DOMAIN")
        self.variable_type = _PX_VARIABLE_TYPE("VARIABLE-TYPE")
        self.hierarchies = _PX_HIERARCHIES("HIERARCHIES")
        self.hierarchylevels = _PX_HIERARCHYLEVELS("HIERARCHYLEVELS")
        self.hierarchylevelsopen = _PX_HIERARCHYLEVELSOPEN("HIERARCHYLEVELSOPEN")
        self.hierarchynames = _PX_HIERARCHYNAMES("HIERARCHYNAMES")
        self.map = _PX_MAP("MAP")
        self.partitioned = _PX_PARTITIONED("PARTITIONED")
        self.elimination = _PX_ELIMINATION("ELIMINATION")
        self.precision = _PX_PRECISION("PRECISION")
        self.last_updated = _PX_LAST_UPDATED("LAST-UPDATED")
        self.stockfa = _PX_STOCKFA("STOCKFA")
        self.cfprices = _PX_CFPRICES("CFPRICES")
        self.dayadj = _PX_DAYADJ("DAYADJ")
        self.seasadj = _PX_SEASADJ("SEASADJ")
        self.contact = _PX_CONTACT("CONTACT")
        self.refperiod = _PX_REFPERIOD("REFPERIOD")
        self.baseperiod = _PX_BASEPERIOD("BASEPERIOD")
        self.database = _PX_DATABASE("DATABASE")
        self.source = _PX_SOURCE("SOURCE")
        self.survey = _PX_SURVEY("SURVEY")
        self.link = _PX_LINK("LINK")
        self.infofile = _PX_INFOFILE("INFOFILE")
        self.info = _PX_INFO("INFO")
        self.notex = _PX_NOTEX("NOTEX")
        self.note = _PX_NOTE("NOTE")
        self.valuenotex = _PX_VALUENOTEX("VALUENOTEX")
        self.valuenote = _PX_VALUENOTE("VALUENOTE")
        self.datanote = _PX_DATANOTE("DATANOTE")
        self.cellnotex = _PX_CELLNOTEX("CELLNOTEX")
        self.cellnote = _PX_CELLNOTE("CELLNOTE")
        self.datasymbol1 = _PX_DATASYMBOL1("DATASYMBOL1")
        self.datasymbol2 = _PX_DATASYMBOL2("DATASYMBOL2")
        self.datasymbol3 = _PX_DATASYMBOL3("DATASYMBOL3")
        self.datasymbol4 = _PX_DATASYMBOL4("DATASYMBOL4")
        self.datasymbol5 = _PX_DATASYMBOL5("DATASYMBOL5")
        self.datasymbol6 = _PX_DATASYMBOL6("DATASYMBOL6")
        self.datasymbolnil = _PX_DATASYMBOLNIL("DATASYMBOLNIL")
        self.datasymbolsum = _PX_DATASYMBOLSUM("DATASYMBOLSUM")
        self.datanotecell = _PX_DATANOTECELL("DATANOTECELL")
        self.datanotesum = _PX_DATANOTESUM("DATANOTESUM")
        self.keys = _PX_KEYS("KEYS")
        self.attribute_id = _PX_ATTRIBUTE_ID("ATTRIBUTE-ID")
        self.attribute_text = _PX_ATTRIBUTE_TEXT("ATTRIBUTE-TEXT")
        self.attributes = _PX_ATTRIBUTES("ATTRIBUTES")
        self.variable_code = _PX_VARIABLE_CODE("VARIABLE-CODE")
        self.meta_id = _PX_META_ID("META-ID")
        self.data = _PX_DATA("DATA")

    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)
