-------------------------------------
Synchronization Trigger | (0018,106A)
-------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - synchronization [Conditional (C)] [Required with valid value (1)]::

       <p>
        Data acquisition synchronization with external equipment
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
           SOURCE
          </span>
         </dt>
         <dd>
          <p>
           this equipment provides synchronization channel or trigger to other equipment
          </p>
         </dd>
         <dt>
          <span>
           EXTERNAL
          </span>
         </dt>
         <dd>
          <p>
           this equipment receives synchronization channel or trigger from other equipment
          </p>
         </dd>
         <dt>
          <span>
           PASSTHRU
          </span>
         </dt>
         <dd>
          <p>
           this equipment receives synchronization channel or trigger and forwards it
          </p>
         </dd>
         <dt>
          <span>
           NO TRIGGER
          </span>
         </dt>
         <dd>
          <p>
           data acquisition not synchronized by common channel or trigger
          </p>
         </dd>
        </dl>
       </div>
