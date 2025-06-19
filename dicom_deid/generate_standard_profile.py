import argparse
from pathlib import Path

from dicom_deid.standard_profile import generate_standard_profile


def main():
    parser = argparse.ArgumentParser(
        description="Generate a standard DICOM de-identification profile"
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

    generate_standard_profile(
        dicom_standard_path=args.dicom_standard,
        output_path=args.output,
    )


if __name__ == "__main__":
    main()
