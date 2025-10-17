-----------------------------------------
Light Path Filter Pass Band | (0022,0002)
-----------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - optical-path [Mandatory (M)] [Optional (3)]::

       <p>
        Pass band of light path filter(s) in nm. This Attribute has two Values.
                                               The first Value is the shorter and the second Value the longer wavelength relative to the peak.
                                               The Values are for the - 3dB nominal (1/2 of peak) pass through intensity.
       </p>
       <p>
        One of the two Values may be zero length, in which case it is a cutoff filter.
       </p>
