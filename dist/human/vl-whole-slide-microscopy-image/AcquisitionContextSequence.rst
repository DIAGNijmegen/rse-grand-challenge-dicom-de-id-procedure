------------------------------------------
Acquisition Context Sequence | (0040,0555)
------------------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Basic Profile
:Basic Profile: X/Z
:In Modules:
   - acquisition-context [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        A Sequence of Items that describes the conditions present during the acquisition of the data of the SOP Instance.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
