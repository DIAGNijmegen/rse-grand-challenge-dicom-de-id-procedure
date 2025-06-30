import argparse
from pathlib import Path

from dicom_deid.checksum import sha256sum
from dicom_deid.procedure_generation import DICOMStandard, Procedure

action_lookup = {
    "D": "Replace with a non-zero length value that may be a "
    "dummy value and consistent with the VR (D)",
    "Z": "Replace with a zero length value, or a non-zero length "
    "value that may be a dummy value and consistent with the VR (Z)",
    "X": "Remove (X)",
    "K": "Keep (K)",
    "U": "Replace with a non-zero length UID that is internally "
    "consistent within a set of Instances",
    "R": "Reject the entire DICOM file (R)",
}


def render_action(dicom_standard: DICOMStandard, tag, action, sop_id):

    justification = action.get("justification", "N/A")
    action_info = []
    desc = action_lookup[action["default"]]
    action_info.append(f":Action: {desc}")
    action_info.append(f":Justication: {justification}")

    return dicom_standard.render_attribute_info(
        tag=tag, sop_id=sop_id, headers=action_info
    )


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
    final_json = p.to_json(
        sort_keys=True,
        separators=(",", ":"),
    )
    procedure_path = args.output / "procedure.json"
    with open(procedure_path, "w") as f:
        f.write(final_json)

    # Ensure a checksum gets added
    sha256sum(procedure_path)

    # Generate human-readable format

    ds = DICOMStandard.from_path(args.dicom_standard)
    description = []
    for sop_id in p.sop_ids:
        description.append("=" * len(sop_id))
        description.append(sop_id)
        description.append("=" * len(sop_id))
        description.append("\n")

        for tag, action in p.get_sop_actions(sop_id).items():
            render = render_action(ds, tag, action, sop_id)
            description.append(render + "\n\n\n")

        description.append("\n")

        with open(args.output / "human-readable-procedure.rts", "w") as f:
            f.writelines(description)


if __name__ == "__main__":
    main()
