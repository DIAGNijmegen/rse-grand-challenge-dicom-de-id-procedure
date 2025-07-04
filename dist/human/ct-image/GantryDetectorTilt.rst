----------------------------------
Gantry/Detector Tilt | (0018,1120)
----------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Nominal angle of tilt in degrees of the scanning gantry. Not intended for mathematical computations.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal angle of tilt in degrees of the scanning gantry. Not intended for mathematical computations. Zero degrees means the gantry is not tilted, negative degrees are when the top of the gantry is tilted away from where the table enters the gantry.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
