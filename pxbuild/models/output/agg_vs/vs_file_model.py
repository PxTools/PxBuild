from pxtool.models.output.agg_vs.sections._description import Description
from pxtool.models.output.agg_vs.sections._aggreg import Aggreg
from pxtool.models.output.agg_vs.sections._domain import Domain
from pxtool.models.output.agg_vs.sections._valuecode import Valuecode
from pxtool.models.output.agg_vs.sections._valuetext import Valuetext

class _VSFileModel():
    def __init__(self) -> None:
        self.description = Description()
        self.aggreg = Aggreg() 
        self.domain = Domain()
        self.valuecode = Valuecode()
        self.valuetext = Valuetext()
    
    def __str__(self):
        attrs = vars(self)
        attr_strings = [str(value) for value in attrs.values() if str(value) != ""]
        return "\n".join(attr_strings)