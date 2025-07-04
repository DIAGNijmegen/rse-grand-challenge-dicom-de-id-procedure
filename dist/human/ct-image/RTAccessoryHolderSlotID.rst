-----------------------------------------
RT Accessory Holder Slot ID | (300A,0611)
-----------------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Basic Profile
:Basic Profile: Z
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Identifier of the RT Accessory Holder Slot in the RT Accessory Holding Device where this RT Accessory Device is inserted.
       </p>
       <p>
        Required if Referenced RT Accessory Holder Device Index (300A,060E) is present and has a Value and the referenced RT Accessory Holder Device contains an RT Accessory Holder Slot Sequence (300A,0610).
       </p>
