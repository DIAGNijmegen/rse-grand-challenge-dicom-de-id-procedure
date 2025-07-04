---------------------------------
Query/Retrieve View | (0008,0053)
---------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required if special operation has ever occured to the data.
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The view requested during the C-MOVE operation that resulted in the transfer of this Instance.
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
           CLASSIC
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           ENHANCED
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if the Instance has ever been converted from its source form as the result of a C-MOVE operation with a specific view.
       </p>
