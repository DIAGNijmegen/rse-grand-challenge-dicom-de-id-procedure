-------------------------------------
Referenced Frame Number | (0008,1160)
-------------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>
