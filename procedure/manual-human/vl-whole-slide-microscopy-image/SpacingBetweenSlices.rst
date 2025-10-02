------------------------------------
Spacing Between Slices | (0018,0088)
------------------------------------
:Action: Keep (K)
:Justication: Generally required for viewers
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Spacing between adjacent slices, in mm. The spacing is measured from the center-to-center of each slice, and if present shall not be negative.
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is TILED_FULL and Total Pixel Matrix Focal Planes (0048,0303) is greater than 1. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         In the case of Whole Slide Images, Spacing Between Slices (0018,0088) describes the spacing of focal planes separately encoded, and is distinct from Distance Between Focal Planes (0048,0014), which describes in what manner different focal planes were combined into a single encoded plane (focus stacking).
        </p>
       </div>
       <h3>
        Note
       </h3>
       <p>
        Part of the Pixel Measures Functional Group Macro with usage: M
       </p>
