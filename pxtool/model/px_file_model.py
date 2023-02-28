from pxtool.model.keywords._charset import _PX_CHARSET
from pxtool.model.keywords._axis_version import _PX_AXIS_VERSION
from pxtool.model.keywords._codepage import _PX_CODEPAGE
from pxtool.model.keywords._language import _PX_LANGUAGE
from pxtool.model.keywords._languages import _PX_LANGUAGES
from pxtool.model.keywords._creation_date import _PX_CREATION_DATE
from pxtool.model.keywords._next_update import _PX_NEXT_UPDATE
from pxtool.model.keywords._px_server import _PX_PX_SERVER
from pxtool.model.keywords._directory_path import _PX_DIRECTORY_PATH
from pxtool.model.keywords._update_frequency import _PX_UPDATE_FREQUENCY
from pxtool.model.keywords._tableid import _PX_TABLEID
from pxtool.model.keywords._synonyms import _PX_SYNONYMS
from pxtool.model.keywords._default_graph import _PX_DEFAULT_GRAPH
from pxtool.model.keywords._decimals import _PX_DECIMALS
from pxtool.model.keywords._showdecimals import _PX_SHOWDECIMALS
from pxtool.model.keywords._rounding import _PX_ROUNDING
from pxtool.model.keywords._matrix import _PX_MATRIX
from pxtool.model.keywords._aggregallowed import _PX_AGGREGALLOWED
from pxtool.model.keywords._autopen import _PX_AUTOPEN
from pxtool.model.keywords._subject_code import _PX_SUBJECT_CODE
from pxtool.model.keywords._subject_area import _PX_SUBJECT_AREA
from pxtool.model.keywords._confidential import _PX_CONFIDENTIAL
from pxtool.model.keywords._copyright import _PX_COPYRIGHT
from pxtool.model.keywords._description import _PX_DESCRIPTION
from pxtool.model.keywords._title import _PX_TITLE
from pxtool.model.keywords._descriptiondefault import _PX_DESCRIPTIONDEFAULT
from pxtool.model.keywords._contvariable import _PX_CONTVARIABLE
from pxtool.model.keywords._contents import _PX_CONTENTS
from pxtool.model.keywords._units import _PX_UNITS
from pxtool.model.keywords._stub import _PX_STUB
from pxtool.model.keywords._heading import _PX_HEADING
from pxtool.model.keywords._values import _PX_VALUES
from pxtool.model.keywords._timeval import _PX_TIMEVAL
from pxtool.model.keywords._codes import _PX_CODES
from pxtool.model.keywords._doublecolumn import _PX_DOUBLECOLUMN
from pxtool.model.keywords._prestext import _PX_PRESTEXT
from pxtool.model.keywords._domain import _PX_DOMAIN
from pxtool.model.keywords._variable_type import _PX_VARIABLE_TYPE
from pxtool.model.keywords._hierarchies import _PX_HIERARCHIES
from pxtool.model.keywords._hierarchylevels import _PX_HIERARCHYLEVELS
from pxtool.model.keywords._hierarchylevelsopen import _PX_HIERARCHYLEVELSOPEN
from pxtool.model.keywords._hierarchynames import _PX_HIERARCHYNAMES
from pxtool.model.keywords._map import _PX_MAP
from pxtool.model.keywords._partitioned import _PX_PARTITIONED
from pxtool.model.keywords._elimination import _PX_ELIMINATION
from pxtool.model.keywords._precision import _PX_PRECISION
from pxtool.model.keywords._last_updated import _PX_LAST_UPDATED
from pxtool.model.keywords._stockfa import _PX_STOCKFA
from pxtool.model.keywords._cfprices import _PX_CFPRICES
from pxtool.model.keywords._dayadj import _PX_DAYADJ
from pxtool.model.keywords._seasadj import _PX_SEASADJ
from pxtool.model.keywords._contact import _PX_CONTACT
from pxtool.model.keywords._refperiod import _PX_REFPERIOD
from pxtool.model.keywords._baseperiod import _PX_BASEPERIOD
from pxtool.model.keywords._database import _PX_DATABASE
from pxtool.model.keywords._source import _PX_SOURCE
from pxtool.model.keywords._survey import _PX_SURVEY
from pxtool.model.keywords._link import _PX_LINK
from pxtool.model.keywords._infofile import _PX_INFOFILE
from pxtool.model.keywords._info import _PX_INFO
from pxtool.model.keywords._notex import _PX_NOTEX
from pxtool.model.keywords._note import _PX_NOTE
from pxtool.model.keywords._valuenotex import _PX_VALUENOTEX
from pxtool.model.keywords._valuenote import _PX_VALUENOTE
from pxtool.model.keywords._datanote import _PX_DATANOTE
from pxtool.model.keywords._cellnotex import _PX_CELLNOTEX
from pxtool.model.keywords._cellnote import _PX_CELLNOTE
from pxtool.model.keywords._datasymbol1 import _PX_DATASYMBOL1
from pxtool.model.keywords._datasymbol2 import _PX_DATASYMBOL2
from pxtool.model.keywords._datasymbol3 import _PX_DATASYMBOL3
from pxtool.model.keywords._datasymbol4 import _PX_DATASYMBOL4
from pxtool.model.keywords._datasymbol5 import _PX_DATASYMBOL5
from pxtool.model.keywords._datasymbol6 import _PX_DATASYMBOL6
from pxtool.model.keywords._datasymbolnil import _PX_DATASYMBOLNIL
from pxtool.model.keywords._datasymbolsum import _PX_DATASYMBOLSUM
from pxtool.model.keywords._datanotecell import _PX_DATANOTECELL
from pxtool.model.keywords._datanotesum import _PX_DATANOTESUM
from pxtool.model.keywords._keys import _PX_KEYS
from pxtool.model.keywords._attribute_id import _PX_ATTRIBUTE_ID
from pxtool.model.keywords._attribute_text import _PX_ATTRIBUTE_TEXT
from pxtool.model.keywords._attributes import _PX_ATTRIBUTES
from pxtool.model.keywords._variablecode import _PX_VARIABLECODE
from pxtool.model.keywords._meta_id import _PX_META_ID
from pxtool.model.keywords._data import _PX_DATA

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
        self.variablecode = _PX_VARIABLECODE("VARIABLECODE")
        self.meta_id = _PX_META_ID("META-ID")
        self.data = _PX_DATA("DATA")

    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)
