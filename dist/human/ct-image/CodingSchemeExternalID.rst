---------------------------------------
Coding Scheme External ID | (0008,0114)
---------------------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The Coding Scheme identifier as defined in an external registry. Required if Coding Scheme is registered and Coding Scheme UID (0008,010C) is not present.
       </p>
