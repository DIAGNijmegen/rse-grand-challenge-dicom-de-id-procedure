----------------------------------
Decomposition Method | (0018,937E)
----------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Required with valid value (1)]::

       <p>
        Method used to decompose the acquired Multi-energy CT data into basis data.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           PROJECTION_BASED
          </span>
         </dt>
         <dd>
          <p>
           The acquired projection data was fully decomposed into basis projection data (i.e. sinograms).
          </p>
         </dd>
         <dt>
          <span>
           IMAGE_BASED
          </span>
         </dt>
         <dd>
          <p>
           The acquired projection data was fully reconstructed into images before being decomposed into basis image data.
          </p>
         </dd>
         <dt>
          <span>
           HYBRID
          </span>
         </dt>
         <dd>
          <p>
           The acquired projection data was reconstructed using knowledge in both projection and image space to produce basis image data. Decomposition and image reconstruction may be performed in a one-step approach.
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            Basis images and basis projection data are not necessarily instantiated as DICOM Instances.
           </p>
          </li>
          <li>
           <p>
            There may be additional processing steps (e.g. linear combination of basis data) creating the result image.
           </p>
          </li>
         </ol>
        </div>
       </div>
