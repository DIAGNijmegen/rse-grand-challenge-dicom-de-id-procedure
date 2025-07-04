---------------------------------
Pixel Padding Value | (0028,0120)
---------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Single pixel value or one limit (inclusive) of a range of pixel values used in an image to pad to rectangular format or to signal background that may be suppressed or that may be rendered "transparently" when superimposing images. See
        <span href="">
         Section C.7.5.1.1.2
        </span>
        for further explanation.
       </p>
       <p>
        Required if Pixel Padding Range Limit (0028,0121) is present and either Pixel Data (7FE0,0010) or Pixel Data Provider URL (0028,7FE0) is present. May be present otherwise only if Pixel Data (7FE0,0010) or Pixel Data Provider URL (0028,7FE0) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            The Value Representation of this Attribute is determined by the Value of Pixel Representation (0028,0103).
           </p>
          </li>
          <li>
           <p>
            This Attribute is not used in Presentation State Instances; there is no means in a Presentation State to "override" any Pixel Padding Value (0028,0120) specified in the referenced images.
           </p>
          </li>
          <li>
           <p>
            This Attribute does apply to RT Dose and Segmentation Instances, since they include Pixel Data.
           </p>
          </li>
          <li>
           <p>
            This Attribute does not apply when Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are used instead of Pixel Data (7FE0,0010); Float Pixel Padding Value (0028,0122) or Double Float Pixel Padding Value (0028,0123), respectively, are used instead, and defined at the Image, not the Equipment, level.
           </p>
          </li>
          <li>
           <p>
            Only a single Value is allowed for this Attribute, so it only applies to images with Samples per Pixel (0028,0002) of 1, i.e., images with a Photometric Interpretation (0028,0004) of MONOCHROME1, MONOCHROME2 or PALETTE COLOR. See
            <span href="">
             Section C.7.5.1.1.2
            </span>
            for details.
           </p>
          </li>
         </ol>
        </div>
       </div>
