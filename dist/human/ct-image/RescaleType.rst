--------------------------
Rescale Type | (0028,1054)
--------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the output units of Rescale Slope (0028,1053) and Rescale Intercept (0028,1052).
       </p>
       <p>
        See
        <span href="">
         Section C.11.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>
       <p>
        Required if the Rescale Type is not HU (Hounsfield Units), or Multi-energy CT Acquisition (0018,9361) is YES. May be present otherwise.
       </p>
