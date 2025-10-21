------------------------------------
Number of Focal Planes | (0048,0013)
------------------------------------
:Action: Keep (K)
:Justication: Criticial image meta data
:Basic Profile: N/A
:In Modules:
   - whole-slide-microscopy-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Number of acquisition focal planes used for extended depth of field.
       </p>
       <p>
        Required if Extended Depth of Field (0048,0012) Value is YES
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Total Pixel Matrix Focal Planes (0048,0303) describes the number of focal planes separately encoded, and is distinct from Number of Focal Planes (0048,0013), which describes in what manner different focal planes were combined into a single encoded plane (focus stacking).
        </p>
       </div>
