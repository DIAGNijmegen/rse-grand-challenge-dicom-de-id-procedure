-------------------------------
Scanning Sequence | (0018,0020)
-------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - mr-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Description of the type of data taken.
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
           SE
          </span>
         </dt>
         <dd>
          <p>
           Spin Echo
          </p>
         </dd>
         <dt>
          <span>
           IR
          </span>
         </dt>
         <dd>
          <p>
           Inversion Recovery
          </p>
         </dd>
         <dt>
          <span>
           GR
          </span>
         </dt>
         <dd>
          <p>
           Gradient Recalled
          </p>
         </dd>
         <dt>
          <span>
           EP
          </span>
         </dt>
         <dd>
          <p>
           Echo Planar
          </p>
         </dd>
         <dt>
          <span>
           RM
          </span>
         </dt>
         <dd>
          <p>
           Research Mode
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Multi-valued, but not all combinations are valid (e.g., SE/GR, etc.).
        </p>
       </div>
