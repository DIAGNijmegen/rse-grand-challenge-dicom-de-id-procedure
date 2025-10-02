---------------------------------------
Frame Extraction Sequence | (0008,1164)
---------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - frame-extraction [Conditional (C)] [Required with valid value (1)]::

       <p>
        Sequence containing details of how this SOP Instance was extracted from a source multi-frame SOP Instance.
       </p>
       <p>
        If this Instance was created from an Instance that contains a Frame Extraction Sequence, then this Sequence shall contain all of the Items from the parent's Frame Extraction Sequence and a new Item that describes this extraction.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
