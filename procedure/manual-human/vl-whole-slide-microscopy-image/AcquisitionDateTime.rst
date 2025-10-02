----------------------------------
Acquisition DateTime | (0008,002A)
----------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required, with an value
:Basic Profile: X/Z/D
:In Modules:
   - general-acquisition [Mandatory (M)] [Optional (3)]::

       <p>
        The date and time that the acquisition of data that resulted in this instance started.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The synchronization of this time with an external clock is specified in the
         <span href="">
          Synchronization Module
         </span>
         in Acquisition Time Synchronized (0018,1800).
        </p>
       </div>

   - whole-slide-microscopy-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The date and time that the acquisition of data that resulted in this image started.
       </p>
