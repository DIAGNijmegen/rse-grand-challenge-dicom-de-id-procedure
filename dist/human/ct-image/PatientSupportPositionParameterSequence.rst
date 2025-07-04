---------------------------------------------------------
Patient Support Position Parameter Sequence | (300A,065B)
---------------------------------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Translational and rotational parameters for the Patient Support device.
       </p>
       <p>
        Shall be consistent with the Image to Equipment Mapping Matrix (0028,9520).
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
