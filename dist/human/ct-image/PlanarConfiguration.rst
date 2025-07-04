----------------------------------
Planar Configuration | (0028,0006)
----------------------------------
:Action: Keep (K)
:Justication: Describes crucial data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Indicates whether the pixel data are encoded color-by-plane or color-by-pixel. Required if Samples per Pixel (0028,0002) has a Value greater than 1. See
        <span href="">
         Section C.7.6.3.1.3
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Indicates whether the pixel data are encoded color-by-plane or color-by-pixel. Required if Samples per Pixel (0028,0002) has a Value greater than 1. See
        <span href="">
         Section C.7.6.3.1.3
        </span>
        for further explanation.
       </p>
