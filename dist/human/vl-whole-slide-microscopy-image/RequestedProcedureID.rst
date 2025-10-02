------------------------------------
Requested Procedure ID | (0040,1001)
------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Basic Profile
:Basic Profile: X
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifier that identifies the Requested Procedure in the Imaging Service Request.
       </p>
       <p>
        Required if procedure was scheduled. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The condition is to allow the contents of this Macro to be present (e.g., to convey the reason for the procedure, such as whether a mammogram is for screening or diagnostic purposes) even when the procedure was not formally scheduled and a value for this identifier is unknown, rather than making up a dummy value.
        </p>
       </div>
