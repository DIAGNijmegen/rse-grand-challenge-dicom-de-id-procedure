--------------------------------------
Data Collection Diameter | (0018,0090)
--------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The diameter in mm of the region over which data were collected.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The diameter in mm of the region over which data were collected. See
        <span href="">
         Section C.8.15.3.6.1
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         In the case of an Acquisition Type (0018,9302) of CONSTANT_ANGLE, the diameter is that in a plane normal to the central ray of the diverging X-Ray beam as it passes through the data collection center.
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
