--------------------------------------------------
Private Data Element Number of Items | (0008,030B)
--------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Number of Items allowed in a Sequence Data Element.
       </p>
       <p>
        Required if the Value of Private Data Element Value Representation (0008,030A) is SQ.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.7.2
        </span>
        .
       </p>
