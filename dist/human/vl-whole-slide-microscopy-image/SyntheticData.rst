----------------------------
Synthetic Data | (0008,001C)
----------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Whether or not some or all of the content of this instance was made artificially rather than being a faithful representation of acquired data.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            Since synthetic data may be intended for use in training or testing, the data may be otherwise indistinguishable from acquired patient data. For example, the Value of Manufacturer's Model Name (0008,1090) in the Equipment Module may reflect the model, whose output the instance is simulating, even though such a model did not create this instance. Similarly, the Value of KVP (0018,0060) may reflect the technique being simulated even though no x-rays were involved.
           </p>
          </li>
          <li>
           <p>
            The equipment that synthesized the data may be recorded as additional Item(s) of the Contributing Equipment Sequence (0018,A001) in the SOP Common Module. The Purpose of Reference code value of
            <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_109100" target="_blank">
             (109100, DCM, "Synthesizing Equipment")
            </a>
            can be used.
           </p>
          </li>
          <li>
           <p>
            The use of this Attribute to indicate synthetic data is not restricted to images, since any type of SOP Instance may be created artificially
           </p>
          </li>
         </ol>
        </div>
       </div>
       <div>
        <p>
         <strong>
          Enumerated Values:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           YES
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           NO
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        If data with a Synthetic Data (0008,001C) Value of YES is used to derive other content then it is expected that this derived content will also have a Synthetic Data (0008,001C) Value of YES.
       </p>
