import json
from contextlib import nullcontext as does_not_raise

import pytest

from dicom_deid.procedure_generation import (
    DICOMStandard,
    Procedure,
    apply_attribute_type_actions,
    apply_basic_dicom_deid_profile_actions,
    apply_module_actions,
    apply_retired_attribute_actions,
)


@pytest.mark.parametrize(
    "module_usages,expected_action",
    (
        (["U"], Procedure.Action.REMOVE),
        (["M"], None),
        (["C"], None),
        # Multiple, same
        (["U"] * 2, Procedure.Action.REMOVE),
        (["M"] * 2, None),
        (["C"] * 2, None),
        # Multiple, different
        (["U", "M"], None),
        (["M", "C"], None),
        (["C", "M"], None),
    ),
)
def test_module_actions(module_usages, expected_action):

    ds = DICOMStandard(
        version="foo",
        module_to_attributes=[
            *(
                {
                    "moduleId": f"mod{i}",
                    "tag": "(0000,0000)",
                }
                for i in range(len(module_usages))
            ),
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciod_to_modules=[
            *(
                {
                    "ciodId": "a-name",
                    "moduleId": f"mod{idx}",
                    "usage": usage,
                }
                for idx, usage in enumerate(module_usages)
            )
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_module_actions(
        procedure=p,
        dicom_standard=ds,
    )

    procedure_json = json.loads(p.to_json())
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(0000,0000)"]["default"]
        == expected_action
    )
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(1111,1111)"]["default"]
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
        ciod_to_modules=[
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with pytest.raises(ValueError, match="Unsupported module usage"):
        apply_module_actions(
            procedure=p,
            dicom_standard=ds,
        )


@pytest.mark.parametrize(
    "retired_state,expected_action",
    (
        ("Y", Procedure.Action.REMOVE),
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
        ciod_to_modules=[
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_retired_attribute_actions(
        procedure=p,
        dicom_standard=ds,
    )

    procedure_json = json.loads(p.to_json())
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(0000,0000)"]["default"]
        == expected_action
    )
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(1111,1111)"]["default"]
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
        ciod_to_modules=[
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with pytest.raises(ValueError, match="Unsupported attribute retired"):
        apply_retired_attribute_actions(
            procedure=p,
            dicom_standard=ds,
        )


@pytest.mark.parametrize(
    "basic_profile_value,expected_action",
    (
        ("D", Procedure.Action.REPLACE),
        ("Z", Procedure.Action.REPLACE_0),
        ("X", Procedure.Action.REMOVE),
        ("K", Procedure.Action.KEEP),
        ("U", Procedure.Action.UID),
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
        ciod_to_modules=[
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)
    p.set_action(
        sop_id="1.1", tag="(2222,2222)", action=None
    )  # No confidentiality profile set

    apply_basic_dicom_deid_profile_actions(
        procedure=p,
        dicom_standard=ds,
    )

    procedure_json = json.loads(p.to_json())
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(0000,0000)"]["default"]
        == expected_action
    )
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(1111,1111)"]["default"]
        == p.Action.KEEP
    ), "Already set action is left alone"


@pytest.mark.parametrize(
    "basic_profile_value,attribute_types,expected_action",
    [
        # Z/D
        ("Z/D", ["1"], Procedure.Action.REPLACE),
        ("Z/D", ["1C"], None),
        ("Z/D", ["2"], Procedure.Action.REPLACE_0),
        ("Z/D", ["2C"], None),
        ("Z/D", ["3"], Procedure.Action.REMOVE),
        ("Z/D", ["None"], None),
        # X/Z
        ("X/Z", ["1"], Procedure.Action.REPLACE),
        ("X/Z", ["1C"], None),
        ("X/Z", ["2"], Procedure.Action.REPLACE_0),
        ("X/Z", ["2C"], None),
        ("X/Z", ["3"], Procedure.Action.REMOVE),
        ("X/Z", ["None"], None),
        # X/D
        ("X/D", ["1"], Procedure.Action.REPLACE),
        ("X/D", ["1C"], None),
        ("X/D", ["2"], Procedure.Action.REPLACE_0),
        ("X/D", ["2C"], None),
        ("X/D", ["3"], Procedure.Action.REMOVE),
        ("X/D", ["None"], None),
        # "X/Z/D"
        ("X/Z/D", ["1"], Procedure.Action.REPLACE),
        ("X/Z/D", ["1C"], None),
        ("X/Z/D", ["2"], Procedure.Action.REPLACE_0),
        ("X/Z/D", ["2C"], None),
        ("X/Z/D", ["3"], Procedure.Action.REMOVE),
        ("X/Z/D", ["None"], None),
        # X/Z/U
        ("X/Z/U*", ["1"], Procedure.Action.UID),
        ("X/Z/U*", ["1C"], None),
        ("X/Z/U*", ["2"], Procedure.Action.REPLACE_0),
        ("X/Z/U*", ["2C"], None),
        ("X/Z/U*", ["3"], Procedure.Action.REMOVE),
        ("X/Z/U*", ["None"], None),
        # Multiple types, same
        ("Z/D", ["1"] * 2, Procedure.Action.REPLACE),
        ("Z/D", ["1C"] * 2, None),
        ("Z/D", ["2"] * 2, Procedure.Action.REPLACE_0),
        ("Z/D", ["2C"] * 2, None),
        ("Z/D", ["3"] * 2, Procedure.Action.REMOVE),
        ("Z/D", ["None"] * 2, None),
        # Multiple types, but different
        ("Z/D", ["1", "1C"], None),
        ("Z/D", ["1C", "3"], None),
        ("Z/D", ["2", "1"], None),
        ("Z/D", ["2C", "3"], None),
        ("Z/D", ["3", "1"], None),
        ("Z/D", ["None", "1"], None),
    ],
)
def test_basic_dicom_deid_profile_actions_types(
    basic_profile_value, attribute_types, expected_action
):
    ds = DICOMStandard(
        version="foo",
        attributes=[
            {
                "tag": "(0000,0000)",
            },
        ],
        module_to_attributes=[
            *(
                {
                    "moduleId": f"mod{i}",
                    "tag": "(0000,0000)",
                    "type": t,
                }
                for i, t in enumerate(attribute_types)
            ),
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciod_to_modules=[
            {
                "moduleId": f"mod{i}",
                "ciodId": "a-name",
            }
            for i in range(len(attribute_types))
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_basic_dicom_deid_profile_actions(
        procedure=p,
        dicom_standard=ds,
    )

    procedure_json = json.loads(p.to_json())
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(0000,0000)"]["default"]
        == expected_action
    )
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(1111,1111)"]["default"]
        == p.Action.KEEP
    ), "Already set action is left alone"


@pytest.mark.parametrize(
    "basic_profile_value,attribute_type,expectation",
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
    basic_profile_value, attribute_type, expectation
):
    ds = DICOMStandard(
        version="foo",
        attributes=[
            {
                "tag": "(0000,0000)",
            },
        ],
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
                "type": attribute_type,
            },
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciod_to_modules=[
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with expectation:
        apply_basic_dicom_deid_profile_actions(
            procedure=p,
            dicom_standard=ds,
        )


@pytest.mark.parametrize(
    "attribute_types,expected_action",
    (
        #
        # Singular
        (["1"], Procedure.Action.KEEP),
        (["1C"], None),
        (["2"], Procedure.Action.REPLACE_0),
        (["2C"], None),
        (["3"], Procedure.Action.REMOVE),
        #
        # Multiple, but same
        (["1"] * 2, Procedure.Action.KEEP),
        (["1C"] * 2, None),
        (["2"] * 2, Procedure.Action.REPLACE_0),
        (["2C"] * 2, None),
        (["3"] * 2, Procedure.Action.REMOVE),
        #
        # Multiple, but different
        (["1", "1C"], None),
        (["2", "2C"], None),
        (["2C", "3"], None),
        (["3", "2"], None),
    ),
)
def test_attribute_type_actions(attribute_types, expected_action):
    ds = DICOMStandard(
        version="foo",
        attributes=[
            {
                "tag": "(0000,0000)",
            },
        ],
        module_to_attributes=[
            *(
                {
                    "moduleId": f"mod{i}",
                    "tag": "(0000,0000)",
                    "type": attr_type,
                }
                for i, attr_type in enumerate(attribute_types)
            ),
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciod_to_modules=[
            *(
                {
                    "ciodId": "a-name",
                    "moduleId": f"mod{i}",
                }
                for i in range(len(attribute_types))
            ),
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)
    p.set_action(sop_id="1.1", tag="(1111,1111)", action=p.Action.KEEP)

    apply_attribute_type_actions(
        procedure=p,
        dicom_standard=ds,
    )

    procedure_json = json.loads(p.to_json())
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(0000,0000)"]["default"]
        == expected_action
    )
    assert (
        procedure_json["sopClass"]["1.1"]["tag"]["(1111,1111)"]["default"]
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
        attributes=[
            {
                "tag": "(0000,0000)",
            },
        ],
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "tag": "(0000,0000)",
                "type": attribute_type,
            },
            {
                "moduleId": "mod0",
                "tag": "(1111,1111)",
            },
        ],
        ciod_to_modules=[
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
    p = Procedure()
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=None)

    with expectation:
        apply_attribute_type_actions(
            procedure=p,
            dicom_standard=ds,
        )
