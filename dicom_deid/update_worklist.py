import argparse
from collections import defaultdict
from pathlib import Path

from dicom_deid.procedure_generation import DICOMStandard, Procedure
from dicom_deid.render import render_attribute_info


def main():
    parser = argparse.ArgumentParser(
        description="Generate a reStructuredText worklist for unset actions"
    )
    parser.add_argument(
        "--dicom-standard",
        type=Path,
        required=True,
        help="Directory containing DICOM standard files",
    )
    parser.add_argument(
        "--candidate",
        type=Path,
        required=True,
        help="Candidate procedure file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output path for the manual worklist",
    )
    args = parser.parse_args()

    with open(args.candidate, "r") as f:
        candidate_profile = Procedure.from_json(f.read())

    ds = DICOMStandard.from_path(args.dicom_standard)

    worklist = []
    unset = defaultdict(list)
    for tag, sop_id in candidate_profile.get_unset_action_tags_in_sops():
        unset[sop_id].append(tag)

    for sop_id in unset:
        worklist.append(sop_id)
        worklist.append("=" * len(sop_id))
        worklist.append("\n")

        for tag in unset[sop_id]:
            render = render_attribute_info(dicom_standard=ds, tag=tag, sop_id=sop_id)
            worklist.append(render)

        worklist.append("\n")

    with open(args.output / "WORKLIST.rst", "w") as f:
        f.write("\n".join(worklist))


if __name__ == "__main__":
    main()
