---------------------------
Barcode Value | (2200,0005)
---------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: Slide ID
:Basic Profile: X/Z
:In Modules:
   - slide-label [Conditional (C)] [Required; value may be empty (2)]::

       <p>
        Barcode interpreted from the scanned slide label.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This may be the same as Container Identifier (0040,0512).
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Barcode interpreted from a scanned label.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            In the case of a scanned patient label, this may be the same as Patient ID (0010,0020), but it is included in an Instance level Module rather than a Patient level Module since barcodes may also be used to identify lower level entities. This might be obtained by scanning the patient's wrist band, request form, or extracting a burned-in label from the image pixel data, for example.
           </p>
          </li>
          <li>
           <p>
            In the case of a scanned slide label, this may be the same as Container Identifier (0040,0512) in the
            <span href="">
             Specimen Module
            </span>
            .
           </p>
          </li>
         </ol>
        </div>
       </div>
