-------------------------------------
In-concatenation Number | (0020,9162)
-------------------------------------
:Action: Keep (K)
:Justication: Keeps the concatenation internally consistent
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifier for one SOP Instance belonging to a Concatenation. See
        <span href="">
         Section C.7.6.16.2.2.4
        </span>
        for further specification. The first Instance in a Concatenation (that with the lowest Concatenation Frame Offset Number (0020,9228) Value) shall have an In-concatenation Number (0020,9162) Value of 1, and subsequent Instances shall have Values monotonically increasing by 1.
       </p>
       <p>
        Required if Concatenation UID (0020,9161) is present.
       </p>
