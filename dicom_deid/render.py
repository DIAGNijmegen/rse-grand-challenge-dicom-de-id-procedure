import textwrap
from pathlib import Path

from bs4 import BeautifulSoup

from dicom_deid.procedure_generation import DICOMStandard, Procedure

verbose_action = {
    "D": "Replace with a non-zero length value that may be a "
    "dummy value and consistent with the VR (D)",
    "Z": "Replace with a zero length value, or a non-zero length "
    "value that may be a dummy value and consistent with the VR (Z)",
    "X": "Remove (X)",
    "K": "Keep (K)",
    "U": "Replace with a non-zero length UID that is internally "
    "consistent within a set of Instances (U)",
    "R": "Reject the entire DICOM file (R)",
}

verbose_usage = {
    "U": "User Optional (U)",
    "M": "Mandatory (M)",
    "C": "Conditional (C)",
}

verbose_type = {
    "1": "Required with valid value (1)",
    "1C": "Conditional; required with valid value if condition is met (1C)",
    "2": "Required; value may be empty (2)",
    "2C": "Conditional; must be present but " "can be empty if condition is met (2C)",
    "3": "Optional (3)",
}


def generate_human_readable_format(
    *,
    dicom_standard: DICOMStandard,
    procedure: Procedure,
    output: Path,
):

    for sop_id in procedure.sop_ids:
        coid_id = dicom_standard.map_sop_to_coid_id(sop_id)

        coid_output = output / coid_id
        coid_output.mkdir(parents=True, exist_ok=True)

        meta = []

        title = f"{coid_id} | {sop_id}"
        meta.append("=" * len(title))
        meta.append(title)
        meta.append("=" * len(title))
        meta.append("\n")

        try:
            meta.append(
                f":Default: {verbose_action[procedure.get_sop_default(sop_id)]}"
            )
            meta.append(f":Justification: {procedure.get_sop_justification(sop_id)}")
        except KeyError:
            pass  # Manual does not have a default

        with open(coid_output / "meta.rts", "w") as f:
            f.writelines("\n".join(meta))
            f.write("\n")

        for tag, action in procedure.get_sop_actions(sop_id).items():
            content = render_action(dicom_standard, tag, action, sop_id)
            keyword = dicom_standard.get_keyword_via_tag(tag)

            with open(coid_output / f"{keyword}.rts", "w") as f:
                f.write(content)


def render_action(dicom_standard: DICOMStandard, tag, action, sop_id):

    justification = action.get("justification", "N/A")
    action_info = []
    desc = verbose_action[action["default"]]
    action_info.append(f":Action: {desc}")
    action_info.append(f":Justication: {justification}")

    return render_attribute_info(
        dicom_standard=dicom_standard,
        tag=tag,
        sop_id=sop_id,
        headers=action_info,
    )


def render_attribute_info(dicom_standard: DICOMStandard, tag, sop_id, headers=None):
    name = dicom_standard.get_name_via_tag(tag)
    title = f"{name} | {tag}"
    info = ["-" * len(title)]
    info += [title]
    info.append("-" * len(title))

    for h in headers or []:
        info.append(h)

    try:
        bp = dicom_standard.get_basic_confidentiality_profile_via_tag(tag)
    except KeyError:
        bp = "N/A"
    info.append(f":Basic Profile: {bp}")

    module_info = render_module_info(dicom_standard, tag, sop_id)
    info += module_info

    return "\n".join(info)


def render_module_info(dicom_standard: DICOMStandard, tag, sop_id):
    info = []
    module_ids = dicom_standard._get_possible_module_ids_via_tag(tag, sop_id=sop_id)

    info.append(":In Modules:")

    indent = 3

    for module_id in sorted(module_ids):
        ciod_usage = dicom_standard.get_module_usage(module_id, sop_id=sop_id)
        tag_module_type = dicom_standard.get_tag_type(tag, module_id=module_id)
        tag_module_desc = dicom_standard.get_tag_description(tag, module_id=module_id)

        usage = verbose_usage[ciod_usage]
        type_ = verbose_type[tag_module_type]

        info.append(" " * indent + f"- {module_id} [{usage}] [{type_}]::\n")

        desc = str(
            BeautifulSoup(
                tag_module_desc,
                "html.parser",
            ).prettify()
        )

        desc_indented = textwrap.indent(desc, " " * (indent + 4))

        info.append(desc_indented)
    return info
