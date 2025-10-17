-------------------------------
Concatenation UID | (0020,9161)
-------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifier of all SOP Instances that belong to the same Concatenation.
       </p>
       <p>
        Required if a group of Multi-frame Image SOP Instances within a Series are part of a Concatenation.
       </p>
