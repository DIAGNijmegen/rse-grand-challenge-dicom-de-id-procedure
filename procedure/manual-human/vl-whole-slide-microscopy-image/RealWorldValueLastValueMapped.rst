------------------------------------------------
Real World Value Last Value Mapped | (0040,9211)
------------------------------------------------
:Action: Keep (K)
:Justication: Sequence describing image-to-world details
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the last stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) or Real World Value LUT Data (0040,9212) of this Item.
       </p>
       <p>
        Required if Pixel Data (7FE0,0010) or Real World Value LUT Data (0040,9212) is present or Double Float Real World Value Last Value Mapped (0040,9213) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be used even when Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are used instead of Pixel Data (7FE0,0010) if an integer of the size of this Attribute is sufficient to define the range.
        </p>
       </div>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.11.1
        </span>
        for further explanation.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the last stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) or Real World Value LUT Data (0040,9212) of this Item.
       </p>
       <p>
        Required if Pixel Data (7FE0,0010) or Real World Value LUT Data (0040,9212) is present or Double Float Real World Value Last Value Mapped (0040,9213) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be used even when Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are used instead of Pixel Data (7FE0,0010) if an integer of the size of this Attribute is sufficient to define the range.
        </p>
       </div>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.11.1
        </span>
        for further explanation.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Real World Value Mapping Functional Group Macro with usage: U
       </p>
