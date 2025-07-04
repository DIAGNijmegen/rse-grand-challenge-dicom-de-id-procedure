-----------------------------
Revolution Time | (0018,9305)
-----------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The time in seconds of a complete revolution of the source around the gantry orbit.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The time in seconds of a complete revolution of the source around the gantry orbit. This Value is independent of the Reconstruction Angle (0018,9319) of the Frame.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>
       <p>
        Otherwise may be present if Frame Type (0008,9007) Value 1 of this Frame is DERIVED or Image Type (0008,0008) Value 1 is DERIVED, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>
