---------------------------
Patient's Sex | (0010,0040)
---------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Basic Profile
:Basic Profile: Z
:In Modules:
   - patient [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Sex of the named Patient.
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
           M
          </span>
         </dt>
         <dd>
          <p>
           male
          </p>
         </dd>
         <dt>
          <span>
           F
          </span>
         </dt>
         <dd>
          <p>
           female
          </p>
         </dd>
         <dt>
          <span>
           O
          </span>
         </dt>
         <dd>
          <p>
           other
          </p>
         </dd>
        </dl>
       </div>
       <p>
        See Note 2 and Note 3.
       </p>
