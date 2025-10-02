-------------------------------------------
Lossy Image Compression Ratio | (0028,2112)
-------------------------------------------
:Action: Keep (K)
:Justication: Important data conversion details
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        Describes the approximate lossy compression ratio(s) that have been applied to this image.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.1.1.5.2
        </span>
        .
       </p>

   - whole-slide-microscopy-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Describes the approximate lossy compression ratio(s) that have been applied to this image.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.1.1.5.2
        </span>
        .
       </p>
       <p>
        Required if Lossy Image Compression (0028,2110) is "01".
       </p>
