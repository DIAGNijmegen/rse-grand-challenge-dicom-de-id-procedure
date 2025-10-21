-------------------------------
Rescale Intercept | (0028,1052)
-------------------------------
:Action: Keep (K)
:Justication: Describes crucial data format
:Basic Profile: N/A
:In Modules:
   - whole-slide-microscopy-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The value b in relationship between stored values (SV) and the output units.
       </p>
       <p>
        Output units = m*SV + b.
       </p>
       <p>
        Required if Photometric Interpretation (0028,0004) is MONOCHROME2.
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
           0
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
