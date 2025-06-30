import argparse
from pathlib import Path

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

    # Clear all non-reject justifications
    for sop_id in p.sop_ids:
        for action in p._procedure["sopClass"][sop_id]["tag"].values():
            if "justification" in action:
                if action["default"] != p.Action.REJECT:
                    del action["justification"]

    # Set version
    p._procedure["version"] = args.version

    # Minify version
    final_json = p.to_json(
        sort_keys=True,
        separators=(",", ":"),
    )

    with open(args.output / "procedure.json", "w") as f:
        f.write(final_json)


if __name__ == "__main__":
    main()
