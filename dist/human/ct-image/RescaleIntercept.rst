-------------------------------
Rescale Intercept | (0028,1052)
-------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The value b in relationship between stored values (SV) and the output units.
       </p>
       <p>
        Output units = m*SV+b
       </p>
       <p>
        If Image Type (0008,0008) Value 1 is ORIGINAL and Value 3 is not LOCALIZER, and Multi-energy CT Acquisition (0018,9361) is either absent or NO, output units shall be Hounsfield Units (HU).
       </p>
