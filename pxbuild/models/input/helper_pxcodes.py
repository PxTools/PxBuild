from .pydantic_pxcodes import PxCodes, Grouping, Valueitem, Note
from typing import Dict, List


def sort_valueitems_by_field(objects: List[Valueitem], sort_by: str, lang: str):
    # Define a custom sorting key function based on the specified key
    def get_sort_key(obj: Valueitem) -> str:
        if sort_by == "code":
            return obj.code
        elif sort_by == "label":
            return obj.label[lang]

        return obj.rank[lang]

    # Sort the objects using the custom sorting key
    return sorted(objects, key=get_sort_key)


class HelperPxCodes:
    def __init__(self, in_pxcodes: PxCodes, in_languages: List[str]) -> None:
        self._pxcodes = in_pxcodes
        self.elimination_possible = in_pxcodes.elimination_possible

        sortby = str(in_pxcodes.sort_valueitems_on).replace("SortValueitemsOn.", "")
        # print("sortby",sortby,"inPxCodes.sort_valueitems_on",str(inPxCodes.sort_valueitems_on))

        self._sorted_valueitems = {}
        for lang in in_languages:
            self._sorted_valueitems[lang] = sort_valueitems_by_field(in_pxcodes.valueitems, sortby, lang)

    # self._has_grouping:bool = False
    # if inPxCodes.groupings:
    #     self._has_grouping = True

    def get_codes(self, language: str) -> List[str]:
        if language not in self._sorted_valueitems:
            raise ValueError(f"Language '{language}' not found in _sorted_valueitems")
        return [valueitem.code for valueitem in self._sorted_valueitems[language]]

    def get_labels(self, language: str) -> List[str]:
        return [valueitem.label[language] for valueitem in self._sorted_valueitems[language]]

    def get_elimination_label(self, language: str) -> str:
        my_out: str = ""
        if self._pxcodes.elimination_possible and self._pxcodes.elimination_code:
            # need to find label ...
            my_out = self.get_label(language, self._pxcodes.elimination_code)
        return my_out

    def get_label(self, language: str, code: str) -> str:
        my_out: str = ""
        for valueitem in self._pxcodes.valueitems:
            if valueitem.code == code:
                my_out = valueitem.label[language]
                break
        return my_out

    def get_valueotes(self):
        my_out: Dict[str, List[Note]] = dict()

        for valueitem in self._pxcodes.valueitems:
            if valueitem.notes:
                my_out[str(valueitem.code)] = valueitem.notes

        return my_out

    #   def has_grouping(self) -> bool:
    #       return self._has_grouping

    def groupings(self) -> List[Grouping] | None:
        return self._pxcodes.groupings

    def id(self) -> str:
        return self._pxcodes.id
