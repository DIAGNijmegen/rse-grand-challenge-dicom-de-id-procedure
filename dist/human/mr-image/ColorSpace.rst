-------------------------
Color Space | (0028,2002)
-------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        A label that identifies the well-known color space of the image. Shall be consistent with any ICC Profile (0028,2000) that is also present.
       </p>
       <p>
        Shall not be present when the Optical Path Sequence (0048,0105) is present.
       </p>
       <p>
        See
        <span href="">
         Section C.11.15.1.2
        </span>
        .
       </p>

   - image-pixel [Mandatory (M)] [Optional (3)]::

       <p>
        A label that identifies the well-known color space of the image. Shall be consistent with any ICC Profile (0028,2000) that is also present.
       </p>
       <p>
        Shall not be present when the Optical Path Sequence (0048,0105) is present.
       </p>
       <p>
        See
        <span href="">
         Section C.11.15.1.2
        </span>
        .
       </p>
