from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_stub_and_heading import check_stub_and_heading


def test_check_stub_and_heading_one_missing_ok():
    pxfile = PXFileModel()
    pxfile.languages.set(["sv", "fi"])
    pxfile.stub.set(["var_sv"], "sv")
    pxfile.stub.set(["var_fi"], "fi")

    val_rep = check_stub_and_heading(pxfile)
    assert val_rep.is_valid


def test_check_stub_and_heading_the_other_missing_ok():
    pxfile = PXFileModel()
    pxfile.languages.set(["sv", "fi"])
    pxfile.heading.set(["var_sv"], "sv")
    pxfile.heading.set(["var_fi"], "fi")

    val_rep = check_stub_and_heading(pxfile)
    assert val_rep.is_valid


def test_check_stub_and_heading_fails_different_length():
    pxfile = PXFileModel()
    pxfile.languages.set(["sv", "fi"])

    pxfile.stub.set(["var_sv", "var2_sv"], "sv")
    pxfile.stub.set(["var_fi"], "fi")

    pxfile.heading.set(["var_sv", "var2_sv"], "sv")

    val_rep = check_stub_and_heading(pxfile)
    assert not val_rep.is_valid
    assert "Number of items in HEADING don't match when comparing language code: fi and sv." in val_rep.error_msg


def test_check_stub_and_heading_fails_both_missing():
    pxfile = PXFileModel()
    pxfile.languages.set(["no", "en", "fi"])

    val_rep = check_stub_and_heading(pxfile)
    assert not val_rep.is_valid
    assert 'For language code "fi": Neither STUB nor HEADING found.' in val_rep.error_msg
