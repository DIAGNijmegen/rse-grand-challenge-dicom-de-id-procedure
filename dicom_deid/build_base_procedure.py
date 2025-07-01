import argparse
from pathlib import Path

from dicom_deid.procedure_generation import generate_base_procedure


def main():
    parser = argparse.ArgumentParser(
        description="Generate a base DICOM de-identification procedure"
    )
    parser.add_argument(
        "--dicom-standard",
        type=Path,
        required=True,
        help="Directory containing DICOM standard files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output path for the standard profile",
    )
    args = parser.parse_args()

    base = generate_base_procedure(
        dicom_standard_path=args.dicom_standard,
    )
    base_json = base.to_json(indent=4)

    with open(args.output, "w") as f:
        f.write(base_json)


if __name__ == "__main__":
    main()
