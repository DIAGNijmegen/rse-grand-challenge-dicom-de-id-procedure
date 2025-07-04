-------------------------------------
Deidentification Action | (0008,0307)
-------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Recommended action to be performed during de-identification on elements listed in Identifying Private Elements (0008,0306) within this Item.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         A specific type of action is suggested in order to minimize the impact of de-identification on the behavior of recipients that use the Private Data Elements.
        </p>
       </div>
       <div>
        <p>
         <strong>
          Enumerated Values:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           D
          </span>
         </dt>
         <dd>
          <p>
           replace with a non-zero length value that may be a dummy value and consistent with the VR
          </p>
         </dd>
         <dt>
          <span>
           Z
          </span>
         </dt>
         <dd>
          <p>
           replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR
          </p>
         </dd>
         <dt>
          <span>
           X
          </span>
         </dt>
         <dd>
          <p>
           remove
          </p>
         </dd>
         <dt>
          <span>
           U
          </span>
         </dt>
         <dd>
          <p>
           replace with a non-zero length UID that is internally consistent within a set of Instance
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            No C (clean) action is specified, since replacement with values of similar meaning known not to contain identifying information and consistent with the VR requires an understanding of the meaning of the value of the element. Whether or not to clean rather than remove or replace values is at the discretion of the implementer.
           </p>
          </li>
          <li>
           <p>
            No suggested dummy value is provided, since the encoding of the value would depend on the VR of the Data Element.
           </p>
          </li>
          <li>
           <p>
            Further explanation of these actions can be found in
            <span href="">
             PS3.15 Section E.3.1 Clean Pixel Data Option
            </span>
            .
           </p>
          </li>
         </ol>
        </div>
       </div>
