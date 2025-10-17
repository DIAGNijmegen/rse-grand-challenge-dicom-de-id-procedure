-----------------------------------------------
Channel Description Code Sequence | (0022,001A)
-----------------------------------------------
:Action: Keep (K)
:Justication: Crucial acquisition data
:Basic Profile: N/A
:In Modules:
   - optical-path [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Describes the light color sensed for each channel to generate the image.
       </p>
       <p>
        Required if this differs from the natural interpretation.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            For MONOCHROME2, the natural interpretation is the full visible light spectrum. A full spectrum sensor may be presented with light of only a single color based on illumination and filters.
           </p>
          </li>
          <li>
           <p>
            Equipment may use a color Photometric Interpretation (RGB, YBR) as a container representing up to 3 channels of any detected wavelength.
           </p>
          </li>
         </ol>
        </div>
       </div>
       <p>
        Shall have the same number of Items as the Value of Samples per Pixel Used (0028,0003) if present, or otherwise the Value of Samples per Pixel (0028,0002). The channels shall be described in the order in which the channels are encoded.
       </p>
