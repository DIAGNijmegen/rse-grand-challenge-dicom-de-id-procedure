----------------------------------
Instance Creator UID | (0008,0014)
----------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Uniquely identifies device that created the SOP Instance.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         There is no requirement that the Instance Creator UID (0008,0014) be the same as the Device UID (0018,1002) in the
         <span href="">
          General Equipment Module
         </span>
         , though they may be.
        </p>
       </div>
