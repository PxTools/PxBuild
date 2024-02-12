from jinja2 import Environment, FileSystemLoader


class TstTemplates:
    def __init__(self) -> None:
        env = Environment(loader=FileSystemLoader("jinja2_templates"))
        self.intro = env.get_template("intro.jinja2")
        self.set_valid_keyless = env.get_template("set_valid_keyless.jinja2")
        self.set_valid_with_key = env.get_template("set_valid_with_key.jinja2")

        self.set_invalid_keyless = env.get_template("set_invalid_keyless.jinja2")
        self.set_invalid_with_key = env.get_template("set_invalid_with_key.jinja2")

        self.language_management_no_subkey = env.get_template("language_management_no_subkey.jinja2")
        self.language_management_with_subkey = env.get_template("language_management_with_subkey.jinja2")

        self.duplicate_set_raises_keyless = env.get_template("set_duplicate_keyless.jinja2")
        self.duplicate_set_raises_with_key = env.get_template("set_duplicate_with_key.jinja2")

        self.hack_forcing_error_multi_raises_with_key = env.get_template(
            "hack_forcing_error_multi_raises_with_key.jinja2"
        )
