-------------------------------------------
Distance Between Focal Planes | (0048,0014)
-------------------------------------------
:Action: Keep (K)
:Justication: Criticial image meta data
:Basic Profile: N/A
:In Modules:
   - whole-slide-microscopy-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Distance between acquisition focal planes used for extended depth of field, in µm.
       </p>
       <p>
        Required if Extended Depth of Field (0048,0012) Value is YES.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Spacing Between Slices (0018,0088) describes the spacing of focal planes separately encoded, and is distinct from Distance Between Focal Planes (0048,0014), which describes in what manner different focal planes were combined into a single encoded plane (focus stacking).
        </p>
       </div>
