----------------------------------
Burned In Annotation | (0028,0301)
----------------------------------
:Action: Keep (K)
:Justication: No image content analysis is done, so it is good to remember this
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        Indicates whether or not image contains sufficient burned in annotation to identify the patient and date the image was acquired.
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
        If this Attribute is absent, then the image may or may not contain burned in annotation.
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Indicates whether or not image contains sufficient burned in annotation to identify the patient.
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
       <div>
        <h3>
         Note
        </h3>
        <p>
         If Specimen Label in Image (0048,0010) Value is YES, Burned In Annotation (0028,0301) might be NO if the label includes only a specimen identifier and not patient identifying data.
        </p>
       </div>
