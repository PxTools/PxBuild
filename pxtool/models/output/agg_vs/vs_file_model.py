from pxtool.models.output.agg_vs.sections._description import _Description
from pxtool.models.output.agg_vs.sections._aggreg import _Aggreg
from pxtool.models.output.agg_vs.sections._domain import _Domain

class _VSFileModel():
    def __init__(self) -> None:
        self.description = _Description()
        self.aggreg = _Aggreg() 
        self.domain = _Domain()
    
    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)