-----------------------------------
Quality Control Image | (0028,0300)
-----------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        Indicates whether or not quality control material (such as calibration or control material, or a phantom) is present in this image.
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
           the image contains only quality control material
          </p>
         </dd>
         <dt>
          <span>
           NO
          </span>
         </dt>
         <dd>
          <p>
           the image does not contain quality control material
          </p>
         </dd>
         <dt>
          <span>
           BOTH
          </span>
         </dt>
         <dd>
          <p>
           the image contains both subject (patient) and quality control information
          </p>
         </dd>
        </dl>
       </div>
       <p>
        If this Attribute is absent, then the image may or may not be a quality control or phantom image. The phantom device or quality control material in the image can be described using the
        <span href="">
         Device Module
        </span>
        . See
        <span href="">
         Section C.7.6.12
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Examples of the presence of both subject and quality control information include:
        </p>
        <div>
         <ul>
          <li>
           <p>
            presence of objects of known density in radiographic images for calibration
           </p>
          </li>
          <li>
           <p>
            presence of control material for immunohistochemistry within slide images
           </p>
          </li>
         </ul>
        </div>
       </div>
