----------------------------
Inversion Time | (0018,0082)
----------------------------
:Action: Keep (K)
:Justication: Describes crucial data acquisition details
:Basic Profile: N/A
:In Modules:
   - mr-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Time in msec after the middle of inverting RF pulse to middle of excitation pulse to detect the amount of longitudinal magnetization. Required if Scanning Sequence (0018,0020) has Values of IR.
       </p>
