-------------------------
ICC Profile | (0028,2000)
-------------------------
:Action: Keep (K)
:Justication: Important viewing specification
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        An ICC Profile encoding the transformation of device-dependent color stored pixel values into PCS-Values.
       </p>
       <p>
        See
        <span href="">
         Section C.11.15.1.1
        </span>
        .
       </p>
       <p>
        When present, defines the color space of color Pixel Data (7FE0,0010) Values, and the output of Palette Color Lookup Table Data (0028,1201-1203).
       </p>
       <p>
        Shall not be present in the top level dataset when the Optical Path Sequence (0048,0105) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            The profile applies only to Pixel Data (7FE0,0010) at the same level of the Data Set and not to any icons nested within Sequences, which may or may not have their own ICC profile specified.
           </p>
          </li>
          <li>
           <p>
            When the
            <span href="">
             Optical Path Module
            </span>
            is used, each optical path (Item of the Optical Path Sequence (0048,0105)) has its own ICC Profile (0028,2000).
           </p>
          </li>
         </ol>
        </div>
       </div>

   - image-pixel [Mandatory (M)] [Optional (3)]::

       <p>
        An ICC Profile encoding the transformation of device-dependent color stored pixel values into PCS-Values.
       </p>
       <p>
        See
        <span href="">
         Section C.11.15.1.1
        </span>
        .
       </p>
       <p>
        When present, defines the color space of color Pixel Data (7FE0,0010) Values, and the output of Palette Color Lookup Table Data (0028,1201-1203).
       </p>
       <p>
        Shall not be present in the top level dataset when the Optical Path Sequence (0048,0105) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            The profile applies only to Pixel Data (7FE0,0010) at the same level of the Data Set and not to any icons nested within Sequences, which may or may not have their own ICC profile specified.
           </p>
          </li>
          <li>
           <p>
            When the
            <span href="">
             Optical Path Module
            </span>
            is used, each optical path (Item of the Optical Path Sequence (0048,0105)) has its own ICC Profile (0028,2000).
           </p>
          </li>
         </ol>
        </div>
       </div>

   - optical-path [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An ICC Profile encoding the transformation of device-dependent stored pixel values into PCS-Values. See
        <span href="">
         Section C.8.12.5.1.4
        </span>
       </p>
       <p>
        Required if Photometric Interpretation (0028,0004) is not MONOCHROME2, or if Palette Color Lookup Table Sequence (0048,0120) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The ICC Profile (0028,2000) in the
         <span href="">
          Image Pixel Description Macro
         </span>
         is not used when the Optical Path Module is used.
        </p>
       </div>
