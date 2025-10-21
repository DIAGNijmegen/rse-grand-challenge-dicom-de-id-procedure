---------------------------------------------
Total Pixel Matrix Focal Planes | (0048,0303)
---------------------------------------------
:Action: Keep (K)
:Justication: Criticial image meta data
:Basic Profile: N/A
:In Modules:
   - microscope-slide-layer-tile-organization [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Total number of focal planes (Z locations) in the pixel matrix; i.e., depth of total imaged volume in pixels. See
        <span href="">
         Section C.8.12.14.1.1
        </span>
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is present with a Value of TILED_FULL. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Total Pixel Matrix Focal Planes (0048,0303) describes the number of focal planes separately encoded, and is distinct from Number of Focal Planes (0048,0013), which describes in what manner different focal planes were combined into a single encoded plane (focus stacking).
        </p>
       </div>
