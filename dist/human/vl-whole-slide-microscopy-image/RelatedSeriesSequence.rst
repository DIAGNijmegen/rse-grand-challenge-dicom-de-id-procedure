-------------------------------------
Related Series Sequence | (0008,1250)
-------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Optional (3)]::

       <p>
        Identification of Series significantly related to this Series.
       </p>
       <p>
        One or more Items are permitted in this Sequence.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            For example, for a combined CT and PET acquisition, the CT images and PET images would be in separate Series that could cross-reference each other with multiple purpose of reference codes meaning same anatomy, simultaneously acquired and same indication.
           </p>
          </li>
          <li>
           <p>
            The related Series may have different Frames of Reference and hence require some sort of registration before spatial coordinates can be directly compared.
           </p>
          </li>
          <li>
           <p>
            This Attribute is not intended for conveying localizer reference information, for which Referenced Image Sequence (0008,1140) should be used.
           </p>
          </li>
         </ol>
        </div>
       </div>
