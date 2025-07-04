---------------------------------
Patient Orientation | (0020,0020)
---------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Patient direction of the rows and columns of the image. Required if image does not require Image Orientation (Patient) (0020,0037) and Image Position (Patient) (0020,0032) or if image does not require Image Orientation (Slide) (0048,0102). May be present otherwise. See
        <span href="">
         Section C.7.6.1.1.1
        </span>
        for further explanation.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         IODs may have Attributes other than Patient Orientation, Image Orientation, or Image Position (Patient) to describe orientation in which case this Attribute will be zero length.
        </p>
       </div>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Patient Orientation values of the source image.
       </p>
       <p>
        Required if the Value of Spatial Locations Preserved (0028,135A) is REORIENTED_ONLY.
       </p>
