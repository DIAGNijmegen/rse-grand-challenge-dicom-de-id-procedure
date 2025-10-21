-------------------------------------
Optical Path Identifier | (0048,0106)
-------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - optical-path [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Identifier for the optical path specified in the Sequence Item. The identifier shall be unique for each Item within the Optical Path Sequence.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Uniquely identifies the path described in the Optical Path Sequence (0048,0105) by reference to an Item with the same Optical Path Identifier (0048,0106) Value. See
        <span href="">
         Section C.8.12.5
        </span>
        .
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
