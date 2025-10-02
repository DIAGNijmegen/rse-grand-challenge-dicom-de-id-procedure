----------------------------------------
Digital Signature DateTime | (0400,0105)
----------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: D
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The date and time the Digital Signature was created. The time shall include an offset (i.e., time zone indication) from Coordinated Universal Time.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This is not a certified timestamp, and hence is not completely verifiable. An application can compare this date and time with those of other signatures and the validity date of the certificate to gain confidence in the veracity of this date and time.
        </p>
       </div>
