---------------------
CTDIvol | (0018,9345)
---------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Computed Tomography Dose Index (CTDI
        <sub>
         vol
        </sub>
        ), in mGy according to the principles described in
        <span href="">
         [
         <abbr>
          IEC 60601-2-44
         </abbr>
         ]
        </span>
        .
                                               It describes the average dose for this image for the selected CT conditions of operation.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Computed Tomography Dose Index (CTDI
        <sub>
         vol
        </sub>
        ), in mGy according to the principles described in
        <span href="">
         [
         <abbr>
          IEC 60601-2-44
         </abbr>
         ]
        </span>
        .
                                                   The CTDI
        <sub>
         vol
        </sub>
        describes the average dose for this Frame for the selected CT conditions of operation.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
