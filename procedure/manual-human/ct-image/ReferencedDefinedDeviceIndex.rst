---------------------------------------------
Referenced Defined Device Index | (300A,0602)
---------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Extended device information is not allowed by default
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Value of Device Index (3010,0039) from the Acquisition Device Sequence (3002,0117) corresponding to the Acquisition Device used in this Item.
       </p>
       <p>
        Required if Acquisition Device Sequence (3002,0117) is present and Value 1 of Image Type (0008,0008) has the Value ORIGINAL or the current Instance was derived from an Instance where Referenced Defined Device Index (300A,0602) was present in the Image Receptor Position Sequence (3002,010E). May be present otherwise.
       </p>
