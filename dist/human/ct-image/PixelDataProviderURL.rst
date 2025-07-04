-------------------------------------
Pixel Data Provider URL | (0028,7FE0)
-------------------------------------
:Action: Remove (X)
:Justication: URL to gather pixel data from, DANGER Will Robinson!
:Basic Profile: N/A
:In Modules:
   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A URL of a provider service that supplies the pixel data of the Image.
       </p>
       <p>
        Required if the image is to be transferred in one of the following presentation contexts identified by Transfer Syntax UID:
       </p>
       <div>
        <ul>
         <li>
          <p>
           1.2.840.10008.1.2.4.94 (DICOM JPIP Referenced Transfer Syntax)
          </p>
         </li>
         <li>
          <p>
           1.2.840.10008.1.2.4.95 (DICOM JPIP Referenced Deflate Transfer Syntax)
          </p>
         </li>
        </ul>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The VR of this Data Element has changed from UT to UR.
        </p>
       </div>
