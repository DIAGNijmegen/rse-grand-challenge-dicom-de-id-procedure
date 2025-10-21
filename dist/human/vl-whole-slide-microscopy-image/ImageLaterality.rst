------------------------------
Image Laterality | (0020,0062)
------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        Laterality of (possibly paired) body part (as described in Anatomic Region Sequence (0008,2218)) examined.
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
           R
          </span>
         </dt>
         <dd>
          <p>
           right
          </p>
         </dd>
         <dt>
          <span>
           L
          </span>
         </dt>
         <dd>
          <p>
           left
          </p>
         </dd>
         <dt>
          <span>
           U
          </span>
         </dt>
         <dd>
          <p>
           unpaired
          </p>
         </dd>
         <dt>
          <span>
           B
          </span>
         </dt>
         <dd>
          <p>
           both left and right
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Shall be consistent with any laterality information contained in Primary Anatomic Structure Modifier Sequence (0008,2230) and/or Laterality (0020,0060), if present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Laterality (0020,0060) is a Series level Attribute and must be the same for all Images in the Series, hence it must be absent if Image Laterality (0020,0062) has different Values for Images in the same Series.
        </p>
       </div>
