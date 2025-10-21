----------------------------
Bits Allocated | (0028,0100)
----------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of bits allocated for each pixel sample. Each sample shall have the same number of bits allocated. Bits Allocated (0028,0100) shall be either 1, or a multiple of 8. See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#PS3.5" target="_blank">
         PS3.5
        </a>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of bits allocated for each pixel sample. Each sample shall have the same number of bits allocated. Bits Allocated (0028,0100) shall be either 1, or a multiple of 8. See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#PS3.5" target="_blank">
         PS3.5
        </a>
        for further explanation.
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of bits allocated for each pixel sample.
       </p>
       <div>
        <p>
         <strong>
          Enumerated Values:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           8
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           16
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
