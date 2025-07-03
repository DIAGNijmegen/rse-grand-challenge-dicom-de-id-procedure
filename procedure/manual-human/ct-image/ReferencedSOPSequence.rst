-------------------------------------
Referenced SOP Sequence | (0008,1199)
-------------------------------------
:Action: Keep (K)
:Justication: Required, child elements of this sequence are handled separately
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - patient [Mandatory (M)] [Required with valid value (1)]::

       <p>
        References to object Instances.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>
