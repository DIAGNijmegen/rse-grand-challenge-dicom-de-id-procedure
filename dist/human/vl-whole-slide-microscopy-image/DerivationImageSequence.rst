---------------------------------------
Derivation Image Sequence | (0008,9124)
---------------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        The set of Images or other composite SOP Instances that were used to derive this Frame.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
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
