--------------------------------------
Dimension Index Sequence | (0020,9222)
--------------------------------------
:Action: Keep (K)
:Justication: Multi-frame meta data
:Basic Profile: N/A
:In Modules:
   - multi-frame-dimension [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Sequence containing the indices used to specify the dimension of the multi-frame object.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is absent or not TILED_FULL. May be present otherwise.
       </p>
