--------------------------------
Rotation Direction | (0018,1140)
--------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Direction of rotation of the source when relevant, about nearest principal axis of equipment.
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
           CW
          </span>
         </dt>
         <dd>
          <p>
           clockwise
          </p>
         </dd>
         <dt>
          <span>
           CC
          </span>
         </dt>
         <dd>
          <p>
           counter clockwise
          </p>
         </dd>
        </dl>
       </div>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Direction of rotation of the source about the gantry, as viewed while facing the gantry where the table enters the gantry.
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
           CW
          </span>
         </dt>
         <dd>
          <p>
           clockwise
          </p>
         </dd>
         <dt>
          <span>
           CC
          </span>
         </dt>
         <dd>
          <p>
           counter clockwise
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>
       <p>
        Otherwise may be present if Frame Type (0008,9007) Value 1 of this Frame is DERIVED or Image Type (0008,0008) Value 1 is DERIVED, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>
