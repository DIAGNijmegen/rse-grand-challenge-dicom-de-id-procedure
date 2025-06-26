import argparse
from pathlib import Path

from dicom_deid.standard_profile import Profile


def main():
    parser = argparse.ArgumentParser(
        description="Generate a candidate DICOM de-identification procedure"
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
        base_profile = Profile.from_json(f.read())

    with open(args.manual, "r") as f:
        manual_profile = Profile.from_json(f.read())

    candidate_profile = base_profile + manual_profile

    candidate_profile_json = candidate_profile.to_json(indent=4)

    with open(args.output, "w") as f:
        f.write(candidate_profile_json)


if __name__ == "__main__":
    main()
