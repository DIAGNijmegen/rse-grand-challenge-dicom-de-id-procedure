-------------------------------------
Number of Optical Paths | (0048,0302)
-------------------------------------
:Action: Keep (K)
:Justication: Critical data
:Basic Profile: N/A
:In Modules:
   - optical-path [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Number of Items in the Optical Path Sequence (0048,0105).
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is present with a Value of TILED_FULL. May be present otherwise.
       </p>
