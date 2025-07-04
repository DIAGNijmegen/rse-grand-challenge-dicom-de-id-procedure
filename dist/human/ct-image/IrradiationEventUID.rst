-----------------------------------
Irradiation Event UID | (0008,3010)
-----------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - general-acquisition [Mandatory (M)] [Optional (3)]::

       <p>
        Unique identification of the irradiation event(s) associated with the acquisition of this instance. See
        <span href="">
         Section C.7.10.1.1.1
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         There is not necessarily a 1:1 relationship between an Irradiation Event and an Acquisition. An Acquisition may not involve the use of ionizing radiation, in which case this Attribute would be absent. A single Acquisition may result from more than one Irradiation Event, e.g., when there are multiple X-Ray sources. More than one Irradiation Event may be involved in a single Acquisition, e.g., when there is a quiescent period between Irradiation Events during which data gathering continues.
        </p>
       </div>
