-------------------------------------------------------
Selector Sequence Pointer Private Creator | (0072,0054)
-------------------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the creator of a group of Private Data Elements used to encode Attributes in the Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        This Attribute shall have the same number of Values as Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        For Values of the Selector Sequence Pointer (0072,0052) that are not the Data Element Tag of a Private Attribute, the corresponding Value in Selector Sequence Pointer Private Creator (0072,0054) shall be empty.
       </p>
       <p>
        Required if Selector Sequence Pointer (0072,0052) is present and one or more of the Values of Selector Sequence Pointer (0072,0052) is the Data Element Tag of a Private Attribute.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.2
        </span>
        .
       </p>
