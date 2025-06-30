import argparse
from pathlib import Path

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

    candidate = base + manual

    candidate_json = candidate.to_json(indent=4, sort_keys=True)

    with open(args.output, "w") as f:
        f.write(candidate_json)

    generate_human_readable_format(
        output=args.output.parent / "manual-human",
        dicom_standard=DICOMStandard.from_path(args.dicom_standard),
        procedure=manual,
    )


if __name__ == "__main__":
    main()
