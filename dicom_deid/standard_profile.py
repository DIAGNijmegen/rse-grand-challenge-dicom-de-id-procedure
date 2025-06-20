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
    ):

        self.version = version

        sops = sops or []
        module_to_attributes = module_to_attributes or []
        ciods_to_modules = ciods_to_modules or []
        ciods = ciods or []
        attributes = attributes or []

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
        return self.__attribute_lookup[tag]


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
