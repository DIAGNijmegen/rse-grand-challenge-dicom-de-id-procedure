------------------------------------
Presentation LUT Shape | (2050,0020)
------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        When present, specifies an identity transformation for the Presentation LUT such that the output of all grayscale transformations, if any, are defined to be in P-Values.
       </p>
       <div>
        <p>
         <strong>
          Enumerated Values:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           IDENTITY
          </span>
         </dt>
         <dd>
          <p>
           output is in P-Values - shall be used if Photometric Interpretation (0028,0004) is MONOCHROME2 or any color photometric interpretation.
          </p>
         </dd>
         <dt>
          <span>
           INVERSE
          </span>
         </dt>
         <dd>
          <p>
           output after inversion is in P-Values - shall be used if Photometric Interpretation (0028,0004) is MONOCHROME1.
          </p>
         </dd>
        </dl>
       </div>
       <p>
        When this Attribute is used with a color photometric interpretation then the luminance component is in P-Values.
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies an identity transformation for the Presentation LUT, such that the output of all grayscale transformations defined in the IOD containing this Module are defined to be P-Values.
       </p>
       <div>
        <p>
         <strong>
          Enumerated Values:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           IDENTITY
          </span>
         </dt>
         <dd>
          <p>
           output is in P-Values.
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if Photometric Interpretation (0028,0004) is MONOCHROME2.
       </p>
