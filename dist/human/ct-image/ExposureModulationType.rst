--------------------------------------
Exposure Modulation Type | (0018,9323)
--------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        A label describing the type of exposure modulation used for the purpose of limiting the dose.
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
           NONE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A label describing the type of exposure modulation used for the purpose of limiting the dose.
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
           NONE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
