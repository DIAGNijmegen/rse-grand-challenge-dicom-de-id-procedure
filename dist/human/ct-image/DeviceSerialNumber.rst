----------------------------------
Device Serial Number | (0018,1000)
----------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: IOD conformance: sometimes required
:Basic Profile: X/Z/D
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer's serial number of the device.
       </p>

   - device [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer's serial number of the device.
       </p>

   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's serial number of the equipment that produced the Composite Instances.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This identifier corresponds to the device that actually created the images, such as a CR plate reader or a CT console, and may not be sufficient to identify all of the equipment in the imaging chain, such as the generator or gantry or plate.
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's serial number of the equipment that contributed to the Composite Instance.
       </p>
