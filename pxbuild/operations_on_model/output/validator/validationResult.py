class ValidationResult:
    desc:str
    is_valid:bool
    error_msg:str

    def __init__(self, desc) -> None:
        self.desc = desc
        self.is_valid = True

    def add_error(self, error:str):
        self.error_msg = error
        self.is_valid = False

    def __str__(self)-> str:
        rep_str = f"{self.desc}"
        if self.is_valid:
            rep_str += "\n" + "Validation passed"
        else:
            rep_str += "\n" + "Validation failed" + "\n" + f"Error: {self.error_msg}"
        return rep_str
