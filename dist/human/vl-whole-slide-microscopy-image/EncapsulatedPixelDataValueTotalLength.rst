--------------------------------------------------------
Encapsulated Pixel Data Value Total Length | (7FE0,0003)
--------------------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Optional (3)]::

       <p>
        The length of the pixel data bit stream encapsulated in Pixel Data (7FE0,0010), in bytes, when all the fragments have been combined, not including any trailing padding to even length in the last Fragment added for encapsulation.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Value will depend on the Transfer Syntax in which the Pixel Data (7FE0,0010) is encoded, and may need to be updated depending on the Transfer Syntax negotiated and selected for a particular transfer. See
         <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_8.2.html#sect_8.2" target="_blank">
          PS3.5 Section 8.2 “Native or Encapsulated Format Encoding”
         </a>
         .
        </p>
       </div>
