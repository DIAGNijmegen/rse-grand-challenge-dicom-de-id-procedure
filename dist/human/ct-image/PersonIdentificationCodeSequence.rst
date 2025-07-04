-------------------------------------------------
Person Identification Code Sequence | (0040,1101)
-------------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: D
:In Modules:
   - general-series [Mandatory (M)] [Required with valid value (1)]::

       <p>
        A coded entry that identifies a person.
       </p>
       <p>
        The Code Meaning Attribute, though it will be encoded with a VR of LO, may be encoded according to the rules of the PN VR (e.g., caret '^' delimiters shall separate name components), except that a single component (i.e., the whole name unseparated by caret delimiters) is not permitted. Name component groups for use with multi-byte character sets are permitted, as long as they fit within the 64 characters (the length of the LO VR).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

   - general-study [Mandatory (M)] [Required with valid value (1)]::

       <p>
        A coded entry that identifies a person.
       </p>
       <p>
        The Code Meaning Attribute, though it will be encoded with a VR of LO, may be encoded according to the rules of the PN VR (e.g., caret '^' delimiters shall separate name components), except that a single component (i.e., the whole name unseparated by caret delimiters) is not permitted. Name component groups for use with multi-byte character sets are permitted, as long as they fit within the 64 characters (the length of the LO VR).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        A coded entry that identifies a person.
       </p>
       <p>
        The Code Meaning Attribute, though it will be encoded with a VR of LO, may be encoded according to the rules of the PN VR (e.g., caret '^' delimiters shall separate name components), except that a single component (i.e., the whole name unseparated by caret delimiters) is not permitted. Name component groups for use with multi-byte character sets are permitted, as long as they fit within the 64 characters (the length of the LO VR).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
