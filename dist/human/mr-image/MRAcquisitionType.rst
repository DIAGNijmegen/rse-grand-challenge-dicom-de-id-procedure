---------------------------------
MR Acquisition Type | (0018,0023)
---------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - mr-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Identification of data encoding scheme.
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
           2D
          </span>
         </dt>
         <dd>
          <p>
           frequency x phase
          </p>
         </dd>
         <dt>
          <span>
           3D
          </span>
         </dt>
         <dd>
          <p>
           frequency x phase x phase
          </p>
         </dd>
        </dl>
       </div>
