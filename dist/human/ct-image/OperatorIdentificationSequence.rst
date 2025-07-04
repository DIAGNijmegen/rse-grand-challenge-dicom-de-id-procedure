----------------------------------------------
Operator Identification Sequence | (0008,1072)
----------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Basic Profile
:Basic Profile: X/D
:In Modules:
   - general-series [Mandatory (M)] [Optional (3)]::

       <p>
        Identification of the operator(s) supporting the Series.
       </p>
       <p>
        One or more Items are permitted in this Sequence. If more than one Item, the number and order shall correspond to the Value of Operators' Name (0008,1070), if present.
       </p>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Identification of the operator(s) of the contributing equipment.
       </p>
       <p>
        One or more Items are permitted in this Sequence.
       </p>
       <p>
        The number and order of Items shall correspond to the number and order of values of Operators' Name (0008,1070), if present.
       </p>
