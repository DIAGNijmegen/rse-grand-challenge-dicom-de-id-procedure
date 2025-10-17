--------------------------
Manufacturer | (0008,0070)
--------------------------
:Action: Keep (K)
:Justication: Required, manufacturer might be relevant
:Basic Profile: N/A
:In Modules:
   - enhanced-general-equipment [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Manufacturer of the equipment that produced the Composite Instances.
       </p>

   - general-equipment [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer of the equipment that produced the Composite Instances.
       </p>

   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Manufacturer of the equipment that contributed to the Composite Instance.
       </p>

   - specimen [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer of the container component.
       </p>
