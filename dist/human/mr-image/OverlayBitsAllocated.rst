------------------------------------
Overlay Bits Allocated | (60XX,0100)
------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: N/A
:In Modules:
   - overlay-plane [User Optional (U)] [Required with valid value (1)]::

       <p>
        Number of Bits Allocated in the Overlay.
       </p>
       <p>
        The Value of this Attribute shall be 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Formerly the Standard described embedding the overlay data in the Image Pixel Data (7FE0,0010), in which case the Value of this Attribute was required to be the same as Bits Allocated (0028,0100). This usage has been retired. See
         <a href="http://medical.nema.org/MEDICAL/Dicom/2004/printed/04_03pu3.pdf">
          PS3.3-2004
         </a>
         .
        </p>
       </div>
