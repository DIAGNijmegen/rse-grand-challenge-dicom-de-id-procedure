---------------------------
Pixel Spacing | (0028,0030)
---------------------------
:Action: Keep (K)
:Justication: Describes crucial data format
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Physical distance in the imaging target (patient, specimen, or phantom) between the centers of each pixel, specified by a numeric pair - adjacent row spacing (delimiter) adjacent column spacing in mm. See
        <span href="">
         Section 10.7.1.3
        </span>
        for further explanation of the order of the Values.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            In the case of CT images with an Acquisition Type (0018,9302) of CONSTANT_ANGLE, the pixel spacing is that in a plane normal to the central ray of the diverging X-Ray beam as it passes through the data collection center.
           </p>
          </li>
          <li>
           <p>
            In the case when SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.481.23" (Enhanced RT Image Storage) or "1.2.840.10008.5.1.4.1.1.481.24" (Enhanced Continuous RT Image Storage), the pixel spacing is defined on the x/y plane at z = 0 of the Image Receptor Coordinate System.
           </p>
          </li>
          <li>
           <p>
            In the case when SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.77.1.5.4" (Ophthalmic Tomography Image Storage) or "1.2.840.10008.5.1.4.1.1.77.1.5.8" (Ophthalmic Optical Coherence Tomography B-scan Volume Analysis Storage SOP Class), the pixel spacing is specified as nominal because the physical distance may vary across the field of the images.
           </p>
          </li>
         </ol>
        </div>
       </div>
       <p>
        Required if:
       </p>
       <div>
        <ul>
         <li>
          <p>
           Volumetric Properties (0008,9206) is other than DISTORTED or SAMPLED, and Image Type (0008,0008) Value 3 is not LABEL or OVERVIEW, or
          </p>
         </li>
         <li>
          <p>
           SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.66.4" (Segmentation Storage SOP Class) and Frame of Reference UID (0020,0052) is present, or
          </p>
         </li>
         <li>
          <p>
           SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.77.1.5.4" (Ophthalmic Tomography Image Storage) and Ophthalmic Volumetric Properties Flag (0022,1622) is YES, or
          </p>
         </li>
         <li>
          <p>
           SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.77.1.5.8" (Ophthalmic Optical Coherence Tomography B-scan Volume Analysis Storage SOP Class), or
          </p>
         </li>
         <li>
          <p>
           SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.481.23" (Enhanced RT Image Storage), or
          </p>
         </li>
         <li>
          <p>
           SOP Class UID (0008,0016) is"1.2.840.10008.5.1.4.1.1.481.24" (Enhanced Continuous RT Image Storage).
          </p>
         </li>
        </ul>
       </div>
       <p>
        May be present otherwise.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Pixel Measures Functional Group Macro with usage: M
       </p>
