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
        ciods_to_modules=None,
        ciods=None,
        attributes=None,
        confidentiality_profile_attributes=None,
        macro_to_attributes=None,
    ):

        self.version = version

        sops = sops or []
        module_to_attributes = module_to_attributes or []
        ciods_to_modules = ciods_to_modules or []
        ciods = ciods or []
        attributes = attributes or []
        confidentiality_profile_attributes = confidentiality_profile_attributes or []
        macro_to_attributes = macro_to_attributes or []

        # Map CIOD name to CIOD id: SOPClasses and CIOD are linked via name
        ciod_name_to_id = {ciod["name"].lower(): ciod["id"] for ciod in ciods}

        # Map SOPClassUID to CIOD
        self.__sop_id_to_ciod_id = {}
        for entry in sops:
            sop_id = entry["id"]
            ciod_name = entry["ciod"].lower()
            ciod_id = ciod_name_to_id[ciod_name]
            if sop_id in self.__sop_id_to_ciod_id:
                raise DICOMStandardError(
                    f"SOP {sop_id} is already mapped to another CIOD"
                )
            self.__sop_id_to_ciod_id[sop_id] = ciod_id

        # Map COID to modules
        self.__ciod_id_to_module_ids = defaultdict(set)

        for entry in ciods_to_modules:
            ciod_id = entry["ciodId"]
            module_id = entry["moduleId"]
            self.__ciod_id_to_module_ids[ciod_id].add(module_id)

        # Build module to tags, and vice vera
        self.__module_id_to_tags = defaultdict(set)
        self.__tag_to_module_ids = defaultdict(set)

        for entry in module_to_attributes:
            module_id = entry["moduleId"]
            tag = entry["tag"]

            self.__module_id_to_tags[module_id].add(tag)
            self.__tag_to_module_ids[tag].add(module_id)

        # Lookups

        # Note: modules ARE defined multiple times in the reference
        # We do a sanity check if the values are the same
        self.__module_lookup = {}
        for entry in ciods_to_modules:
            module_id = entry["moduleId"]

            # Sanity check on consistency
            if module_id in self.__module_lookup:
                existing = self.__module_lookup[module_id]
                for k, v in entry.items():
                    if k != "ciodId" and existing[k] != v:
                        raise DICOMStandardError(
                            f"Inconsistent definitions found for module {module_id}"
                        )
            else:
                self.__module_lookup[module_id] = entry

        self.__attribute_lookup = {entry["tag"]: entry for entry in attributes}

        self.__confidentiality_profile_lookup = {
            entry["tag"]: entry for entry in confidentiality_profile_attributes
        }

        self.__attribute_type_lookup = {
            entry["tag"]: entry["type"] for entry in macro_to_attributes
        }

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

    def get_module_via_tag(self, /, tag, *, sop_id):
        sop_module_ids = self.map_sop_to_module_ids(sop_id)
        tag_module_ids = self.__tag_to_module_ids[tag]

        matching_modules = sop_module_ids & tag_module_ids

        if len(matching_modules) != 1:
            raise DICOMStandardError(
                f"Tag {tag} belongs to {len(matching_modules)} modules, expected 1"
            )

        module_id = matching_modules.pop()
        return self.__module_lookup[module_id]

    def get_attribute_via_tag(self, /, tag):
        attribute = {**self.__attribute_lookup[tag]}

        try:
            attribute["type"] = self.__attribute_type_lookup[tag]
        except KeyError:
            pass  # attribute will simply not have a type

        return attribute

    def get_confidentiality_profile_via_tag(self, /, tag):
        return self.__confidentiality_profile_lookup[tag]


class ActionChoices(str, Enum):
    REMOVE = "X"
    KEEP = "K"

    REPLACE = "D"
    REPLACE0 = "Z"
    CLEAN = "C"
    UID = "U"


class Profile:

    Action = ActionChoices

    def __init__(self):

        self.__profile = {
            "SOPClassUID": defaultdict(
                lambda: {
                    "tag": {},
                },
            )
        }

    def set_action(self, sop_id, tag, action):
        self.__profile["SOPClassUID"][sop_id]["tag"][tag] = {
            "action": action,
        }

    def get_unset_action_tags_in_sops(
        self,
    ):
        for sop, entry in self.__profile["SOPClassUID"].items():
            for tag, action in entry["tag"].items():
                if action["action"] is None:
                    yield tag, sop

    def to_json(self):
        return json.dumps(self.__profile)


def generate_standard_profile(*, dicom_standard_path, output_path):
    pass


def apply_module_actions(
    *,
    profile: Profile,
    dicom_standard: DICOMStandard,
):

    for tag, sop in profile.get_unset_action_tags_in_sops():
        module = dicom_standard.get_module_via_tag(tag, sop_id=sop)
        usage = module["usage"].lower()
        if usage == "u":
            profile.set_action(
                sop_id=sop,
                tag=tag,
                action=profile.Action.REMOVE,
            )
        elif usage in ("m", "c"):
            continue  # Leave it unset
        else:
            raise ValueError(f"Unsupported module usage: {usage!r}")


def apply_retired_attribute_actions(
    *,
    profile: Profile,
    dicom_standard: DICOMStandard,
):
    for tag, sop in profile.get_unset_action_tags_in_sops():
        attribute = dicom_standard.get_attribute_via_tag(tag)
        retired = attribute["retired"].lower()
        if retired == "y":
            profile.set_action(
                sop_id=sop,
                tag=tag,
                action=profile.Action.REMOVE,
            )
        elif retired == "n":
            continue  # Leave it unset
        else:
            raise ValueError(f"Unsupported attribute retired: {retired!r}")


def apply_basic_dicom_deid_profile_actions(
    *,
    profile: Profile,
    dicom_standard: DICOMStandard,
):
    action_map = {
        "d": Profile.Action.REPLACE,
        "z": Profile.Action.REPLACE0,
        "x": Profile.Action.REMOVE,
        "k": Profile.Action.KEEP,
        "c": Profile.Action.CLEAN,
        "u": Profile.Action.UID,
    }

    basic_profile_action_type_lookup = {
        ("z/d", "1"): Profile.Action.REPLACE,
        ("z/d", "1c"): Profile.Action.REPLACE,
        ("z/d", "2"): Profile.Action.REPLACE0,
        ("z/d", "2c"): Profile.Action.REPLACE0,
        ("z/d", "3"): Profile.Action.REMOVE,
        ("x/z", "1"): Profile.Action.REPLACE,
        ("x/z", "1c"): Profile.Action.REPLACE,
        ("x/z", "2"): Profile.Action.REPLACE0,
        ("x/z", "2c"): Profile.Action.REPLACE0,
        ("x/z", "3"): Profile.Action.REMOVE,
        ("x/d", "1"): Profile.Action.REPLACE,
        ("x/d", "1c"): Profile.Action.REPLACE,
        ("x/d", "2"): Profile.Action.REPLACE0,
        ("x/d", "2c"): Profile.Action.REPLACE0,
        ("x/d", "3"): Profile.Action.REMOVE,
        ("x/z/d", "1"): Profile.Action.REPLACE,
        ("x/z/d", "1c"): Profile.Action.REPLACE,
        ("x/z/d", "2"): Profile.Action.REPLACE0,
        ("x/z/d", "2c"): Profile.Action.REPLACE0,
        ("x/z/d", "3"): Profile.Action.REMOVE,
        ("x/z/u*", "1"): Profile.Action.UID,
        ("x/z/u*", "1c"): Profile.Action.UID,
        ("x/z/u*", "2"): Profile.Action.REPLACE0,
        ("x/z/u*", "2c"): Profile.Action.REPLACE0,
        ("x/z/u*", "3"): Profile.Action.REMOVE,
    }

    for tag, sop in profile.get_unset_action_tags_in_sops():
        conf_profile = dicom_standard.get_confidentiality_profile_via_tag(tag)
        basic_profile_action = conf_profile["basicProfile"].lower()

        action = action_map.get(basic_profile_action)
        if action is None:
            attribute = dicom_standard.get_attribute_via_tag(tag)
            attribute_type = attribute["type"].lower()
            try:
                action = basic_profile_action_type_lookup[
                    (basic_profile_action, attribute_type)
                ]
            except KeyError as e:
                raise ValueError(
                    f"Unsupported confidentiality action: {basic_profile_action} for "
                    f"attribute type {attribute_type}"
                ) from e

        profile.set_action(sop_id=sop, tag=tag, action=action)


def apply_attribute_type_actions(
    *,
    profile: Profile,
    dicom_standard: DICOMStandard,
):
    for tag, sop in profile.get_unset_action_tags_in_sops():
        attribute = dicom_standard.get_attribute_via_tag(tag)
        attribute_type = attribute["type"].lower()

        action = None

        if attribute_type == "1":
            action = Profile.Action.KEEP
        elif attribute_type == "2":
            action = Profile.Action.REPLACE0
        elif attribute_type == "3":
            action = Profile.Action.REMOVE
        elif attribute_type in ("1c", "2c"):
            pass  # We don't touch it
        else:
            raise ValueError(f"Unsupported attribute type: {attribute_type}")

        if action is not None:
            profile.set_action(sop_id=sop, tag=tag, action=action)
