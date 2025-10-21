-----------------------------
Slice Thickness | (0018,0050)
-----------------------------
:Action: Keep (K)
:Justication: Generally required for viewers
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal reconstructed slice thickness (for tomographic imaging) or depth of field (for optical non-tomographic imaging), in mm.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.3.1
        </span>
        for further explanation.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Depth of field may be an extended depth of field created by focus stacking (see
         <span href="">
          Section C.8.12.4
         </span>
         ).
        </p>
       </div>
       <p>
        Required if:
       </p>
       <div>
        <ul>
         <li>
          <p>
           Volumetric Properties (0008,9206) is VOLUME or SAMPLED, and Image Type (0008,0008) Value 3 is not LABEL or OVERVIEW, or
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
           SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.77.1.5.8" (Ophthalmic Optical Coherence Tomography B-scan Volume Analysis Storage SOP Class).
          </p>
         </li>
        </ul>
       </div>
       <p>
        May be present otherwise, if
       </p>
       <div>
        <ul>
         <li>
          <p>
           SOP Class UID (0008,0016) is not "1.2.840.10008.5.1.4.1.1.481.23" (Enhanced RT Image Storage), and
          </p>
         </li>
         <li>
          <p>
           SOP Class UID (0008,0016) is not "1.2.840.10008.5.1.4.1.1.481.24" (Enhanced Continuous RT Image Storage).
          </p>
         </li>
        </ul>
       </div>
       <h3>
        Note
       </h3>
       <p>
        Part of the Pixel Measures Functional Group Macro with usage: M
       </p>
