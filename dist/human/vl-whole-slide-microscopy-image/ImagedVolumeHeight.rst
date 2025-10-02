----------------------------------
Imaged Volume Height | (0048,0002)
----------------------------------
:Action: Keep (K)
:Justication: Criticial image meta data
:Basic Profile: N/A
:In Modules:
   - whole-slide-microscopy-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Height of total imaged volume (distance in the direction of columns in each Frame) in mm. See
        <span href="">
         Section C.8.12.4.1.2
        </span>
       </p>
       <p>
        Required if Image Type (0008,0008) Value 3 is VOLUME. May be present otherwise.
       </p>
