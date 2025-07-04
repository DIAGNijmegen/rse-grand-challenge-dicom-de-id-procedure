------------------------------------------------------------------------
Water Equivalent Diameter Calculation Method Code Sequence | (0018,1272)
------------------------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The method of calculation of Water Equivalent Diameter (0018,1271).
       </p>
       <p>
        Required if Water Equivalent Diameter (0018,1271) is present.
       </p>
       <p>
        Only a single Item is permitted in this Sequence.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The method of calculation of Water Equivalent Diameter (0018,1271).
       </p>
       <p>
        Required if Water Equivalent Diameter (0018,1271) is present.
       </p>
       <p>
        Only a single Item is permitted in this Sequence.
       </p>
