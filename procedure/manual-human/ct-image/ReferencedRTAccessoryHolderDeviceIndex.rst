---------------------------------------------------------
Referenced RT Accessory Holder Device Index | (300A,060E)
---------------------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Extended device information is not allowed by default
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The Value of Device Index (3010,0039) of the RT Accessory Holder Device in the RT Accessory Holder Definition Sequence (300A,0614).
       </p>
       <p>
        Required if RT Accessory Device Slot ID (300A,0615) is not present.
       </p>
       <p>
        See
        <span href="">
         Section C.36.2.2.3.1
        </span>
        .
       </p>
