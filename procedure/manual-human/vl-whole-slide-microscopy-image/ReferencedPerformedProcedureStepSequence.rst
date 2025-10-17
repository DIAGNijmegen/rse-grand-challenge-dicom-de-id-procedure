----------------------------------------------------------
Referenced Performed Procedure Step Sequence | (0008,1111)
----------------------------------------------------------
:Action: Keep (K)
:Justication: Required for WSI
:Basic Profile: X/Z/D
:In Modules:
   - general-series [Mandatory (M)] [Optional (3)]::

       <p>
        Uniquely identifies the Performed Procedure Step SOP Instance to which the Series is related.
       </p>
       <p>
        Only a single Item is permitted in this Sequence.
       </p>

   - whole-slide-microscopy-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Uniquely identifies the Performed Procedure Step SOP Instance to which the Series is related.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if a Performed Procedure Step SOP Class was involved in the creation of this Series.
       </p>
