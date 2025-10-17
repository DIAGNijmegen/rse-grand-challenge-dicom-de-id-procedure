---------------------------------------------
Dimension Index Private Creator | (0020,9213)
---------------------------------------------
:Action: Keep (K)
:Justication: If present, pointer is likely required
:Basic Profile: N/A
:In Modules:
   - multi-frame-dimension [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the creator of a group of Private Data Elements.
       </p>
       <p>
        Required if the Dimension Index Pointer (0020,9165) Value is the Data Element Tag of a Private Attribute.
       </p>
