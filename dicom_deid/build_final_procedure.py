import argparse
from pathlib import Path

from dicom_deid.checksum import sha256sum
from dicom_deid.procedure_generation import Procedure


def main():
    parser = argparse.ArgumentParser(
        description="Generate a candidate DICOM de-identification procedure"
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
    final_json = p.to_json(
        sort_keys=True,
        separators=(",", ":"),
    )

    procedure_path = args.output / "procedure.json"
    with open(procedure_path, "w") as f:
        f.write(final_json)

    sha256sum(procedure_path)


if __name__ == "__main__":
    main()
