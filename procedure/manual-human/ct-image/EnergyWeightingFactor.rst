-------------------------------------
Energy Weighting Factor | (0018,9353)
-------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The weighting factor of the data from this additional source in a multiple energy composition image. This factor incorporates the effects of
       </p>
       <div>
        <ul>
         <li>
          <p>
           the specific X-Ray source and kV value
          </p>
         </li>
         <li>
          <p>
           examination specific characteristics.
          </p>
         </li>
        </ul>
       </div>
       <p>
        Required if one Derivation Code Sequence (0008,9215) Item value is
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_113097" target="_blank">
         (113097, DCM, "Multi-energy proportional weighting")
        </a>
        . May be present otherwise.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The weighting factor of the data from this Sequence Item.
       </p>
       <p>
        Required if Required if Frame Type (0008,9007) Value 4 of this Frame is ENERGY_PROP_WT or Image Type (0008,0008) Value 4 is ENERGY_PROP_WT. May be present otherwise.
       </p>
