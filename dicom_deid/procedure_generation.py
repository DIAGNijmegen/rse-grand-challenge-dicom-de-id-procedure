from __future__ import annotations

import json
from collections import defaultdict
from enum import Enum


class DICOMStandardError(ValueError):
    pass


class DICOMStandard:
    """
    Represents the DICOM standard that can be queries for properties or relations.

    Raises:
        DICOMStandardError: If inconsistencies found in relations or assumptions are
        broken.
    """

    def __init__(
        self,
        *,
        version=None,
        sops=None,
        module_to_attributes=None,
        ciod_to_modules=None,
        ciods=None,
        attributes=None,
        confidentiality_profile_attributes=None,
    ):

        self.version = version

        # Relationships
        self.__sop_id_to_ciod_id = self._build_sop_id_to_ciod_id(sops, ciods)
        self.__ciod_id_to_module_ids = self._build_ciod_id_to_module_ids(
            ciod_to_modules
        )
        self.__module_id_to_tags = self._build_module_id_to_tags(module_to_attributes)
        self.__tag_to_module_ids = self._build_tag_to_module_ids()

        # Object lookups
        self.__module_lookup = self._build_module_lookup(ciod_to_modules)
        self.__attribute_lookup = self._build_attribute_lookup(attributes)
        self.__tag_to_module_lookup = self._build_tag_to_module_lookup(
            module_to_attributes
        )

        self.__confidentiality_profile_lookup = (
            self._build_confidentiality_profile_lookup(
                confidentiality_profile_attributes
            )
        )

    def _build_sop_id_to_ciod_id(self, sops, ciods):
        sops = sops or []
        ciods = ciods or []

        ciod_name_to_id = {ciod["name"].casefold(): ciod["id"] for ciod in ciods}
        result = {}
        for entry in sops:
            sop_id = entry["id"]
            ciod_name = entry["ciod"].casefold()
            ciod_id = ciod_name_to_id[ciod_name]
            if sop_id in result:
                raise DICOMStandardError(
                    f"SOP {sop_id} is already mapped to another CIOD"
                )
            result[sop_id] = ciod_id

        return result

    def _build_ciod_id_to_module_ids(self, ciod_to_modules):
        ciod_to_modules = ciod_to_modules or []

        result = defaultdict(set)

        for entry in ciod_to_modules:
            ciod_id = entry["ciodId"]
            module_id = entry["moduleId"]
            result[ciod_id].add(module_id)

        return result

    def _build_module_id_to_tags(self, module_to_attributes):
        module_to_attributes = module_to_attributes or []

        result = defaultdict(set)

        for entry in module_to_attributes:
            module_id = entry["moduleId"]
            tag = entry["tag"]

            result[module_id].add(tag)

        return result

    def _build_tag_to_module_ids(self):
        result = defaultdict(set)
        for module_id, tags in self.__module_id_to_tags.items():
            for tag in tags:
                result[tag].add(module_id)
        return result

    def _build_module_lookup(self, ciod_to_modules):
        ciod_to_modules = ciod_to_modules or []

        result = defaultdict(dict)
        for entry in ciod_to_modules:
            ciod_id = entry["ciodId"]
            module_id = entry["moduleId"]

            module_lookup_for_ciod = result[ciod_id]

            # Sanity check on consistency
            if module_id in module_lookup_for_ciod:
                raise DICOMStandardError(
                    f"Multiple definitions found for "
                    f"module {module_id} and CIOD {ciod_id}"
                )
            else:
                module_lookup_for_ciod[module_id] = entry

        return result

    def _build_attribute_lookup(self, attributes):
        attributes = attributes or []

        result = {}
        for entry in attributes:
            tag = entry["tag"]
            if tag in result:
                raise DICOMStandardError(
                    f"Multiple attribute definitions found for tag {tag}"
                )
            else:
                result[tag] = entry

        return result

    def _build_tag_to_module_lookup(self, module_to_attributes):
        module_to_attributes = module_to_attributes or []

        result = defaultdict(dict)
        for entry in module_to_attributes:
            tag = entry["tag"]
            module_id = entry["moduleId"]
            result[tag][module_id] = entry

        return result

    def _build_confidentiality_profile_lookup(self, confidentiality_profile_attributes):
        confidentiality_profile_attributes = confidentiality_profile_attributes or []

        result = {}
        for entry in confidentiality_profile_attributes:
            tag = entry["tag"]
            if tag in result:
                raise DICOMStandardError(
                    f"Multiple confidentiality profiles found for tag {tag}"
                )
            else:
                result[tag] = entry

        return result

    def map_sop_to_module_ids(self, /, sop_id):
        coid_id = self.__sop_id_to_ciod_id[sop_id]
        return self.__ciod_id_to_module_ids[coid_id]

    def map_sop_to_tags(self, /, sop_id):
        module_ids = self.map_sop_to_module_ids(sop_id)

        sop_tags = set()
        for module_id in module_ids:
            module_tags = self.__module_id_to_tags[module_id]
            sop_tags.update(module_tags)
        return sop_tags

    def _get_possible_module_ids_via_tag(self, /, tag, *, sop_id):
        sop_module_ids = self.map_sop_to_module_ids(sop_id)
        tag_module_ids = self.__tag_to_module_ids[tag]

        # Limit to the modules that are options given the COID (via SOP)
        return sop_module_ids & tag_module_ids

    def get_module_usages_via_tag(self, /, tag, *, sop_id):
        module_ids = self._get_possible_module_ids_via_tag(tag, sop_id=sop_id)

        ciod_id = self.__sop_id_to_ciod_id[sop_id]

        modules = []
        for module_id in module_ids:
            modules.append(self.__module_lookup[ciod_id][module_id])

        return {m["usage"] for m in modules}

    def get_attribute_types_via_tag(self, /, tag, *, sop_id):
        module_ids = self._get_possible_module_ids_via_tag(tag, sop_id=sop_id)
        module_lookup = self.__tag_to_module_lookup[tag]

        result = set()
        for module_id in module_ids:
            attr_mod_type = module_lookup[module_id]["type"]
            result.add(attr_mod_type)

        return result

    def get_attribute_retired_via_tag(self, /, tag):
        attribute = self.__attribute_lookup[tag]
        return attribute["retired"]

    def get_basic_confidentiality_profile_via_tag(self, /, tag):
        conf_profile = self.__confidentiality_profile_lookup[tag]
        return conf_profile["basicProfile"]

    @classmethod
    def from_path(cls, path):
        with (path / "version.json").open() as f:
            version = json.load(f)
        with (path / "sops.json").open() as f:
            sops = json.load(f)
        with (path / "module_to_attributes.json").open() as f:
            module_to_attributes = json.load(f)
        with (path / "ciod_to_modules.json").open() as f:
            ciod_to_modules = json.load(f)
        with (path / "ciods.json").open() as f:
            ciods = json.load(f)
        with (path / "attributes.json").open() as f:
            attributes = json.load(f)
        with (path / "confidentiality_profile_attributes.json").open() as f:
            confidentiality_profile_attributes = json.load(f)

        return cls(
            version=version,
            sops=sops,
            module_to_attributes=module_to_attributes,
            ciod_to_modules=ciod_to_modules,
            ciods=ciods,
            attributes=attributes,
            confidentiality_profile_attributes=confidentiality_profile_attributes,
        )

    def render_attribute_info(self, *, tag, sop_id):
        attr = self.__attribute_lookup[tag]

        return f"{attr["name"]} {tag}"


class ActionChoices(str, Enum):
    REMOVE = "X"
    KEEP = "K"

    REPLACE = "D"
    REPLACE_0 = "Z"
    UID = "U"

    REJECT = "R"


class Procedure:

    Action = ActionChoices

    def __init__(self):

        self._procedure = {
            "dicomStandardVersion": None,
            "default": self.Action.REJECT,
            "justification": "Unsupported SOP Class",
            "sopClass": defaultdict(
                lambda: {
                    "default": self.Action.REMOVE,
                    "justification": "Unsupported data element",
                    "tag": {},
                },
            ),
        }

    @property
    def dicom_standard_version(self):
        return self._procedure.get("dicomStandardVersion")

    @dicom_standard_version.setter
    def dicom_standard_version(self, version):
        self._procedure["dicomStandardVersion"] = version

    @property
    def default(self):
        return self._procedure.get("default")

    @default.setter
    def default(self, version):
        self._procedure["default"] = version

    @property
    def sop_ids(self):
        for sop in self._procedure["sopClass"]:
            yield sop

    def set_action(self, sop_id, tag, action, justification=""):
        if action is not None:
            action = {
                "default": action,
            }

            if justification:
                action["justification"] = justification

        self._procedure["sopClass"][sop_id]["tag"][tag] = action

    def get_sop_actions(self, sop_id):
        return self._procedure["sopClass"][sop_id]["tag"]

    def set_sop_default(self, sop_id, default):
        self._procedure["sopClass"][sop_id]["default"] = default

    def get_sop_default(self, sop_id):
        return self._procedure["sopClass"][sop_id]["default"]

    def get_unset_action_tags_in_sops(
        self,
    ):
        for sop, entry in self._procedure["sopClass"].items():
            for tag, action in entry["tag"].items():
                if action is None:
                    yield tag, sop

    @classmethod
    def from_json(cls, json_str):

        p = json.loads(json_str)

        procedure = cls()
        procedure._procedure = p

        return procedure

    def to_json(self, **kwargs):
        return json.dumps(self._procedure, **kwargs)

    def __add__(self: Procedure, other: Procedure):
        p = Procedure()
        p._procedure = self._procedure.copy()

        p.dicom_standard_version = (
            other.dicom_standard_version or p.dicom_standard_version
        )
        p.default = other.default or p.default

        for sop_id in other.sop_ids:
            for tag, action in other.get_sop_actions(sop_id).items():
                p.set_action(
                    sop_id=sop_id,
                    tag=tag,
                    action=action["default"],
                    justification=action.get("justification"),
                )

        return p


def apply_module_actions(
    *,
    procedure: Procedure,
    dicom_standard: DICOMStandard,
):

    for tag, sop in procedure.get_unset_action_tags_in_sops():
        usages = dicom_standard.get_module_usages_via_tag(tag, sop_id=sop)

        if len(usages) != 1:
            continue
        else:
            usage = usages.pop().casefold()

        if usage == "u":
            procedure.set_action(
                sop_id=sop,
                tag=tag,
                action=procedure.Action.REMOVE,
                justification="[AUTO] Module usage",
            )
        elif usage in ("m", "c"):
            continue  # Leave it unset
        else:
            raise ValueError(f"Unsupported module usage: {usage!r}")


def apply_retired_attribute_actions(
    *,
    procedure: Procedure,
    dicom_standard: DICOMStandard,
):
    for tag, sop in procedure.get_unset_action_tags_in_sops():
        retired = dicom_standard.get_attribute_retired_via_tag(tag).casefold()
        if retired == "y":
            procedure.set_action(
                sop_id=sop,
                tag=tag,
                action=procedure.Action.REMOVE,
                justification="[AUTO] Retired",
            )
        elif retired == "n":
            continue  # Leave it unset
        else:
            raise ValueError(f"Unsupported attribute retired: {retired!r}")


def apply_basic_dicom_deid_profile_actions(
    *,
    procedure: Procedure,
    dicom_standard: DICOMStandard,
):
    action_map = {
        "d": Procedure.Action.REPLACE,
        "z": Procedure.Action.REPLACE_0,
        "x": Procedure.Action.REMOVE,
        "k": Procedure.Action.KEEP,
        "u": Procedure.Action.UID,
    }

    basic_profile_action_type_lookup = {
        ("z/d", "1"): Procedure.Action.REPLACE,
        ("z/d", "2"): Procedure.Action.REPLACE_0,
        ("z/d", "3"): Procedure.Action.REMOVE,
        ("x/z", "1"): Procedure.Action.REPLACE,
        ("x/z", "2"): Procedure.Action.REPLACE_0,
        ("x/z", "3"): Procedure.Action.REMOVE,
        ("x/d", "1"): Procedure.Action.REPLACE,
        ("x/d", "2"): Procedure.Action.REPLACE_0,
        ("x/d", "3"): Procedure.Action.REMOVE,
        ("x/z/d", "1"): Procedure.Action.REPLACE,
        ("x/z/d", "2"): Procedure.Action.REPLACE_0,
        ("x/z/d", "3"): Procedure.Action.REMOVE,
        ("x/z/u*", "1"): Procedure.Action.UID,
        ("x/z/u*", "2"): Procedure.Action.REPLACE_0,
        ("x/z/u*", "3"): Procedure.Action.REMOVE,
    }

    for tag, sop in procedure.get_unset_action_tags_in_sops():
        try:
            basic_profile_action = (
                dicom_standard.get_basic_confidentiality_profile_via_tag(tag)
            )
        except KeyError:
            continue  # No confidentiality profile set

        basic_profile_action = basic_profile_action.casefold()

        action = action_map.get(basic_profile_action)
        if action is None:
            attribute_types = dicom_standard.get_attribute_types_via_tag(
                tag, sop_id=sop
            )

            if len(attribute_types) != 1:
                continue
            else:
                attribute_type = next(iter(attribute_types)).casefold()

            if attribute_type in ("1c", "2c", "none"):
                continue  # conditionals or unknowns can't be set automatically

            try:
                action = basic_profile_action_type_lookup[
                    (basic_profile_action, attribute_type)
                ]
            except KeyError as e:
                raise ValueError(
                    f"Unsupported confidentiality action: {basic_profile_action} for "
                    f"attribute type {attribute_type}"
                ) from e

        if action is not None:
            procedure.set_action(
                sop_id=sop,
                tag=tag,
                action=action,
                justification="[AUTO] Basic Profile",
            )


def apply_attribute_type_actions(
    *,
    procedure: Procedure,
    dicom_standard: DICOMStandard,
):
    for tag, sop in procedure.get_unset_action_tags_in_sops():

        attribute_types = dicom_standard.get_attribute_types_via_tag(tag, sop_id=sop)

        if len(attribute_types) != 1:
            continue
        else:
            attribute_type = next(iter(attribute_types)).casefold()

        action = None

        if attribute_type == "1":
            action = Procedure.Action.KEEP
        elif attribute_type == "2":
            action = Procedure.Action.REPLACE_0
        elif attribute_type == "3":
            action = Procedure.Action.REMOVE
        elif attribute_type in ("1c", "2c", "none"):
            pass  # We don't touch it
        else:
            raise ValueError(f"Unsupported attribute type: {attribute_type}")

        if action is not None:
            procedure.set_action(
                sop_id=sop,
                tag=tag,
                action=action,
                justification="[AUTO] Attribute-Module type",
            )


def generate_base_procedure(*, dicom_standard_path):
    ds = DICOMStandard.from_path(dicom_standard_path)
    sops = ["1.2.840.10008.5.1.4.1.1.2"]

    p = Procedure()
    for sop in sops:
        tags = ds.map_sop_to_tags(sop)
        for tag in tags:
            p.set_action(sop_id=sop, tag=tag, action=None)

    p.dicom_standard_version = ds.version

    apply_module_actions(procedure=p, dicom_standard=ds)
    apply_retired_attribute_actions(procedure=p, dicom_standard=ds)
    apply_basic_dicom_deid_profile_actions(procedure=p, dicom_standard=ds)
    apply_attribute_type_actions(procedure=p, dicom_standard=ds)

    return p
