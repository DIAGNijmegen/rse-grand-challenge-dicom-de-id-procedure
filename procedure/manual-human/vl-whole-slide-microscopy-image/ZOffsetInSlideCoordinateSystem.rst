-------------------------------------------------
Z Offset in Slide Coordinate System | (0040,074A)
-------------------------------------------------
:Action: Keep (K)
:Justication: Crucial acq detail
:Basic Profile: N/A
:In Modules:
   - microscope-slide-layer-tile-organization [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Z offset in µm from the image substrate reference plane (i.e., utilized surface of a glass slide).
       </p>
       <p>
        Required if the Z offset is not zero. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The conditional requirement is used because, historically, this Attribute was not present.
        </p>
       </div>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The Z offset in µm from the Origin of the Slide Coordinate System, nominally the surface of the glass slide substrate. See
        <span href="">
         Figure C.8-17
        </span>
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Required even if only a single focal plane was acquired.
        </p>
       </div>
       <h3>
        Note
       </h3>
       <p>
        Part of the Plane Position (Slide) Functional Group Macro with usage: C
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is not TILED_FULL; may be present otherwise.
       </p>
