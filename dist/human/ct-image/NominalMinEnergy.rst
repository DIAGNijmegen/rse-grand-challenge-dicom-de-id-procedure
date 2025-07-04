--------------------------------
Nominal Min Energy | (0018,9375)
--------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal minimum energy in keV of photons that are integrated/counted by the detector (see
        <span href="">
         Section C.8.2.2.1.1
        </span>
        ). Due to energy resolution limits of the detector, some photons below the nominal minimum may be counted.
       </p>
       <p>
        Required if Multi-energy Detector Type (0018,9372) is PHOTON_COUNTING. May be present otherwise.
       </p>
