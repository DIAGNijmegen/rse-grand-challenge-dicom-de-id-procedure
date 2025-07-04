-------------------------
Person Name | (0040,A123)
-------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: D
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Person name value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is PNAME.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Person name value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is PNAME.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Person name value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is PNAME.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Person name value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is PNAME.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Person name value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is PNAME.
       </p>
