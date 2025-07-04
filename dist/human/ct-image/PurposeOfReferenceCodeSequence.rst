------------------------------------------------
Purpose of Reference Code Sequence | (0040,A170)
------------------------------------------------
:Action: Remove (X)
:Justication: Def. optional, where required the parent-sequence is user optional
:Basic Profile: N/A
:In Modules:
   - general-reference [User Optional (U)] [Optional (3)]::

       <p>
        Describes the purpose for which the reference is made, that is what role the source Instance(s) played in the derivation of this Instance.
       </p>
       <p>
        Only a single Item single Item is permitted in this Sequence.
       </p>

   - general-series [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Describes the purpose for which the reference is made.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
       <p>
        When absent, implies that the reason for the reference is unknown.
       </p>

   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Describes the purpose for which the related equipment is being referenced.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.5
        </span>
        for further explanation.
       </p>
