------------------------
Device UID | (0018,1002)
------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Unique identifier of the equipment that produced the Composite Instances.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            If present in an SR object, the value is expected to be the same as the
            <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_121012" target="_blank">
             (121012, DCM, "Device Observer UID")
            </a>
            in
            <span href="">
             TID 1004 “Device Observer Identifying Attributes”
            </span>
            .
           </p>
          </li>
          <li>
           <p>
            There is no requirement that the Device UID (0018,1002) be the same as the Instance Creator UID (0008,0014) in the
            <span href="">
             SOP Common Module
            </span>
            , though they may be.
           </p>
          </li>
         </ol>
        </div>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Unique identifier of the contributing equipment.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         There is no requirement that this Device UID (0018,1002) be the same as the Instance Creator UID (0008,0014) in the
         <span href="">
          SOP Common Module
         </span>
         , though it may be.
        </p>
       </div>
