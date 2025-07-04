---------------------------------------
Institution Code Sequence | (0008,0082)
---------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required, under some condition
:Basic Profile: X/Z/D
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Name (0008,0080) is not present. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Name (0008,0080) is not present. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Name (0008,0080) is not present. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
