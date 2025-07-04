-----------------------------------
Concept Code Sequence | (0040,A168)
-----------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>
