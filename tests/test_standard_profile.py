import json
from contextlib import nullcontext as does_not_raise

import pytest

from dicom_deid.standard_profile import (
    DICOMStandard,
    Profile,
    apply_attribute_type_actions,
    apply_basic_dicom_deid_profile_actions,
    apply_module_actions,
    apply_retired_attribute_actions,
)


@pytest.mark.parametrize(
    "module_usage,expected_action",
    (
        ("U", Profile.Action.REMOVE),
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
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

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
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"]
        == p.Action.KEEP
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
        ("Y", Profile.Action.REMOVE),
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
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

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
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"]
        == p.Action.KEEP
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


@pytest.mark.parametrize(
    "basic_profile_value,expected_action",
    (
        ("D", Profile.Action.REPLACE),
        ("Z", Profile.Action.REPLACE0),
        ("X", Profile.Action.REMOVE),
        ("K", Profile.Action.KEEP),
        ("C", Profile.Action.CLEAN),
        ("U", Profile.Action.UID),
    ),
)
def test_basic_dicom_deid_profile_actions(basic_profile_value, expected_action):
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
        confidentiality_profile_attributes=[
            {
                "tag": "(0000,0000)",
                "basicProfile": basic_profile_value,
            },
        ],
    )
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_basic_dicom_deid_profile_actions(
        profile=p,
        dicom_standard=ds,
    )

    json_profile = json.loads(p.to_json())
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(0000,0000)"]["action"]
        == expected_action
    )
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"]
        == p.Action.KEEP
    ), "Already set action is left alone"


@pytest.mark.parametrize(
    "basic_profile_value,type_value,expected_action",
    [
        # Z/D
        ("Z/D", "1", Profile.Action.REPLACE),
        ("Z/D", "1C", Profile.Action.REPLACE),
        ("Z/D", "2", Profile.Action.REPLACE0),
        ("Z/D", "2C", Profile.Action.REPLACE0),
        ("Z/D", "3", Profile.Action.REMOVE),
        # X/Z
        ("X/Z", "1", Profile.Action.REPLACE),
        ("X/Z", "1C", Profile.Action.REPLACE),
        ("X/Z", "2", Profile.Action.REPLACE0),
        ("X/Z", "2C", Profile.Action.REPLACE0),
        ("X/Z", "3", Profile.Action.REMOVE),
        # X/D
        ("X/D", "1", Profile.Action.REPLACE),
        ("X/D", "1C", Profile.Action.REPLACE),
        ("X/D", "2", Profile.Action.REPLACE0),
        ("X/D", "2C", Profile.Action.REPLACE0),
        ("X/D", "3", Profile.Action.REMOVE),
        # "X/Z/D"
        ("X/Z/D", "1", Profile.Action.REPLACE),
        ("X/Z/D", "1C", Profile.Action.REPLACE),
        ("X/Z/D", "2", Profile.Action.REPLACE0),
        ("X/Z/D", "2C", Profile.Action.REPLACE0),
        ("X/Z/D", "3", Profile.Action.REMOVE),
        # X/Z/U
        ("X/Z/U*", "1", Profile.Action.UID),
        ("X/Z/U*", "1C", Profile.Action.UID),
        ("X/Z/U*", "2", Profile.Action.REPLACE0),
        ("X/Z/U*", "2C", Profile.Action.REPLACE0),
        ("X/Z/U*", "3", Profile.Action.REMOVE),
    ],
)
def test_basic_dicom_deid_profile_actions_types(
    basic_profile_value, type_value, expected_action
):
    ds = DICOMStandard(
        version="foo",
        macro_to_attributes=[
            {
                "tag": "(0000,0000)",
                "type": type_value,
            },
        ],
        attributes=[
            {
                "tag": "(0000,0000)",
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
        confidentiality_profile_attributes=[
            {
                "tag": "(0000,0000)",
                "basicProfile": basic_profile_value,
            },
        ],
    )
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_basic_dicom_deid_profile_actions(
        profile=p,
        dicom_standard=ds,
    )

    json_profile = json.loads(p.to_json())
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(0000,0000)"]["action"]
        == expected_action
    )
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"]
        == p.Action.KEEP
    ), "Already set action is left alone"


@pytest.mark.parametrize(
    "basic_profile_value,type_value,expectation",
    [
        (
            "Z/D",
            "1",
            does_not_raise(),
        ),
        (
            "I DO NOT EXIST",
            "1",
            pytest.raises(ValueError, match="Unsupported confidentiality action"),
        ),
        (
            "Z/D",
            "I DO NOT EXIST",
            pytest.raises(ValueError, match="Unsupported confidentiality action"),
        ),
    ],
)
def test_basic_dicom_deid_unsupported_type_and_basic_profile(
    basic_profile_value, type_value, expectation
):
    ds = DICOMStandard(
        version="foo",
        macro_to_attributes=[
            {
                "tag": "(0000,0000)",
                "type": type_value,
            },
        ],
        attributes=[
            {
                "tag": "(0000,0000)",
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
        confidentiality_profile_attributes=[
            {
                "tag": "(0000,0000)",
                "basicProfile": basic_profile_value,
            },
        ],
    )
    p = Profile()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with expectation:
        apply_basic_dicom_deid_profile_actions(
            profile=p,
            dicom_standard=ds,
        )


@pytest.mark.parametrize(
    "attribute_type,expected_action",
    (
        ("1", Profile.Action.KEEP),
        ("1C", None),
        ("2", Profile.Action.REPLACE0),
        ("2C", None),
        ("3", Profile.Action.REMOVE),
    ),
)
def test_attribute_type_actions(attribute_type, expected_action):
    ds = DICOMStandard(
        version="foo",
        macro_to_attributes=[
            {
                "tag": "(0000,0000)",
                "type": attribute_type,
            },
        ],
        attributes=[
            {
                "tag": "(0000,0000)",
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
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_attribute_type_actions(
        profile=p,
        dicom_standard=ds,
    )

    json_profile = json.loads(p.to_json())
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(0000,0000)"]["action"]
        == expected_action
    )
    assert (
        json_profile["SOPClassUID"]["1.1"]["tag"]["(1111,1111)"]["action"]
        == p.Action.KEEP
    ), "Already set action is left alone"


@pytest.mark.parametrize(
    "attribute_type,expectation",
    [
        (
            "1",
            does_not_raise(),
        ),
        (
            "I DO NOT EXIST",
            pytest.raises(ValueError, match="Unsupported attribute type"),
        ),
    ],
)
def test_attribute_type_actions_unsupported_type(attribute_type, expectation):
    ds = DICOMStandard(
        version="foo",
        macro_to_attributes=[
            {
                "tag": "(0000,0000)",
                "type": attribute_type,
            },
        ],
        attributes=[
            {
                "tag": "(0000,0000)",
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

    with expectation:
        apply_attribute_type_actions(
            profile=p,
            dicom_standard=ds,
        )
