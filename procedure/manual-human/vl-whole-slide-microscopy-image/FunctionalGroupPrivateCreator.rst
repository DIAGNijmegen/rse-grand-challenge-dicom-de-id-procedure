----------------------------------------------
Functional Group Private Creator | (0020,9238)
----------------------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: Good to replace consistently, might be relevant
:Basic Profile: N/A
:In Modules:
   - multi-frame-dimension [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the creator of a group of Private Data Elements.
       </p>
       <p>
        Required if the Functional Group Pointer (0020,9167) Value is the Data Element Tag of a Private Attribute.
       </p>
