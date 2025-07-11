------------------------------------
XDS Retrieval Sequence | (0040,E024)
------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances using the IHE XDS-I.b RAD-69 Transaction.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Retrieval via WADO-URI is addressed by the WADO Retrieval Sequence (0040,E023). Retrieval via WADO-RS is addressed by the WADO-RS Retrieval Sequence (0040,E025).
        </p>
       </div>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), DICOM Media Retrieval Sequence (0040,E022), WADO-RS Retrieval Sequence (0040,E025) and WADO Retrieval Sequence (0040,E023) are not present. May be present otherwise.
       </p>
       <p>
        This Sequence shall only identify repositories known to have Instances referenced in Referenced SOP Sequence (0008,1199).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
