import re

from pxtool.models.output.pxfile.px_file_model import PXFileModel
import pxtool.models.output.pxfile.util.constants as constants


class QuotedItem:
    def __init__(self, string: str) -> None:
        self.string: str = '"""' + string + '"""'

    def has_px_part_separator(self) -> bool:
        return False

    def has_px_endline(self) -> bool:
        return False

    def has_subkey_start(self) -> bool:
        return False

    def trim_whitespace(self) -> None:
        pass

    def is_type_quoted(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"QuotedItem in quotes:{self.string}"


class UnQuotedItem:
    def __init__(self, string: str) -> None:
        self.string: str = string

    def has_px_part_separator(self) -> bool:
        return "=" in self.string

    def has_px_endline(self) -> bool:
        return ";" in self.string

    def has_subkey_start(self) -> bool:
        return "(" in self.string

    def get_before_and_after(self, split_char: str) -> tuple:
        string1, _, string2 = self.string.partition(split_char)
        return string1, string2

    def trim_whitespace(self) -> None:
        self.string = re.sub(r"\s+", "", self.string)

    def is_type_quoted(self) -> bool:
        return False

    def __str__(self):
        return f"UnQuotedItem:{self.string}"


class Keypart:
    keyword: str
    language: str
    sub_keys: list[str]

    def __init__(self, keyword: str, language: str, sub_keys: list[str]) -> None:
        self.keyword = keyword
        self.language = language
        self.sub_keys = sub_keys

    def __str__(self):
        lang_part = f"[{self.language}]" if self.language else ""
        subkey_part = "(" + ",".join(self.sub_keys) + ")" if self.sub_keys else ""
        return f"{self.keyword}{lang_part}{subkey_part}"


class Loader:
    @staticmethod
    def is_even(value: int) -> bool:
        if value % 2 == 0:
            return True
        else:
            return False

    def digest_keypart_valuepart_pair(self, key_items: list, value_items: list) -> None:
        keypart = self.get_keypart(key_items)
        if keypart.keyword in constants.KEYWORDS_PYTHONIC_MAP.keys():
            self.fix_value_part(keypart, value_items)
        else:
            self.when_unknown_keyword(keypart, value_items)

    def get_keypart(self, items: list) -> Keypart:
        # keypart: KEYWORD[lang]( quotedsubkeys sep by ",")
        # only KEYWORD ismandatory, lang may be quoted

        # split items into before and after start subkey
        items_before_subkey = []
        items_after_subkey = []
        found_subkey = False

        for item in items:
            item.trim_whitespace()
            if item.has_subkey_start():
                string_before, string_after = item.get_before_and_after("(")
                if string_before:
                    items_before_subkey.append(UnQuotedItem(string_before))
                if string_after:
                    raise Exception(f'Hmm, there is something:{string_after} between ( and first " in keypart.')
                found_subkey = True
            else:
                if found_subkey:
                    items_after_subkey.append(item)
                else:
                    items_before_subkey.append(item)

        sub_keys = [x.string for x in items_after_subkey if x.is_type_quoted()]

        # The spec in unclear on  if both ["en"] and [en]  is allowed.
        # first item will be UnQuoted and will contain the "[" if language is present in the keypart.
        keyword = ""
        lang_value = ""
        if items_before_subkey[0].is_type_quoted() or items_before_subkey[0].string == "":
            raise Exception(f"Hmm, expected non-empty UnquotedItem.")
        else:
            if "[" in items_before_subkey[0].string:
                keyword, string_after = items_before_subkey[0].get_before_and_after("[")
                if "]" in string_after:  # stringAfter must be: en]
                    lang_value = '"""' + string_after[:2] + '"""'
                else:
                    lang_value = items_before_subkey[1].string
            else:
                keyword = items_before_subkey[0].string

        return Keypart(keyword, lang_value, sub_keys)

    def when_unknown_keyword(self, keypart: Keypart, valueitems: list) -> None:
        very_quoted_string = f"{keypart}={''.join([str(x.string) for x in valueitems])};"
        add_string = very_quoted_string.replace('"""', '"')  # .replace("\"\"","\"")
        # strings are """ quoted for strings with newline to survive in a exec

        if self.outModel.unknown_keywords:
            self.outModel.unknown_keywords = self.outModel.unknown_keywords + "\n" + add_string
        else:
            self.outModel.unknown_keywords = add_string

    def fix_value_part(self, keypart: Keypart, items: list) -> None:
        attr_name = constants.KEYWORDS_PYTHONIC_MAP[keypart.keyword]
        print(f"    Valuepart for {attr_name}")

        my_attri = vars(self.outModel)[attr_name]
        # "MADE-WITH"

        out_lang_part = ""
        if keypart.language:
            out_lang_part = f", lang={keypart.language}"

        out_subkey_part = ""
        if len(keypart.sub_keys) > 0:
            out_subkey_part = f", {', '.join(keypart.sub_keys)}"

        out_value = ""
        do_run_exec = True

        if my_attri.pxvalue_type == "_PxString":
            if len(items) != 1:
                raise ValueError(
                    f"Value for keypart {keypart}: Excepting single quoted string, but items has not len = 1 "
                )
            out_value = items[0].string
        elif my_attri.pxvalue_type == "_PxBool":
            if len(items) != 1:
                raise ValueError(
                    f"Value for keypart {keypart}: Excepting single unquoted string YES or NO, but items has not len = 1"
                )
            out_value = "True"
            if items[0].string not in ["YES", "NO"]:
                raise ValueError(
                    f"Value for keypart {keypart}: Boolean values must be YES or NO, not:{items[0].string}"
                )
            if items[0].string == "NO":
                out_value = "False"
        elif my_attri.pxvalue_type == "_PxInt":
            if len(items) != 1:
                raise ValueError(
                    f"Value for keypart {keypart}: Excepting an integer as single unquoted string, but items has not len = 1"
                )

            if not items[0].string.isdecimal():
                raise ValueError(f"Value for keypart {keypart}: integer value convertion")

            out_value = "False"
        elif my_attri.pxvalue_type == "_PxStringList":
            print("Stringlist")
            if Loader.is_even(len(items)):
                raise ValueError(f"Bad list")
            if not items[0].is_type_quoted():
                raise ValueError(f"Value for keypart {keypart}: List must start with quoted string")

            my_strings = []
            for idx, x in enumerate(items):
                if Loader.is_even(idx):
                    my_strings.append(x.string)
                else:
                    x.trim_whitespace()
                    if x.string != ",":
                        raise ValueError(
                            f"Value for keypart {keypart}: Bad list, at item-index{idx}: expected comma found {x.string}"
                        )

            out_value = "[" + ",".join(my_strings) + "]"

            for item in items:
                print(f"      {item}")
            print("    --------")
        elif my_attri.pxvalue_type == "_PxTlist":
            # TLIST(A1, ”1994”-”1996”);  or TLIST(A1), ”1994”, ”1995”,"1996”;
            first_item = items.pop(0)
            tmp = first_item.string.replace("TLIST(", "").strip()
            timescale = tmp[0:2]

            out_value = f'"{timescale}", '

            if len(items) > 2 and items[1].string.strip() == "-":
                out_value = out_value + f'{items[0].string} "-" {items[2].string}'
            else:
                out_value = out_value + "["
                for item in items:
                    out_value = out_value + item.string
                out_value = out_value + "]"
        elif my_attri.pxvalue_type == "_PxData":
            data_list = []
            for item in items:
                data_list.append(item.string)
            # self.outModel.data.set()
            self.outModel.data.set(data_list, 1)
            do_run_exec = False

        if do_run_exec:
            string_to_exec = f"self.outModel.{attr_name}.set({out_value}{out_subkey_part}{out_lang_part})"
            print("do_exec:" + string_to_exec)
            exec(string_to_exec)

        print(f"---- etter keyword {keypart}  er modellen ----")
        print(self.outModel)

        print("--------")

    @staticmethod
    def get_file_in_chunks(filename: str) -> list:
        """Reads file, removes any QuoteNewlineQuote, splits on quote and retuns the list with UnQuotedItem and QuotedItem"""
        my_out = []

        with open(filename, "r") as file:
            file_contents1: str = file.read()

        first_chars: str = file_contents1[:2]
        if not first_chars.isalpha():
            raise ValueError(f"A PxFile must start with a letter. {filename} does not.")

        file_contents2: str = file_contents1.replace('"\n"', "")
        split_file_on_quote = file_contents2.split('"')

        unquoted = True
        for item in split_file_on_quote:
            if unquoted:
                my_out.append(UnQuotedItem(item))
            else:
                my_out.append(QuotedItem(item))
            unquoted = not unquoted

        return my_out

    def __init__(self, filename: str) -> None:
        self.outModel: PXFileModel = PXFileModel()

        file = Loader.get_file_in_chunks(filename)

        current_key_items = []
        current_value_items = []
        collecting_key = True

        while len(file) > 0:
            item = file.pop(0)
            print(f"item:{item}")
            if collecting_key:
                if not item.has_px_part_separator():
                    current_key_items.append(item)
                else:
                    string_before, string_after = item.get_before_and_after("=")
                    if string_before:
                        current_key_items.append(UnQuotedItem(string_before))
                    if string_after:
                        # put the "unused" part of the string back
                        file.insert(0, UnQuotedItem(string_after))
                    collecting_key = False
            else:
                # collection Valuepart
                if not item.has_px_endline():
                    current_value_items.append(item)
                else:
                    string_before, string_after = item.get_before_and_after(";")
                    if string_before:
                        current_value_items.append(UnQuotedItem(string_before))
                    if string_after:
                        # put the "unused" part of the string back
                        file.insert(0, UnQuotedItem(string_after))

                    self.digest_keypart_valuepart_pair(current_key_items, current_value_items)

                    # get ready for next record
                    collecting_key = True
                    current_key_items = []
                    current_value_items = []

        print(self.outModel)
