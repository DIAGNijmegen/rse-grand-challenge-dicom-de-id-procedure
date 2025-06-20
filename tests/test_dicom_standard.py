import os
from contextlib import nullcontext as does_not_raise
from pathlib import Path

import pytest

from dicom_deid.standard_profile import DICOMStandard, DICOMStandardError

TEST_RESOURCES = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


def test_dicom_standard():
    ds = DICOMStandard(
        version="foo",
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
            },
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
            {
                "moduleId": "mod1",
                "tag": "(2222,2222)",
            },
        ],
        ciods_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
            },
            {
                "ciodId": "another-name",
                "moduleId": "mod0",
            },
            {
                "ciodId": "another-name",
                "moduleId": "mod1",
            },
        ],
        sops=[
            {
                "id": "1.1",
                "ciod": "A Name",
            },
            {
                "id": "2.2",
                "ciod": "Another Name",
            },
        ],
        ciods=[
            {
                "name": "A Name",
                "id": "a-name",
            },
            {
                "name": "Another Name",
                "id": "another-name",
            },
        ],
    )

    # SOP => TAGS
    assert ds.map_sop_to_tags("1.1") == {"(0000,0000)", "(1111,1111)"}
    assert ds.map_sop_to_tags("2.2") == {"(0000,0000)", "(1111,1111)", "(2222,2222)"}

    # TAG => MODULE
    assert ds.get_module_via_tag("(0000,0000)", sop_id="1.1")["moduleId"] == "mod0"

    assert ds.get_module_via_tag("(2222,2222)", sop_id="2.2")["moduleId"] == "mod1"


def test_dicom_standard_module_clash():
    ds = DICOMStandard(
        version="foo",
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
            },
            {
                "moduleId": "mod1",
                "tag": "(0000,0000)",
            },
        ],
        ciods_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
            },
            {
                "ciodId": "a-name",
                "moduleId": "mod1",
            },
        ],
        sops=[
            {
                "id": "1.1",
                "ciod": "A Name",
            },
        ],
        ciods=[
            {
                "name": "A Name",
                "id": "a-name",
            },
        ],
    )

    with pytest.raises(
        DICOMStandardError, match=r"Tag \(0000,0000\) belongs to 2 modules"
    ):
        # Tag belongs to two different modules, in the same SOP
        ds.get_module_via_tag("(0000,0000)", sop_id="1.1")


@pytest.mark.parametrize(
    "ciods_to_modules,expectation",
    [
        (
            [
                {"ciodId": "a-name", "moduleId": "mod0", "usage": "C"},
                {"ciodId": "another-name", "moduleId": "mod0", "usage": "C"},
            ],
            does_not_raise(),
        ),
        (
            [
                {"ciodId": "a-name", "moduleId": "mod0", "usage": "C"},
                {"ciodId": "another-name", "moduleId": "mod0", "usage": "U"},
            ],
            pytest.raises(
                DICOMStandardError,
                match="Inconsistent definitions found for module",
            ),
        ),
    ],
)
def test_dicom_standard_inconsistent_modules(ciods_to_modules, expectation):
    with expectation:
        DICOMStandard(
            version="foo",
            module_to_attributes=[],
            ciods_to_modules=ciods_to_modules,
            sops=[],
            ciods=[],
        )


def test_from_path():
    ds = DICOMStandard.from_path(TEST_RESOURCES / "dicom_standard")

    assert ds.version == "test"

    assert ds.map_sop_to_tags("1.1") == {"(0000,0000)", "(1111,1111)"}
    assert ds.map_sop_to_tags("2.2") == {"(0000,0000)", "(1111,1111)", "(2222,2222)"}

    assert ds.get_module_via_tag("(0000,0000)", sop_id="1.1")["moduleId"] == "mod0"

    assert ds.get_module_via_tag("(2222,2222)", sop_id="2.2")["moduleId"] == "mod1"
