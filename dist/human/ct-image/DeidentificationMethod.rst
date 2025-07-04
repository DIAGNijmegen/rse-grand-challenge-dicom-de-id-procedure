--------------------------------------
De-identification Method | (0012,0063)
--------------------------------------
:Action: Keep (K)
:Justication: De-identifaction trace, should be kept and extended
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A description or label of the mechanism or method use to remove the Patient's identity. May be multi-valued if successive de-identification steps have been performed.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            This may be used to describe the extent or thoroughness of the de-identification, for example whether or not the de-identification is for a "Limited Data Set" (as per HIPAA Privacy Rule).
           </p>
          </li>
          <li>
           <p>
            The characteristics of the de-identifying equipment and/or the responsible operator of that equipment may be recorded as an additional Item of the Contributing Equipment Sequence (0018,A001) in the
            <span href="">
             SOP Common Module
            </span>
            . De-identifying equipment may use a Purpose of Reference of
            <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_109104" target="_blank">
             (109104, DCM, "De-identifying Equipment")
            </a>
            .
           </p>
          </li>
         </ol>
        </div>
       </div>
       <p>
        Required if Patient Identity Removed (0012,0062) is present and has a Value of YES and De-identification Method Code Sequence (0012,0064) is not present. May be present otherwise.
       </p>
