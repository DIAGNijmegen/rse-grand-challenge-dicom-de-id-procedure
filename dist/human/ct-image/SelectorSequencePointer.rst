---------------------------------------
Selector Sequence Pointer | (0072,0052)
---------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Contains the Data Element Tags of the path to the Sequence that contains the Attribute that is identified by Selector Attribute (0072,0026) or to the Item(s) to be selected in Selector Sequence Pointer Items (0074,1057).
       </p>
       <p>
        This Attribute shall have the same number of Values as the level of nesting of Selector Attribute (0072,0026) or the selected Item(s).
       </p>
       <p>
        Required if Selector Attribute (0072,0026) is nested in one or more Sequences or is absent.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.1
        </span>
        .
       </p>
