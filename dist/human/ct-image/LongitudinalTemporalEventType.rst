----------------------------------------------
Longitudinal Temporal Event Type | (0012,0053)
----------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The type of event to which Longitudinal Temporal Offset from Event (0012,0052) is relative.
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
           ENROLLMENT
          </span>
         </dt>
         <dd>
          <p>
           Relative to enrollment of the subject in the research activity or clinical trial.
          </p>
         </dd>
         <dt>
          <span>
           BASELINE
          </span>
         </dt>
         <dd>
          <p>
           Relative to the baseline imaging Study.
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if Longitudinal Temporal Offset from Event (0012,0052) is present.
       </p>
