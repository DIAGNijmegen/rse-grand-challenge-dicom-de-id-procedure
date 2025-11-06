-------------------------------------------
Encrypted Attributes Sequence | (0400,0500)
-------------------------------------------
:Action: Remove (X)
:Justication: Contains encrypted DICOM data, possibly PI
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Sequence of Items containing encrypted DICOM data.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if application level confidentiality is needed and certain recipients are allowed to decrypt all or portions of the Encrypted Attributes Data Set. See
        <span href="">
         Section C.12.1.1.4.1
        </span>
        .
       </p>
