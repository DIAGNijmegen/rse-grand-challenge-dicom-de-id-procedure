------------------------------
Patient Position | (0018,5100)
------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Patient position descriptor relative to the equipment. Required for images where Patient Orientation Code Sequence (0054,0410) is not present and whose SOP Class UID (0008,0016) is one of the following:
                                               "1.2.840.10008.5.1.4.1.1.2" (CT Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4" (MR Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.2.1" (Enhanced CT Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4.1" (Enhanced MR Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4.3" (Enhanced Color MR Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4.2" (MR Spectroscopy Storage SOP Class).
       </p>
       <p>
        May be present for other SOP Classes if Patient Orientation Code Sequence (0054,0410) is not present.
       </p>
       <p>
        See
        <span href="">
         Section C.7.3.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>

   - patient [Mandatory (M)] [Optional (3)]::

       <p>
        Patient position descriptor relative to the equipment. See
        <span href="">
         Section C.7.1.4.1.1.1
        </span>
        .
       </p>
       <p>
        See
        <span href="">
         Section C.7.3.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>
