--------------------------------------------
DICOM Media Retrieval Sequence | (0040,E022)
--------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances from Media.
       </p>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), WADO Retrieval Sequence (0040,E023), and WADO-RS Retrieval Sequence (0040,E025) and XDS Retrieval Sequence (0040,E024) are not present. May be present otherwise.
       </p>
       <p>
        This Sequence shall only identify media known to have Instances referenced in Referenced SOP Sequence (0008,1199).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
