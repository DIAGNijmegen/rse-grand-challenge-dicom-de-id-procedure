-----------------------------------------
Distance Source to Detector | (0018,1110)
-----------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Distance in mm from source to detector center.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This value is traditionally referred to as Source Image Receptor Distance (SID).
        </p>
       </div>
       <p>
        Shall not be present if this Attribute is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Distance in mm from source to detector center. See
        <span href="">
         Section C.8.15.3.6.1
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This value is traditionally referred to as Source Image Receptor Distance (SID).
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
