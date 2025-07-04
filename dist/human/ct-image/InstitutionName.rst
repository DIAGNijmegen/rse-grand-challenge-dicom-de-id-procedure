------------------------------
Institution Name | (0008,0080)
------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required, under some condition
:Basic Profile: X/Z/D
:In Modules:
   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Institution where the equipment that produced the Composite Instances is located.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute represents the organizational context only for the Equipment IE, and should not be construed to be a substitute for Issuer of Patient ID (0010,0021) or Issuer of Accession Number (0008,0051).
        </p>
       </div>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Code Sequence (0008,0082) is not present. May be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Code Sequence (0008,0082) is not present. May be present otherwise.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Code Sequence (0008,0082) is not present. May be present otherwise.
       </p>
