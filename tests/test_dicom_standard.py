import os
from pathlib import Path

from dicom_deid.procedure_generation import DICOMStandard

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
        ciod_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
                "usage": "U",
            },
            {
                "ciodId": "another-name",
                "moduleId": "mod0",
                "usage": "M",
            },
            {
                "ciodId": "another-name",
                "moduleId": "mod1",
                "usage": "C",
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
    assert ds.get_module_usages_via_tag("(0000,0000)", sop_id="1.1") == {"U"}
    assert ds.get_module_usages_via_tag("(2222,2222)", sop_id="2.2") == {"C"}


def test_from_path():
    ds = DICOMStandard.from_path(TEST_RESOURCES / "dicom_standard")

    assert ds.version == "test"

    assert ds.map_sop_to_tags("1.1") == {"(0000,0000)", "(1111,1111)"}
    assert ds.map_sop_to_tags("2.2") == {"(0000,0000)", "(1111,1111)", "(2222,2222)"}

    assert ds.get_module_usages_via_tag("(0000,0000)", sop_id="1.1") == {"U"}

    assert ds.get_module_usages_via_tag("(2222,2222)", sop_id="2.2") == {"C"}
