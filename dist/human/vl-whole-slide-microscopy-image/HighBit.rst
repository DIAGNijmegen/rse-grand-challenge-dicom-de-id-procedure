----------------------
High Bit | (0028,0102)
----------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Most significant bit for pixel sample data. Each sample shall have the same high bit. High Bit (0028,0102) shall be one less than Bits Stored (0028,0101). See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#PS3.5" target="_blank">
         PS3.5
        </a>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Most significant bit for pixel sample data. Each sample shall have the same high bit. High Bit (0028,0102) shall be one less than Bits Stored (0028,0101). See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#PS3.5" target="_blank">
         PS3.5
        </a>
        for further explanation.
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Most significant bit for pixel sample data. High Bit (0028,0102) shall be one less than Bits Stored (0028,0101).
       </p>
