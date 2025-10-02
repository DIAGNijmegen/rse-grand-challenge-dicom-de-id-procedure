--------------------------------------
Derivation Code Sequence | (0008,9215)
--------------------------------------
:Action: Remove (X)
:Justication: References other Images, this is not supported
:Basic Profile: N/A
:In Modules:
   - general-reference [User Optional (U)] [Optional (3)]::

       <p>
        A coded description of how this image was derived. See
        <span href="">
         Section C.12.4.1.1
        </span>
        for further explanation.
       </p>
       <p>
        One or more Items are permitted in this Sequence. More than one Item indicates that successive derivation steps have been applied.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A coded description of how this Frame was derived. See
        <span href="">
         Section C.12.4.1.1
        </span>
        for further explanation.
       </p>
       <p>
        One or more Items shall be included in this Sequence. More than one Item indicates that successive derivation steps have been applied.
       </p>
       <p>
        Required if SOP Class UID (0008,0016) is not "1.2.840.10008.5.1.4.1.1.2.2" (Legacy Converted Enhanced CT Image Storage) and not "1.2.840.10008.5.1.4.1.1.4.4" (Legacy Converted Enhanced MR Image Storage) and not "1.2.840.10008.5.1.4.1.1.128.1" (Legacy Converted Enhanced PET Image Storage), may be present otherwise.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Derivation Image Functional Group Macro with usage: C
       </p>
       <p>
        Required if the image or Frame has been derived from another SOP Instance.
       </p>
