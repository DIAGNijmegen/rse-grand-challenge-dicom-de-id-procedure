# Standard-Operating Procedure

This document describes how the de-identification procedure is defined. 

The [core procedure](dist/procedure.json) is specified in JSON format. For ease of review, a [human-readable version](dist/human/) is also provided, enabling easy inspection of any changes.

## Guiding Principles

This procedure is based on the DICOM [Standard Basic De-identification Profile](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1), with customizations specific to the Grand Challenge platform.

The standard DICOM Basic Profile follows an **allow-by-default** principle: any attribute not explicitly mentioned in the profile is retained in the DICOM file. On the Grand Challenge platform, we take a stricter privacy stance by adopting a **deny-by-default** approach: attributes are removed unless explicitly allowed.  

However, simply denying all unspecified attributes would result in invalid DICOM files. To prevent this, we define an **allowlist of exceptions**, specifying the minimal set of DICOM tags that must remain to maintain file validity and usefulness. The procedure assigns a specific `Action` to each tag on this allowlist.

The final procedure is therefore a **customized superset** of the standard DICOM Basic Profile: it starts from a deny-by-default policy, then adds carefully selected exceptions to ensure the resulting files remain valid and fit for purpose.


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


#### 1. Module-Use Determinant

Module Use| Description | Action
---|---|---
U | User Optional | X (remove tags)
M | Mandatory | determine per tag
C | Conditional | determine per module/tag

Only U can be set automatically, both M/C need to have a manual choice made.

If a tag is could be used in multiple `Module` within a `SOPClass` the determinant is only used if all usages are the same.



#### 2. Retired-tags Determinant
The second determinant for the `Action` is the `Retired` value of the DICOM tag in the IOD:


Retired value | Action
---|---
Y|X



#### 3. Basic-Profile Determinant

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

If a tag is in multiple modules and hence has multiple `Type`, we only automatically determine the action if they are all the same. In other cases a manual choice needs to be made.

The `Action` of the `Basic Profile` together with the `Type` of the tag result in the following actions:

Action in Basic Profile | Description | Action if Type 1 |Action if Type 2 | Action if Type 3
--|--|--|--|--
Z/D |	Z unless D is required to maintain IOD conformance (Type 2 versus Type 1) | D | Z | X
X/Z |	X unless Z is required to maintain IOD conformance (Type 3 versus Type 2) | D | Z | X
X/D |	X unless D is required to maintain IOD conformance (Type 3 versus Type 1) | D | Z | X
X/Z/D |	X unless Z or D is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1) | D | Z | X
X/Z/U* |	X unless Z or replacement of contained instance UIDs (U) is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1 sequences containing UID references) | U | Z | X


#### 4. Tag-Type Determinant

When a tag is not present in the Standard DICOM de-identification profile, the `Action` is determined by the `Type` of the tag.

Type | Meaning | Action
-- | -- | --
Type 1 | Must be present and have a valid (non-empty) value | K
Type 2 | Must be present, but value can be empty | Z
Type 3 | Optional — may be present or absent | X

Other types require further follow ups. As mentioned above, if a tag is in multiple `Modules` for a single `SOPClass` we only determine an action automatically if all the `Type` are equal.



#### 5. Manual Determinant

Above determinants are automatic, however for conditional modules and conditional tags, a manual choice is required to determine the correct action.

Depending on the exact `Type`/`Module`/`description` an action is chosen that adheres to the guiding principle of being safe while maintaining a valid DICOM format.

Technically, these are noted in [procedure/manual.json](./procedure/manual.json). Which have a [human-readable counter part](./procedure/manual-human/) to aid in reviewing.

To aid in the choices an automatically spawned worklist which lists all still unset sop-tag-actions is used. It be found in [procedure/WORKLIST.rst](./procedure/WORKLIST.rts): in normal situations this worklist should be empty.
