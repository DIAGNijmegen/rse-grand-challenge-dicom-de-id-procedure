---------------------------------------------
Manufacturer's Device Class UID | (0018,100B)
---------------------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's Unique Identifier (UID) for the class of the device.
       </p>
       <p>
        A class is a manufacturer-specific grouping concept with no DICOM-defined scope or criteria. A class is independent from a marketing-defined make, model or version.
       </p>
       <p>
        A class allows grouping of devices with a similar set of capabilities.
       </p>
       <p>
        This Attribute may be multi-valued if this device is a member of more than one class.
       </p>
