--------------------------------------------------
Referenced Defined Protocol Sequence | (0018,990C)
--------------------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Defined Procedure Protocol SOP Instance(s) that were used for this Instance.
       </p>
       <p>
        Required if this instance is a Performed Procedure Protocol that resulted from a Defined Procedure Protocol. May be present otherwise.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section 10.41.1
        </span>
        .
       </p>
