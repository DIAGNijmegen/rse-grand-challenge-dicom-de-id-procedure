------------------------------------
Presentation LUT Shape | (2050,0020)
------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
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
