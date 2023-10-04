from pxtool.models.output.agg_vs.sections._description import _Description
from pxtool.models.output.agg_vs.sections._aggreg import _Aggreg
from pxtool.models.output.agg_vs.sections._domain import _Domain
from pxtool.models.output.agg_vs.sections._valuecode import _Valuecode
from pxtool.models.output.agg_vs.sections._valuetext import _Valuetext

class _VSFileModel():
    def __init__(self) -> None:
        self.description = _Description()
        self.aggreg = _Aggreg() 
        self.domain = _Domain()
        self.valuecode = _Valuecode()
        self.valuetext = _Valuetext()
    
    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)