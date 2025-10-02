-------------------------------------------------
Y Offset in Slide Coordinate System | (0040,073A)
-------------------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - microscope-slide-layer-tile-organization [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The Y offset in millimeters from the Origin of the Slide Coordinate System.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The Y offset in mm from the Origin of the Slide Coordinate System. See
        <span href="">
         Figure C.8-16
        </span>
        .
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Plane Position (Slide) Functional Group Macro with usage: C
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is not TILED_FULL; may be present otherwise.
       </p>
