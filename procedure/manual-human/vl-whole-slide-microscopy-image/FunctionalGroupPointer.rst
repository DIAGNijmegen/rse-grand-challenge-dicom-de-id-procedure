--------------------------------------
Functional Group Pointer | (0020,9167)
--------------------------------------
:Action: Keep (K)
:Justication: If present, pointer is likely required
:Basic Profile: N/A
:In Modules:
   - multi-frame-dimension [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Contains the Data Element Tag of the Functional Group Sequence that contains the Attribute that is referenced by the Dimension Index Pointer (0020,9165).
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.17.1
        </span>
        for further explanation.
       </p>
       <p>
        Required if the Value of Dimension Index Pointer (0020,9165) is the Data Element Tag of an Attribute that is contained within a Functional Group Sequence.
       </p>
