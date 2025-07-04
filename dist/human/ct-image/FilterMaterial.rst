-----------------------------
Filter Material | (0018,7050)
-----------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The X-Ray absorbing material used in the filter. May be multi-valued.
       </p>
       <p>
        See
        <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_P.html#chapter_P" target="_blank">
         Annex P “Correspondence of X-Ray Filter Material Codes and Defined Terms” in PS3.16
        </a>
        for Defined Terms.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The X-Ray absorbing material used in the filter. May be multi-valued.
       </p>
       <p>
        See
        <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_P.html#chapter_P" target="_blank">
         Annex P “Correspondence of X-Ray Filter Material Codes and Defined Terms” in PS3.16
        </a>
        for Defined Terms.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         At least one Value is required to be present. If a combination of materials is used, they may be listed using multiple Values, or a custom Value may be used to represent a proprietary combination of materials
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL, and the Value of Filter Type (0018,1160) is other than NONE. May be present otherwise.
       </p>
