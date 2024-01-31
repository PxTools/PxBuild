from pxbuild.models.output.pxfile.px_file_model import PXFileModel
import pxbuild.models.output.pxfile.util.constants as constants


def apply_default_language(model: PXFileModel):
    """inserts the actual language where default is use for language
    So that
    LANGUAGE=en  +
    KEYWORD3="Work and stuff";
    =
    KEYWORD3["en"]="Work and stuff";
    """
    if model.language.has_value():
        to_lang = model.language.get_value()
        for kw in constants.LANGDEPENDENT_KEYWORDS:
            instance = model.get_attribute(kw)
            if instance.is_present():
                instance.reset_language_none_to(to_lang)
