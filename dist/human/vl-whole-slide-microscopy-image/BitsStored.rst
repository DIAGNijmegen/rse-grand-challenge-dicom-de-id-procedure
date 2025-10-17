-------------------------
Bits Stored | (0028,0101)
-------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of bits stored for each pixel sample. Each sample shall have the same number of bits stored. See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#PS3.5" target="_blank">
         PS3.5
        </a>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of bits stored for each pixel sample. Each sample shall have the same number of bits stored. See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#PS3.5" target="_blank">
         PS3.5
        </a>
        for further explanation.
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of bits stored for each pixel sample. Shall be equal to Bits Allocated (0028,0100).
       </p>
