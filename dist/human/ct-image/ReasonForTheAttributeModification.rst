---------------------------------------------------
Reason for the Attribute Modification | (0400,0565)
---------------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: D
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Reason for the Attribute modification.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           COERCE
          </span>
         </dt>
         <dd>
          <p>
           Replace, add or remove values of Attributes such as Patient Name, ID, Accession Number, for example, during import of media from an external institution, or reconciliation against a master patient index.
          </p>
         </dd>
         <dt>
          <span>
           CORRECT
          </span>
         </dt>
         <dd>
          <p>
           Replace or remove incorrect values, or add correct values, such as Patient Name or ID, for example, when incorrect worklist item was chosen or operator input error.
          </p>
         </dd>
         <dt>
          <span>
           CONVERT
          </span>
         </dt>
         <dd>
          <p>
           Replace, add, or remove values of Attributes during a conversion, for example, of private DICOM objects to a standard SOP Class.
          </p>
         </dd>
        </dl>
       </div>
