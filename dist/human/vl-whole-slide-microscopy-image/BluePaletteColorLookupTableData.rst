--------------------------------------------------
Blue Palette Color Lookup Table Data | (0028,1203)
--------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Blue Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Blue Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

   - optical-path [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Blue Palette Color Lookup Table Data. Required if segmented data is NOT used in an Image IOD or
        <span href="">
         Color Palette IOD
        </span>
        , or if the IOD is a Presentation State IOD or Segmentation IOD. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>
