--------------------------
UDI Sequence | (0018,100A)
--------------------------
:Action: Remove (X)
:Justication: [AUTO] Basic Profile
:Basic Profile: X
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Unique Device Identifier (UDI) of the device.
       </p>
       <p>
        One or more Items are permitted in this Sequence.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Multiple Items may be present if the entire equipment has UDIs issued by different Issuing Authorities.
        </p>
       </div>

   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Unique Device Identifier (UDI) of the entire equipment. For example, the entire CT Scanner.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            Multiple Items may be present if the entire equipment has UDIs issued by different Issuing Authorities.
           </p>
          </li>
          <li>
           <p>
            Multiple Items may be present if multiple pieces of equipment were involved in the creation of this Instance, e.g., the DR plate and the DR reader.
           </p>
          </li>
          <li>
           <p>
            This is not intended to contain the UDIs of the components of the equipment, such as the X-Ray tube of the CT scanner. Such information is stored elsewhere and accessible using the UDI of the entire equipment and a date.
           </p>
          </li>
         </ol>
        </div>
       </div>
       <p>
        One or more Items are permitted in this Sequence.
       </p>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Unique Device Identifier (UDI) of the contributing equipment.
       </p>
       <p>
        One or more Items are permitted in this Sequence.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            This is the UDI that corresponds to the entire contributing equipment as described by the other Attributes in the Contributing Equipment Sequence Item. This is not intended to contain the UDIs of sub-components of the contributing equipment.
           </p>
          </li>
          <li>
           <p>
            Multiple Items may be present if the contributing equipment has UDIs issued by different Issuing Authorities.
           </p>
          </li>
         </ol>
        </div>
       </div>
