---------------------------------------
Manufacturer's Model Name | (0008,1090)
---------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Mandatory in some modules
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer's model name of the device.
       </p>

   - device [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer's model name of the device.
       </p>

   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's model name of the equipment that produced the Composite Instances.
       </p>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's model name of the equipment that contributed to the Composite Instance.
       </p>

   - specimen [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer's model name of the container component.
       </p>
