--------------------------------------------
Patient's Alternative Calendar | (0010,0035)
--------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required under some conditions: dummy if present
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Alternative Calendar used for Patient's Birth Date in Alternative Calendar (0010,0033) and Patient's Death Date in Alternative Calendar (0010,0034).
       </p>
       <p>
        See
        <span href="">
         Section C.7.1.5
        </span>
        for Defined Terms.
       </p>
       <p>
        Required if either Patient's Birth Date in Alternative Calendar (0010,0033) or Patient's Alternative Death Date in Calendar (0010,0034) is present.
       </p>
