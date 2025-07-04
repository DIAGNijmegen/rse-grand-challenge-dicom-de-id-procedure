------------------------------
Pregnancy Status | (0010,21C0)
------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: X
:In Modules:
   - patient-study [User Optional (U)] [Optional (3)]::

       <p>
        Describes pregnancy state of Patient.
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
           0001H
          </span>
         </dt>
         <dd>
          <p>
           not pregnant
          </p>
         </dd>
         <dt>
          <span>
           0002H
          </span>
         </dt>
         <dd>
          <p>
           possibly pregnant
          </p>
         </dd>
         <dt>
          <span>
           0003H
          </span>
         </dt>
         <dd>
          <p>
           definitely pregnant
          </p>
         </dd>
         <dt>
          <span>
           0004H
          </span>
         </dt>
         <dd>
          <p>
           unknown
          </p>
         </dd>
        </dl>
       </div>
