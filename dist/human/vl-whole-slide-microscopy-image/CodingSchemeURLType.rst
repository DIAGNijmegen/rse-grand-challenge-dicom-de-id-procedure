------------------------------------
Coding Scheme URL Type | (0008,010A)
------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The type of the resource related to the Coding Scheme at the Coding Scheme URL (0008,010E).
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
           DOC
          </span>
         </dt>
         <dd>
          <p>
           The resource is human-readable information describing the Coding Scheme.
          </p>
         </dd>
         <dt>
          <span>
           OWL
          </span>
         </dt>
         <dd>
          <p>
           The resource contains an OWL file that contains a representation of the Coding Scheme.
          </p>
         </dd>
         <dt>
          <span>
           CSV
          </span>
         </dt>
         <dd>
          <p>
           The resource contains a comma separated value text file that contains a representation of the Coding Scheme.
          </p>
         </dd>
         <dt>
          <span>
           FHIR
          </span>
         </dt>
         <dd>
          <p>
           The resource is a FHIR CodingScheme, e.g., as would be referred to in the Coding.system element of a FHIR Coding resource.
          </p>
         </dd>
        </dl>
       </div>
