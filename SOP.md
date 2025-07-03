# Standard-Operating Procedure

This document describes how the final de-identification procedure is created. The procedure are in JSON format and have a human-readable counter part that allow for easy reviewing of any changes. The procedure is split via `SOPClassUID` and then the data element tag (e.g. `(1234, 1234)`). The SOP + tag prescribes the action that should be executed.

## Action logic:
The `Action` determines how a tag is handed during de-identification. The options are as follows:

Code | Action
---|---
"D" |	replace with a non-zero length value that may be a dummy value and consistent with the VR
"Z" |	replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR
"X" |	remove
"K" |	keep (unchanged for non-Sequence Attributes, cleaned for Sequences)
"C" |	clean, that is replace with values of similar meaning known not to contain identifying information and consistent with the VR
"U" |	replace with a non-zero length UID that is internally consistent within a set of Instances
"R" |	reject the entire DICOM file

The VR (Value Representation) describes the datatype of the tag.


Each object in the DICOM standard is described in an IOD (Information Object Definition). Each IOD lists the DICOM-tags associated with that object, grouped by Module (see for example https://dicom.innolitics.com/ciods/ct-image). Each module specifies its `Use` within the object, which is the first determinant for the `Action`.

#### 1. Module Use

Module Use| Description | Action
---|---|---
U | User Optional | X (remove tags)
M | Mandatory | determine per tag
C | Conditional | determine per module

#### 2. Retired tags
The second determinant for the `Action` is the `Retired` value of the DICOM tag in the IOD:


Retired value | Action
---|---
Y|X

#### 3. Standard DICOM de-identification profile

The third determinant for the `Action` is the value for `Basic Profile`, in the [Standard DICOM de-identification profile](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1). In the most simple form these are the same as listed above:

Code | Action
---|---
D |	replace with a non-zero length value that may be a dummy value and consistent with the VR
Z |	replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR
X |	remove
K |	keep (unchanged for non-Sequence Attributes, cleaned for Sequences)
C |	clean, that is replace with values of similar meaning known not to contain identifying information and consistent with the VR
U |	replace with a non-zero length UID that is internally consistent within a set of Instances


For certain tags the `Basic Profile` lists multiple values, in which case the `Type` of a tag becomes relevant. The `Type` of a tag describes the tag's data requirement level when used in specific `Module` and can have the following values:

Type | Meaning
-- | --
Type 1 | Must be present and have a valid (non-empty) value
Type 1C | Must be present and have a valid (non-empty) value under certain conditions
Type 2 | Must be present, but value can be empty
Type 2C | Must be present, but value can be empty under certain conditions
Type 3 | Optional — may be present or absent
none | Unknown

The `Action` of the `Basic Profile` together with the `Type` of the tag result in the following actions:

Action in Basic Profile | Description | Action if Type 1 |Action if Type 2 | Action if Type 3
--|--|--|--|--
Z/D |	Z unless D is required to maintain IOD conformance (Type 2 versus Type 1) | D | Z | X
X/Z |	X unless Z is required to maintain IOD conformance (Type 3 versus Type 2) | D | Z | X
X/D |	X unless D is required to maintain IOD conformance (Type 3 versus Type 1) | D | Z | X
X/Z/D |	X unless Z or D is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1) | D | Z | X
X/Z/U* |	X unless Z or replacement of contained instance UIDs (U) is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1 sequences containing UID references) | U | Z | X


#### 4. Tag type.

When a Tag is not present in the Standard DICOM de-identification profile, the `Action` is determined by the `Type` of the tag.

Type | Meaning | Action
-- | -- | --
Type 1 | Must be present and have a valid (non-empty) value | K
Type 2 | Must be present, but value can be empty | Z
Type 3 | Optional — may be present or absent | X

Other types require further follow ups.

#### 5. Manual determinant

For conditional modules and conditional tags, a manual action is required to determine the correct action. These might be straight-forward.

Technically these are noted in `procedure/manual.json`. A worklist which lists all still unset sop-tag-actions an be found in `procedure/WORKLIST.rst`: in normal situations this worklist should be **empty**.
