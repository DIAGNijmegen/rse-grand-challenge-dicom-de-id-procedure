---------------------------------------
Local Namespace Entity ID | (0040,0031)
---------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required under some conditions: dummy if present
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>
