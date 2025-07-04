----------------------------------------------------------------
Sex Parameters for Clinical Use Category Reference | (0010,0047)
----------------------------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: X
:In Modules:
   - patient-study [User Optional (U)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Reference to a resource that explains or extends the Sex Parameters for Clinical Use Category Code.
       </p>
       <p>
        Required if Sex Parameters for Clinical Use Category Code Sequence (0010,0046) is
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_131232" target="_blank">
         (131232, DCM, "Specified")
        </a>
        . May be present otherwise.
       </p>
