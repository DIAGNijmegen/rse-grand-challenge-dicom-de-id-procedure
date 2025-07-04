-------------------------------
X-Ray Detector ID | (0018,9371)
-------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: D
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Required with valid value (1)]::

       <p>
        Identifier of the physical X-Ray detector. This might be the serial number.
       </p>
       <p>
        When a single detector discriminates different energies, the X-Ray Detector ID (0018,9371) will have the same value in different Items of Multi-energy CT X-Ray Detector Sequence (0018,936F).
       </p>
