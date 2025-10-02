--------------------------------------------------
Block Identifying Information Status | (0008,0303)
--------------------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Specifies whether some or all of the Private Data Elements in the block are safe from identity leakage as defined by
        <span href="">
         PS3.15 Section E.3.10 Retain Safe Private Option
        </span>
        .
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
           SAFE
          </span>
         </dt>
         <dd>
          <p>
           no Data Elements within the block contain identifying information
          </p>
         </dd>
         <dt>
          <span>
           UNSAFE
          </span>
         </dt>
         <dd>
          <p>
           all Data Elements within the block may contain identifying information
          </p>
         </dd>
         <dt>
          <span>
           MIXED
          </span>
         </dt>
         <dd>
          <p>
           some Data Elements within the block may contain identifying information
          </p>
         </dd>
        </dl>
       </div>
