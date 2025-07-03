-------------------------
Filter Type | (0018,1160)
-------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Type of filter(s) inserted into the X-Ray beam.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Type of filter(s) inserted into the X-Ray beam.
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
           WEDGE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           BUTTERFLY
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           MULTIPLE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           FLAT
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           SHAPED
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           NONE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Multiple type of filters can be expressed by a combination, e.g., BUTTERFLY+WEDGE.
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
