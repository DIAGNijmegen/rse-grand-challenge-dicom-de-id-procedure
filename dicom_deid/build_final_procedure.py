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
        "--candidate",
        type=Path,
        required=True,
        help="Candidate procedure file",
    )
    parser.add_argument(
        "--version",
        type=str,
        required=True,
        help="Version of the final procedure",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for the distributable files",
    )
    args = parser.parse_args()

    with open(args.candidate, "r") as f:
        p = Procedure.from_json(f.read())

    # Set version
    p._procedure["version"] = args.version

    # Minify version
    final_mini_json = p.to_json(
        sort_keys=True,
        separators=(",", ":"),
    )

    # Min version
    procedure_min_path = args.output / "procedure.min.json"
    with open(procedure_min_path, "w") as f:
        f.write(final_mini_json)

    generate_human_readable_format(
        output=args.output / "human",
        dicom_standard=DICOMStandard.from_path(args.dicom_standard),
        procedure=p,
    )


if __name__ == "__main__":
    main()
