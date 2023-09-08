import pxtool.model.util.constants as constants
from pxtool.model.px_file_model import PXFileModel

def apply_default_language(model:PXFileModel):
        """ inserts the actual language where default is use for language
        So that
        LANGUAGE=en  +
        KEYWORD3="Work and stuff";
        =
        KEYWORD3["en"]="Work and stuff";
        """
        if model.language.has_value():
            to_lang=model.language.get_value()
            for kw in constants.LANGDEPENDENT_KEYWORDS:
                instance = model.get_attribute(kw)
                if instance.is_present():
                    instance.reset_language_none_to(to_lang)



