------------------------------
Number of Frames | (0028,0008)
------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of Frames in a Multi-frame Image. See
        <span href="">
         Section C.7.6.6.1.1
        </span>
        for further explanation.
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Number of Frames in a Multi-frame Image.
       </p>
       <div>
        <p>
         <strong>
          Enumerated Values if Image Type (0008,0008) Value 3 is THUMBNAIL, LABEL or OVERVIEW:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           1
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Enumerated Value of 1 previously applied to Image Type (0008,0008) Value 3 of LOCALIZER, which has been retired. See
         <a href="http://dicom.nema.org/medical/dicom/2021c/output/pdf/part03.pdf">
          PS3.3-2021c
         </a>
         .
        </p>
       </div>
