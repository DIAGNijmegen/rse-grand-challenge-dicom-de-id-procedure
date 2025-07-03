--------------------------------------
Certified Timestamp Type | (0400,0305)
--------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The type of certified timestamp used in Certified Timestamp (0400,0310). Required if Certified Timestamp (0400,0310) is present.
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
           CMS_TSP
          </span>
         </dt>
         <dd>
          <p>
           Internet X.509 Public Key Infrastructure Time Stamp Protocol
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Digital Signature Security Profiles (see
         <a href="http://dicom.nema.org/medical/dicom/current/output/html/part15.html#PS3.15" target="_blank">
          PS3.15
         </a>
         ) may require the use of a restricted subset of these terms.
        </p>
       </div>
