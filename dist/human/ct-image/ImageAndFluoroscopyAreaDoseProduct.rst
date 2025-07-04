-----------------------------------------------------
Image and Fluoroscopy Area Dose Product | (0018,115E)
-----------------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        X-Ray dose, measured in dGy*cm*cm, to which the patient was exposed for the acquisition of the entire Irradiation Event from which this image was reconstructed.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            All of the images reconstructed from the same Irradiation Event will have the same Value for this Attribute, which is the total for the Irradiation Event, which is repeated in each image, regardless of whether or not the Irradiation Event UID (0008,3010) is present with a Value in the
            <span href="">
             Multi-frame Dimension Module
            </span>
            . I.e., the values for each image should not be summed. The sum of the area dose products of all encoded Irradiation Events may not result in the total area dose product to which the patient was exposed.
           </p>
          </li>
          <li>
           <p>
            This may be an estimated value based on assumptions about the Patient’s body size and habitus.
           </p>
          </li>
          <li>
           <p>
            This value is required by
            <span href="">
             [
             <abbr>
              IEC 60601-2-63
             </abbr>
             ]
            </span>
            .
           </p>
          </li>
         </ol>
        </div>
       </div>

   - multi-energy-ct-image [Conditional (C)] [Optional (3)]::

       <p>
        X-Ray dose, measured in dGy*cm*cm, to which the patient was exposed for the acquisition of the entire Irradiation Event from which this image and Frame was reconstructed.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            All of the images and Frames reconstructed from the same Irradiation Event will have the same Value for this Attribute, which is the total for the Irradiation Event, which is repeated in each image or Frame, regardless of whether or not the Irradiation Event UID (0008,3010) is present with a Value in the
            <span href="">
             Irradiation Event Identification Macro
            </span>
            . I.e., the values for each image or Frame should not be summed. The sum of the area dose products for each Irradiation Event may not result in the total area dose product to which the patient was exposed.
           </p>
          </li>
          <li>
           <p>
            This may be an estimated value based on assumptions about the patient’s body size and habitus.
           </p>
          </li>
          <li>
           <p>
            This value is required by
            <span href="">
             [
             <abbr>
              IEC 60601-2-63
             </abbr>
             ]
            </span>
            .
           </p>
          </li>
         </ol>
        </div>
       </div>
