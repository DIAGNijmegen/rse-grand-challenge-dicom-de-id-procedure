import argparse
from pathlib import Path

from dicom_deid.procedure_cleanup import remove_unreachable_actions
from dicom_deid.procedure_generation import DICOMStandard, Procedure
from dicom_deid.render import generate_human_readable_format


def main():
    parser = argparse.ArgumentParser(
        description="Generate a candidate DICOM de-identification procedure"
    )
    parser.add_argument(
        "--dicom-standard",
        type=Path,
        required=True,
        help="Directory containing DICOM standard files",
    )
    parser.add_argument(
        "--base",
        type=Path,
        required=True,
        help="Base procedure file",
    )
    parser.add_argument(
        "--manual",
        type=Path,
        required=True,
        help="Manual procedure file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output path for the candidate profile",
    )
    args = parser.parse_args()

    with open(args.base, "r") as f:
        base = Procedure.from_json(f.read())

    with open(args.manual, "r") as f:
        manual = Procedure.from_json(f.read())

    # Validate manual: it should not have additional actions base
    # does not prescribe

    for sop_id in manual.sop_ids:
        manual_actions = manual.get_sop_actions(sop_id=sop_id)
        base_actions = base.get_sop_actions(sop_id=sop_id)
        extra_tags = set(manual_actions.keys()) - set(base_actions.keys())

        if extra_tags:
            raise ValueError(
                f"Manual override has unexpected tags for {sop_id=}: {extra_tags}"
            )

    candidate = base + manual

    dicom_standard = DICOMStandard.from_path(args.dicom_standard)

    remove_unreachable_actions(procedure=candidate, dicom_standard=dicom_standard)

    # Loop unreachables action removal back to manual
    candidate_json = candidate.to_json(indent=4, sort_keys=True)

    with open(args.output, "w") as f:
        f.write(candidate_json)

    generate_human_readable_format(
        output=args.output.parent / "manual-human",
        dicom_standard=dicom_standard,
        procedure=manual,
    )


if __name__ == "__main__":
    main()
