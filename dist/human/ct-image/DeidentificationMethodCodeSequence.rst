----------------------------------------------------
De-identification Method Code Sequence | (0012,0064)
----------------------------------------------------
:Action: Keep (K)
:Justication: De-identifaction trace, should be kept and extended
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A code describing the mechanism or method use to remove the Patient's identity.
       </p>
       <p>
        One or more Items shall be included in this Sequence. Multiple Items are used if successive de-identification steps have been performed or to describe options of a defined profile.
       </p>
       <p>
        Required if Patient Identity Removed (0012,0062) is present and has a Value of YES and De-identification Method (0012,0063) is not present. May be present otherwise.
       </p>
