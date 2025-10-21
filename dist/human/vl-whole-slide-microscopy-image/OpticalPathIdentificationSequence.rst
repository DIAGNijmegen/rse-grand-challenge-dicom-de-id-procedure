--------------------------------------------------
Optical Path Identification Sequence | (0048,0207)
--------------------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Identifies the optical path characteristics of this Frame.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Optical Path Identification Functional Group Macro with usage: C
       </p>
       <p>
        Required if Dimension Organization Type (0020,9311) is not TILED_FULL; may be present otherwise.
       </p>
