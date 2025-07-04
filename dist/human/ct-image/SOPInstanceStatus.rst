---------------------------------
SOP Instance Status | (0100,0410)
---------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        A flag that indicates the storage status of the SOP Instance.
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
           NS
          </span>
         </dt>
         <dd>
          <p>
           Not Specified; implies that this SOP Instance has no special storage status, and hence no special actions need be taken
          </p>
         </dd>
         <dt>
          <span>
           OR
          </span>
         </dt>
         <dd>
          <p>
           Original; implies that this is the primary SOP Instance for the purpose of storage, but that it has not yet been authorized for diagnostic use
          </p>
         </dd>
         <dt>
          <span>
           AO
          </span>
         </dt>
         <dd>
          <p>
           Authorized Original; implies that this is the primary SOP Instance for the purpose of storage, which has been authorized for diagnostic use
          </p>
         </dd>
         <dt>
          <span>
           AC
          </span>
         </dt>
         <dd>
          <p>
           Authorized Copy; implies that this is a copy of an Authorized Original SOP Instance; any copies of an Authorized Original should be given the status of Authorized Copy
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Proper use of these flags is specified in Security Profiles. Implementations that do not conform to such Security Profiles may not necessarily handle these flags properly.
        </p>
       </div>
