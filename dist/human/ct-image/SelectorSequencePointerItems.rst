---------------------------------------------
Selector Sequence Pointer Items | (0074,1057)
---------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the Item indices in the Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        This Attribute shall have the same number of Values as the Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        The Value 1 identifies the first Item of the corresponding Sequence. The Value 0 identifies all Items of the corresponding Sequence.
       </p>
       <p>
        Required if Selector Sequence Pointer (0072,0052) is present.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.1
        </span>
        .
       </p>
