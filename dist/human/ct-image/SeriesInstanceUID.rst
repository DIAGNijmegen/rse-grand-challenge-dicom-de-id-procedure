---------------------------------
Series Instance UID | (0020,000E)
---------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - common-instance-reference [User Optional (U)] [Required with valid value (1)]::

       <p>
        Unique identifier of the Series containing the referenced Instances.
       </p>

   - general-series [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Unique identifier of the Series.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Unique identifier for the Series that is part of the Study identified in Study Instance UID (0020,000D), if present, and contains the referenced object Instance(s).
       </p>
       <p>
        Required if Type of Instances (0040,E020) is DICOM and the Information Model of the referenced Instance contains the Series IE.
       </p>
