--------------------------
Trigger Time | (0018,1060)
--------------------------
:Action: Keep (K)
:Justication: Describes crucial data acquisition details
:Basic Profile: N/A
:In Modules:
   - mr-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Time, in msec, between peak of the R wave and the peak of the echo produced. In the case of segmented k-space, the TE(eff) is the time between the peak of the echo that is used to cover the center of k-space. Required for Scan Options (0018,0022) that include heart gating (e.g., CG, PPG, etc.).
       </p>
