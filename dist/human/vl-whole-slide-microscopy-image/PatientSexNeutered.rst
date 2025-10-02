------------------------------------
Patient's Sex Neutered | (0010,2203)
------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: X/Z
:In Modules:
   - patient-study [User Optional (U)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Whether or not a procedure has been performed in an effort to render the Patient sterile.
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
           ALTERED
          </span>
         </dt>
         <dd>
          <p>
           Altered/Neutered
          </p>
         </dd>
         <dt>
          <span>
           UNALTERED
          </span>
         </dt>
         <dd>
          <p>
           Unaltered/intact
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         If this Attribute is present but has no Value then the status is unknown.
        </p>
       </div>
       <p>
        Required if Patient is a non-human organism. May be present otherwise.
       </p>
