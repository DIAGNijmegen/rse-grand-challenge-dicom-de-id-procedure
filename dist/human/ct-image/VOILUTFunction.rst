------------------------------
VOI LUT Function | (0028,1056)
------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: N/A
:In Modules:
   - voi-lut [User Optional (U)] [Optional (3)]::

       <p>
        Describes a VOI LUT function to apply to the Values of Window Center (0028,1050) and Window Width (0028,1051).
       </p>
       <p>
        See
        <span href="">
         Section C.11.2.1.3
        </span>
        for further explanation.
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
           LINEAR
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           LINEAR_EXACT
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           SIGMOID
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        When this Attribute is not present, the interpretation of the Values of Window Center (0028,1050) and Window Width (0028,1051) is linear as in
        <span href="">
         Section C.11.2.1.2
        </span>
        .
       </p>
