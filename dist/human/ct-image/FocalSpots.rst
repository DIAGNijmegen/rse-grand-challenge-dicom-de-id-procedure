---------------------------
Focal Spot(s) | (0018,1190)
---------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Used nominal size of the focal spot in mm.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Used nominal size of the focal spot in mm. The Attribute may only have one or two Values, for devices with variable focal spot, small dimension followed by large dimension
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
