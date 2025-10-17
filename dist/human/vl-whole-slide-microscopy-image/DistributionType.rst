-------------------------------
Distribution Type | (0012,0084)
-------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The type of distribution for which consent to distribute has been granted.
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
           NAMED_PROTOCOL
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           RESTRICTED_REUSE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           PUBLIC_RELEASE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        See
        <span href="">
         Section C.7.2.3.1.2
        </span>
        .
       </p>
       <p>
        Required if Consent for Distribution Flag (0012,0085) equals YES or WITHDRAWN.
       </p>
