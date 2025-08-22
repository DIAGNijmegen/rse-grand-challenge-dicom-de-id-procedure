# Grand-Challenge DICOM De-Identification Procedure

[![CI](https://github.com/DIAGNijmegen/rse-grand-challenge-dicom-de-id-procedure/actions/workflows/ci.yml/badge.svg)](https://github.com/DIAGNijmegen/rse-grand-challenge-dicom-de-id-procedure/actions/workflows/ci.yml)

This repository contains the code that generate the procedure for the [Grand-Challenge.org](https://www.grand-challenge.org) de-identification methods. The procedure describes which action needs to be taken for a DICOM tag in order to be de-identified.

It is based on the DICOM Basic Profile of the [Standard DICOM de-identification profile](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1) but customized for the use on the Grand-Challenge platform.

More information about de-identification choices can be found in the [standard-operation procedure](SOP.md).


## Procedure Usage

For JavaScript you can use the ESM + UDM bundles via the npmjs package:
- https://www.npmjs.com/package/@diagnijmegen/rse-grand-challenge-dicom-deid-procedure

The `procedure.json` has two lookups: firstly by SOPClassUID and secondly by the data element tag. This results in a `"default"` action that is to be executed for the data element in question. The action can be any of:

Code | Action
---|---
"D" |	replace with a non-zero length value that may be a dummy value and consistent with the VR
"Z" |	replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR
"X" |	remove
"K" |	keep (unchanged for non-Sequence Attributes, cleaned for Sequences)
"C" |	clean, that is replace with values of similar meaning known not to contain identifying information and consistent with the VR
"U" |	replace with a non-zero length UID that is internally consistent within a set of Instances
"R" |	reject the entire DICOM file

For Python you can use the PyPi package: https://pypi.org/project/grand-challenge-dicom-de-id-procedure/

    $ pip install grand-challenge-dicom-de-id-procedure

To load the procedure import it as follows:

```Python
from grand_challenge_dicom_de_id_procedure import procedure

# Check the version
print(procedure["version"])

# Get an action for tag (0008,0005) of SOPClassUID "1.2.840.10008.5.1.4.1.1.2" (CT image)
action = procedure["sopClass"]["1.2.840.10008.5.1.4.1.1.2"]["tag"]["(0008,0005)"]["default"]

print(action) # "K"
```

## Procedure Building

First, install `uv` you should then be able to run the any of the following `make` commands:

    $ make base

Which will create the base procedure, see Action logic below for details.

    $ make candidate

Which will merge **BASE** + **MANUAL** procedures to generate a **CANDIDATE procedure**. The **MANUAL procedure** is a hand-crafted action list for each DICOM tag that is unset in the **BASE procedure**.

    $ make worklist

Which will generate a reStructuredText that describes the tags for which no action has been set in the **CANDIDATE procedure**.

These will need to be addressed before we can generate the final procedure.

    $ VERSION="2025.6.0" make final

Finally, above  will run all the earlier `make` targets (i.e. `base`, `candidate`, `worklist`) and then use the **CANDIDATE procedure** to build the distributable **FINAL procedure** Including a `VERSION`, as specified.


## Procedure Release

Calling `make final` with a `VERSION` also inserts the version in the relevant Python and NPM package configuration. The actual package(s) release is done via GitHub actions. The steps are:

1. Ensure that `main` contains the latest version you would like to release
2. Create and publish a release on GitHub, creating a new tag
    - Versioning dated-semver and follows format `YYYY.MM.MINOR`, where `YYYY` is the year `MM` is the month with no-zero padding and MINOR is the version bump within that month (starting at '0'). For instance `2025.2.0`.
3. GitHub actions to publish the new package(s) automatically starts when a release is published
4. Once everything is published, the dependency needs to be updated downstream (e.g. in Grand-Challenge)
