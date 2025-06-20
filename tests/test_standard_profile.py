import json

import pytest

from dicom_deid.standard_profile import (
    DICOMStandard,
    Profile,
    apply_module_actions,
    apply_retired_attribute_actions,
)


@pytest.mark.parametrize(
    "module_usage,expected_action",
    (
        ("U", "X"),
        ("M", None),
        ("C", None),
    ),
)
def test_module_actions(module_usage, expected_action):

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
        ],
        ciods_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
                "usage": module_usage,
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
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action="K")

    apply_module_actions(
        profile=p,
        dicom_standard=ds,
    )

    json_profile = json.loads(p.to_json())
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(0000,0000)"]["action"]
        == expected_action
    )
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"] == "K"
    ), "Already set action is left alone"


def test_unsupported_usage_module_actions():

    ds = DICOMStandard(
        version="foo",
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
            },
        ],
        ciods_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
                "usage": "I AM UNSUPPORTED",
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
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with pytest.raises(ValueError, match="Unsupported module usage"):
        apply_module_actions(
            profile=p,
            dicom_standard=ds,
        )


@pytest.mark.parametrize(
    "retired_state,expected_action",
    (
        ("Y", "X"),
        ("N", None),
    ),
)
def test_retired_attributes(retired_state, expected_action):
    ds = DICOMStandard(
        version="foo",
        attributes=[
            {
                "tag": "(0000,0000)",
                "retired": retired_state,
            },
        ],
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
            },
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciods_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
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
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action="K")

    apply_retired_attribute_actions(
        profile=p,
        dicom_standard=ds,
    )

    json_profile = json.loads(p.to_json())
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(0000,0000)"]["action"]
        == expected_action
    )
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"] == "K"
    ), "Already set action is left alone"


def test_unknown_restired_state():
    ds = DICOMStandard(
        version="foo",
        attributes=[
            {
                "tag": "(0000,0000)",
                "retired": "I AM UNKOWN",
            },
        ],
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
            },
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciods_to_modules=[
            {
                "ciodId": "a-name",
                "moduleId": "mod0",
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
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with pytest.raises(ValueError, match="Unsupported attribute retired"):
        apply_retired_attribute_actions(
            profile=p,
            dicom_standard=ds,
        )
