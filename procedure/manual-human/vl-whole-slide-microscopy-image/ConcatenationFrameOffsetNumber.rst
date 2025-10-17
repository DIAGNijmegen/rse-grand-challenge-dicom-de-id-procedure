-----------------------------------------------
Concatenation Frame Offset Number | (0020,9228)
-----------------------------------------------
:Action: Keep (K)
:Justication: Multi-frame meta data
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Offset of the first Frame in a Multi-frame Image of a Concatenation. Logical Frame numbers in a Concatenation can be used across all its SOP Instances. This offset can be applied to the implicit Frame number to find the logical Frame number in a Concatenation. The offset is numbered from zero; i.e., the instance of a Concatenation that begins with the first Frame of the Concatenation has a Concatenation Frame Offset Number (0020,9228) of zero.
       </p>
       <p>
        Required if Concatenation UID (0020,9161) is present.
       </p>
