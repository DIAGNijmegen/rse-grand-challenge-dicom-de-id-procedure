-----------------------------
Exposure in mAs | (0018,9332)
-----------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The exposure expressed in milliampere seconds, for example calculated from exposure time and X-Ray tube current.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The exposure expressed in milliampere seconds, for example calculated from exposure time and X-Ray tube current.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
