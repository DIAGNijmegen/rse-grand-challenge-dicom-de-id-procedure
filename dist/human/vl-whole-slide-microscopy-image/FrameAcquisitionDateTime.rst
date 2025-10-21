----------------------------------------
Frame Acquisition DateTime | (0018,9074)
----------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: D
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The date and time that the acquisition of data that resulted in this Frame started. See
        <span href="">
         Section C.7.6.16.2.2.1
        </span>
        for further explanation.
       </p>
       <p>
        Required if
       </p>
       <div>
        <ul>
         <li>
          <p>
           Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL, and Dimension Organization Type (0020,9311) is not TILED_FULL, and the SOP Class UID (0008,0016) is not:
          </p>
          <div>
           <ul>
            <li>
             <p>
              "1.2.840.10008.5.1.4.1.1.2.2" (Legacy Converted Enhanced CT Image Storage), or
             </p>
            </li>
            <li>
             <p>
              "1.2.840.10008.5.1.4.1.1.4.4" (Legacy Converted Enhanced MR Image Storage), or
             </p>
            </li>
            <li>
             <p>
              "1.2.840.10008.5.1.4.1.1.128.1" (Legacy Converted Enhanced PET Image Storage), or
             </p>
            </li>
            <li>
             <p>
              "1.2.840.10008.5.1.4.1.1.77.1.6" (VL Whole Slide Microscopy Image Storage)
             </p>
            </li>
           </ul>
          </div>
         </li>
         <li>
          <p>
           or SOP Class UID (0008,0016) is "1.2.840.10008.5.1.4.1.1.6.3" (Photoacoustic Image Storage).
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
        Part of the Frame Content Functional Group Macro with usage: U
       </p>
