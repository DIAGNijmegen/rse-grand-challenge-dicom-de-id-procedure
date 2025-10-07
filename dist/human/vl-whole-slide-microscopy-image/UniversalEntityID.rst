---------------------------------
Universal Entity ID | (0040,0032)
---------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Universal ID: could be traced to all kinds of insitutes or entities
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - specimen [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>
