-------------------------------------
WADO Retrieval Sequence | (0040,E023)
-------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances available via WADO-URI.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Sequence addresses use of the URI-based Web Access to DICOM Objects. Retrieval via the IHE XDS-I.b RAD-69 Transaction
         <span href="">
          [
          <abbr>
           IHE RAD TF-2
          </abbr>
          ]
         </span>
         is addressed in the XDS Retrieval Sequence (0040,E024).
        </p>
       </div>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), DICOM Media Retrieval Sequence (0040,E022), WADO-RS Retrieval Sequence (0040,E025) and XDS Retrieval Sequence (0040,E024) are not present. May be present otherwise.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
