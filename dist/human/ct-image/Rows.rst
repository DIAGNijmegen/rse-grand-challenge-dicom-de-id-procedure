------------------
Rows | (0028,0010)
------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of rows in the image.
       </p>
       <p>
        Shall be an exact multiple of the vertical downsampling factor if any of the samples (planes) are encoded downsampled in the vertical direction for pixel data encoded in a Native (uncompressed) format. E.g., required to be an even value for a Photometric Interpretation (0028,0004) of YBR_FULL_422.
       </p>

   - image-pixel [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of rows in the image.
       </p>
       <p>
        Shall be an exact multiple of the vertical downsampling factor if any of the samples (planes) are encoded downsampled in the vertical direction for pixel data encoded in a Native (uncompressed) format. E.g., required to be an even value for a Photometric Interpretation (0028,0004) of YBR_FULL_422.
       </p>
