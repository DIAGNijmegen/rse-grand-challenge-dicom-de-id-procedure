------------------------
Patient ID | (0010,0020)
------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: [AUTO] Basic Profile
:Basic Profile: Z/D
:In Modules:
   - patient [Mandatory (M)] [Required with valid value (1)]::

       <p>
        An identifier for the Patient.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         In the case of imaging a group of small animals simultaneously, the single Value of this identifier corresponds to the identification of the entire group. See also
         <span href="">
          Section C.7.1.4.1.1
         </span>
         .
        </p>
       </div>
