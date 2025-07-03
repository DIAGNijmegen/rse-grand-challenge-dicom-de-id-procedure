# Grand-Challenge DICOM De-Identification Procedure

[![CI](https://github.com/DIAGNijmegen/rse-grand-challenge-dicom-de-id-procedure/actions/workflows/ci.yml/badge.svg)](https://github.com/DIAGNijmegen/rse-grand-challenge-dicom-de-id-procedure/actions/workflows/ci.yml)

This repository contains the code that generate the procedure for the [Grand-Challenge.org](https://www.grand-challenge.org) de-identification methods. The procedure describes which action needs to be taken for a DICOM tag in order to be de-identified.

It is based on the DICOM Basic Profile of the [Standard DICOM de-identification profile](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1) but customized for the use on the Grand-Challenge platform.

## Usage

First, install `uv` you should then be able to run the any of the following `make` commands:

    $ make base

Which will create the base procedure, see Action logic below for details.

    $ make candidate

Which will merge **BASE** + **MANUAL** procedures to generate a **CANDIDATE procedure**. The **MANUAL procedure** is a hand-crafted action list for each DICOM tag that is unset in the **BASE procedure**.

    $ make worklist

Which will generate a reStructuredText that describes the tags for which no action has been set in the **CANDIDATE procedure**.

These will need to be addressed before we can generate the final procedure.

    $ VERSION="0.20250630.0" make final

Finally, above  will run all the earlier `make` targets (i.e. `base`, `candidate`, `worklist`) and then use the **CANDIDATE procedure** to build the distributable **FINAL procedure** Including a `VERSION`, as specified.

## How are actions determined

See the [standard-operation procedure](SOP.md) for more information.
