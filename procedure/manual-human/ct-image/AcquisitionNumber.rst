--------------------------------
Acquisition Number | (0020,0012)
--------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Allows identification of study. Not allowed
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        A number identifying the single continuous gathering of data over a period of time that resulted in this image.
       </p>

   - general-acquisition [Mandatory (M)] [Optional (3)]::

       <p>
        A number identifying the single continuous gathering of data over a period of time that resulted in this instance.
       </p>
