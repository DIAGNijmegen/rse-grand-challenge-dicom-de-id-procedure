---------------------------------------
Image Orientation (Slide) | (0048,0102)
---------------------------------------
:Action: Keep (K)
:Justication: Criticial image meta data
:Basic Profile: N/A
:In Modules:
   - microscope-slide-layer-tile-organization [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The direction cosines of the first row and the first column of the total pixel matrix with respect to the Slide Coordinate System Frame of Reference. See
        <span href="">
         Section C.8.12.14.1.2
        </span>
        .
       </p>
       <p>
        Required if Plane Position (Slide) Sequence (0048,021A) is present within a Functional Group Sequence or Dimension Organization Type (0020,9311) is present with a Value of TILED_FULL. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This condition will always be satisfied when this Module is included in the Whole Slide Microscopy Image IOD.
        </p>
       </div>
