-----------------------
Echo Time | (0018,0081)
-----------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - mr-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Time in ms between the middle of the excitation pulse and the peak of the echo produced (kx=0). In the case of segmented k-space, the TE(eff) is the time between the middle of the excitation pulse to the peak of the echo that is used to cover the center of k-space (i.e., -kx=0, ky=0).
       </p>
