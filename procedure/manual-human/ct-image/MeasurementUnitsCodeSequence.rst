---------------------------------------------
Measurement Units Code Sequence | (0040,08EA)
---------------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>
