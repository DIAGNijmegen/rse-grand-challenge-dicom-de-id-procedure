import argparse
from pathlib import Path

from dicom_deid.standard_profile import generate_standard_profile


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

    profile = generate_standard_profile(
        dicom_standard_path=args.dicom_standard,
    )
    json_profile = profile.to_json(indent=4)

    with open(args.output, "w") as f:
        f.write(json_profile)


if __name__ == "__main__":
    main()
