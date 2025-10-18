import pytest

from dicom_deid.procedure_cleanup import (
    find_unreachable_nodes,
    remove_unreachable_actions,
)
from dicom_deid.procedure_generation import ActionChoices, DICOMStandard, Procedure


@pytest.mark.parametrize(
    "description, edges, breaking_nodes, expected_redundants",
    (
        (
            "All empy",
            [],
            set(),
            set(),
        ),
        (
            "No paths, no breaks",
            [
                ["1"],
                ["2"],
            ],
            set(),
            set(),
        ),
        (
            "No paths, breaks",
            [
                ["1"],
                ["2"],
            ],
            {"1", "2"},
            set(),
        ),
        (
            "2 is redundant because parent 1 is breaking",
            [
                ["1"],
                ["1", "2"],
            ],
            {"1"},
            {"2"},
        ),
        (
            "3 is redundant, because both parents are breaking",
            [
                ["1"],
                ["2"],
                ["1", "3"],
                ["2", "3"],
            ],
            {"1", "2"},
            {"3"},
        ),
        (
            "3 is not redundant because 1 parent is not breaking",
            [
                ["1"],
                ["2"],
                ["1", "3"],
                ["2", "3"],
            ],
            {"1"},
            set(),
        ),
        (
            "3 is not redundant because it has a root",
            [
                ["1"],
                ["2"],
                ["3"],
                ["1", "3"],
                ["2", "3"],
            ],
            {"1"},
            set(),
        ),
        (
            "Super deep, loads of redundant",
            [
                ["1"],
                ["1", "2"],
                ["1", "2", "3"],
                ["1", "2", "3", "4"],
                ["1", "2", "3", "4", "5"],
                ["1", "2", "3", "4", "6"],
                ["9"],
                ["9", "4"],
                ["9", "4", "5"],
                ["9", "4", "6"],
            ],
            {"1", "4"},
            {"2", "3", "5", "6"},
        ),
        (
            "Super deep, but 5 and 6 are rooted and hence not redundant",
            [
                ["1"],
                ["1", "2"],
                ["1", "2", "3"],
                ["1", "2", "3", "4"],
                ["1", "2", "3", "4", "5"],
                ["1", "2", "3", "4", "6"],
                ["9"],
                ["9", "4"],
                ["9", "4", "5"],
                ["9", "4", "6"],
                # These make 5 and 6 not redundant
                ["5"],
                ["6"],
            ],
            {"1", "4"},
            {"2", "3"},
        ),
        (
            "2 is both breaking and redundant",
            [
                ["1"],
                ["1", "2"],
                ["1", "2", "3"],
            ],
            {"1", "2"},
            {"2", "3"},
        ),
    ),
)
def test_find_unreachable_nodes(
    description, edges, breaking_nodes, expected_redundants
):
    assert (
        find_unreachable_nodes(edges, breaking_nodes) == expected_redundants
    ), description


@pytest.mark.parametrize(
    "sequence_action, within_sequence_tag_action_removed",
    (
        (ActionChoices.REMOVE, True),
        (ActionChoices.REJECT, True),
        (ActionChoices.REPLACE, True),
        (ActionChoices.REPLACE_0, True),
        (ActionChoices.KEEP, False),
    ),
)
def test_remove_unreachable_actions(
    sequence_action, within_sequence_tag_action_removed
):
    ds = DICOMStandard(
        module_to_attributes=[
            {
                "moduleId": "mod0",
                "path": "mod0:00000000",
                "tag": "(0000,0000)",
                "type": "SQ",
            },
            {
                "moduleId": "mod0",
                "path": "mod0:00000000:1111111a",  # Note the sneaky lower-case 'a'
                "tag": "(1111,111a)",
                "type": "SH",
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
    p.set_action(sop_id="1.1", tag="(0000,0000)", action=sequence_action)
    p.set_action(sop_id="1.1", tag="(1111,111A)", action=None)

    remove_unreachable_actions(procedure=p, dicom_standard=ds)
    actions = p.get_sop_actions(sop_id="1.1")

    if within_sequence_tag_action_removed:
        assert "(1111,111A)" not in actions
    else:
        assert "(1111,111A)" in actions
