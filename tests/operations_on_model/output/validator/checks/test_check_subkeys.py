from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_subkeys import check_valuebased_subkeys


def _get_model() -> PXFileModel:
    pxfile = PXFileModel()
    pxfile.languages.set(["sv", "fi"])

    pxfile.stub.set(["var1_sv", "var2_sv"], "sv")
    pxfile.stub.set(["var1_fi", "var2_fi"], "fi")

    pxfile.heading.set(["var3_sv"], "sv")
    pxfile.heading.set(["var3_fi"], "fi")

    pxfile.values.set(["val1", "val2"], "var1_sv", "sv")
    pxfile.values.set(["val1", "val2", "val3", "val4_sv"], "var2_sv", "sv")
    pxfile.values.set(["val1"], "var3_sv", "sv")

    pxfile.values.set(["val1", "val2"], "var1_fi", "fi")
    pxfile.values.set(["val1", "val2", "val3", "val4"], "var2_fi", "fi")
    pxfile.values.set(["val1"], "var3_fi", "fi")

    pxfile.contvariable.set("var2_sv", "sv")
    pxfile.contvariable.set("var2_fi", "fi")
    pxfile.seasadj.set(True, "val1", "sv")
    pxfile.seasadj.set(True, "val1", "fi")
    pxfile.dayadj.set(True, "val4_sv", "sv")
    pxfile.dayadj.set(True, "val4", "fi")
    pxfile.doublecolumn.set(True, "var1_sv", "sv")
    pxfile.doublecolumn.set(True, "var1_fi", "fi")

    pxfile.note.set("A note for table in sv", None, "sv")
    pxfile.note.set("A note for table in fi", None, "fi")

    pxfile.precision.set(2, "var1_sv", "val1", "sv")
    pxfile.precision.set(2, "var1_fi", "val1", "fi")

    pxfile.attributes.set(["A", "F"], ["c1", "*", "c3"])
    pxfile.cellnote.set("A cellnote", ["val2", "val2", "*"], "sv")
    pxfile.cellnote.set("A cellnote", ["val2", "val2", "*"], "fi")

    return pxfile


def test_check_subkeys_values_fails_dimension_count():
    pxfile = _get_model()
    pxfile.cellnote.set("A cellnote", ["val2", "val2", "*", "bonus_dim"], "sv")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert "For keyword CELLNOTE: There are 3 dimensions, but 4 values. For lang:sv." in val_rep.error_msg


def test_check_subkeys_values_fails_no_such_value():
    pxfile = _get_model()
    pxfile.cellnote.set("A cellnote", ["val2", "val2", "no_such_value"], "sv")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert (
        "For keyword CELLNOTE: Cannot find item no_such_value in VALUES for vaiable:var3_sv and lang:sv."
        in val_rep.error_msg
    )


def test_check_subkeys_values_fails_none():
    pxfile = _get_model()
    pxfile.cellnote.set("A cellnote", None, "sv")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert "For keyword CELLNOTE: Values can not be None. For lang:sv." in val_rep.error_msg


def test_check_subkeys_for_precision_fails_variable_none():
    pxfile = _get_model()
    pxfile.precision.set(2, None, "val1", "fi")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert "For keyword PRECISION: Variable can not be None. For lang:fi." in val_rep.error_msg


def test_check_subkeys_for_precision_fails_variable_missing():
    pxfile = _get_model()
    pxfile.precision.set(2, "no_such_thing", "val1", "fi")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert (
        "For keyword PRECISION: Cannot find variable no_such_thing in stub + heading. For lang:fi." in val_rep.error_msg
    )


def test_check_subkeys_for_precision_fails_value_none():
    pxfile = _get_model()
    pxfile.precision.set(2, "var1_sv", None, "sv")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert "For keyword PRECISION: Need value for variable var1_sv. For lang:sv." in val_rep.error_msg


def test_check_subkeys_for_precision_fails_value_missing():
    pxfile = _get_model()
    pxfile.precision.set(2, "var1_sv", "no_such_thing", "sv")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert (
        "For keyword PRECISION: Cannot find item no_such_thing in VALUES for vaiable:var1_sv and lang:sv."
        in val_rep.error_msg
    )


def test_check_subkeys_fails_variable_none():
    pxfile = _get_model()
    pxfile.doublecolumn.set(True, None, "fi")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert "For keyword DOUBLECOLUMN: Variable can not be None. For lang:fi." in val_rep.error_msg


def test_check_subkeys_fails_variable_missing():
    pxfile = _get_model()
    pxfile.doublecolumn.set(True, "variable_missing", "fi")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert (
        "For keyword DOUBLECOLUMN: Cannot find variable variable_missing in stub + heading. For lang:fi."
        in val_rep.error_msg
    )


def test_check_subkeys_fails_content_none():
    pxfile = _get_model()
    pxfile.dayadj.set(True, None, "fi")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert "For keyword DAYADJ: Content value can not be None. For lang:fi." in val_rep.error_msg


def test_check_subkeys_fails_content_missing_from_values():
    pxfile = _get_model()
    pxfile.dayadj.set(True, "missing_cont_val", "fi")

    val_rep = check_valuebased_subkeys(pxfile)
    assert not val_rep.is_valid
    assert (
        "For keyword DAYADJ: Cannot find item missing_cont_val in VALUES for vaiable:var2_fi and lang:fi."
        in val_rep.error_msg
    )


def test_check_subkeys_ok():
    pxfile = _get_model()

    val_rep = check_valuebased_subkeys(pxfile)
    assert val_rep.is_valid
