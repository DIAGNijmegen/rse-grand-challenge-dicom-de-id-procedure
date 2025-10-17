import pytest

from dicom_deid.procedure_cleanup import find_redundant_nodes


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
                {"path": "module:1"},
                {"path": "module:2"},
            ],
            set(),
            set(),
        ),
        (
            "No paths, breaks",
            [
                {"path": "module:1"},
                {"path": "module:2"},
            ],
            {"1", "2"},
            set(),
        ),
        (
            "2 is redundant because parent 1 is breaking",
            [
                {"path": "module:1"},
                {"path": "module:1:2"},
            ],
            {"1"},
            {"2"},
        ),
        (
            "3 is redundant, because both parents are breaking",
            [
                {"path": "module:1"},
                {"path": "module:2"},
                {"path": "module:1:3"},
                {"path": "module:2:3"},
            ],
            {"1", "2"},
            {"3"},
        ),
        (
            "3 is not redundant because 1 parent is not breaking",
            [
                {"path": "module:1"},
                {"path": "module:2"},
                {"path": "module:1:3"},
                {"path": "module:2:3"},
            ],
            {"1"},
            set(),
        ),
        (
            "3 is not redundant because it has a root",
            [
                {"path": "module:1"},
                {"path": "module:2"},
                {"path": "module:3"},
                {"path": "module:1:3"},
                {"path": "module:2:3"},
            ],
            {"1"},
            set(),
        ),
        (
            "Super deep, loads of redundant",
            [
                {"path": "module:1"},
                {"path": "module:1:2"},
                {"path": "module:1:2:3"},
                {"path": "module:1:2:3:4"},
                {"path": "module:1:2:3:4:5"},
                {"path": "module:1:2:3:4:6"},
                {"path": "module:9"},
                {"path": "module:9:4"},
                {"path": "module:9:4:5"},
                {"path": "module:9:4:6"},
            ],
            {"1", "4"},
            {"2", "3", "5", "6"},
        ),
        (
            "Super deep, but 5 and 6 are rooted and hence not redundant",
            [
                {"path": "module:1"},
                {"path": "module:1:2"},
                {"path": "module:1:2:3"},
                {"path": "module:1:2:3:4"},
                {"path": "module:1:2:3:4:5"},
                {"path": "module:1:2:3:4:6"},
                {"path": "module:9"},
                {"path": "module:9:4"},
                {"path": "module:9:4:5"},
                {"path": "module:9:4:6"},
                # These make 5 and 6 not redundant
                {"path": "module:5"},
                {"path": "module:6"},
            ],
            {"1", "4"},
            {"2", "3"},
        ),
        (
            "2 is both breaking and redundant",
            [
                {"path": "module:1"},
                {"path": "module:1:2"},
                {"path": "module:1:2:3"},
            ],
            {"1", "2"},
            {"2", "3"},
        ),
    ),
)
def test_find_redundant_nodes(description, edges, breaking_nodes, expected_redundants):
    assert (
        find_redundant_nodes(edges, breaking_nodes) == expected_redundants
    ), description
