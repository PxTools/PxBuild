class Domain:
    _key_value_rows: list = []

    def __init__(self) -> None:
        self._section = "[Domain]"
        self._key_value_rows.clear()

    def set(self, vskey: str, vsvalue: str):

        vskey = vskey
        vsvalue = vsvalue
        my_dict = {"key": vskey, "val": vsvalue}
        self._key_value_rows.append((my_dict))

    def __str__(self):
        out_str = f"{self._section}\n"

        for my_dict in self._key_value_rows:
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"
        return out_str
