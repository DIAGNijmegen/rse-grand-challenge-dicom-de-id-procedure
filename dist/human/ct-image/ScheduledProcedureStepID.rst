-----------------------------------------
Scheduled Procedure Step ID | (0040,0009)
-----------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Basic Profile
:Basic Profile: X
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifier that identifies the Scheduled Procedure Step.
       </p>
       <p>
        Required if procedure was scheduled.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The condition is to allow the contents of this Macro to be present (e.g., to convey the reason for the procedure, such as whether a mammogram is for screening or diagnostic purposes) even when the procedure step was not formally scheduled and a value for this identifier is unknown, rather than making up a dummy value.
        </p>
       </div>
