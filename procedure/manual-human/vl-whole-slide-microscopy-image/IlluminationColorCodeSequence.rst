----------------------------------------------
Illumination Color Code Sequence | (0048,0108)
----------------------------------------------
:Action: Keep (K)
:Justication: Criticial image meta data
:Basic Profile: N/A
:In Modules:
   - optical-path [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Color of the illuminator.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Illumination Wave Length (0022,0055) is not present. May be present otherwise.
       </p>
