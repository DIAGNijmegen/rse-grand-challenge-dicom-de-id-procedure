--------------------------------------------------------------
Double Float Real World Value First Value Mapped | (0040,9214)
--------------------------------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the first stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) of this Item.
       </p>
       <p>
        Required if Real World Value First Value Mapped (0040,9216) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The same Attribute with a double float precision value is used whether or not Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are present, an integer value is not sufficient.
        </p>
       </div>
