------------------------------
SOP Instance UID | (0008,0018)
------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Uniquely identifies the SOP Instance. See
        <span href="">
         Section C.12.1.1.1
        </span>
        for further explanation. See also
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part04.html#PS3.4" target="_blank">
         PS3.4
        </a>
        .
       </p>
