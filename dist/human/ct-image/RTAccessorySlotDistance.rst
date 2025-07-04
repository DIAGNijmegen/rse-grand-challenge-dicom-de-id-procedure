----------------------------------------
RT Accessory Slot Distance | (300A,0613)
----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Distance in mm from the reference location as specified by RT Device Distance Reference Location Code Sequence (300A,0659) to the RT Accessory Device Slot.
       </p>
       <p>
        Required if RT Accessory Device Slot ID (300A,0615) is present and has a Value.
       </p>
