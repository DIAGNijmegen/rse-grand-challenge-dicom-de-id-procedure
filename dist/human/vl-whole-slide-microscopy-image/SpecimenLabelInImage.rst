-------------------------------------
Specimen Label in Image | (0048,0010)
-------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Indicates whether the specimen label is captured in the image.
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
           YES
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           NO
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Shall be YES if Image Type (0008,0008) Value 3 is OVERVIEW or LABEL.
       </p>
       <p>
        Shall be NO if Image Type (0008,0008) Value 3 is THUMBNAIL or VOLUME.
       </p>
