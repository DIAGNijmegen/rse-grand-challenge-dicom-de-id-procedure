--------------------------------------
Timezone Offset From UTC | (0008,0201)
--------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Basic Profile
:Basic Profile: X
:In Modules:
   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Contains the offset from UTC to the timezone for all DA and TM Attributes present in this SOP Instance, and for all DT Attributes present in this SOP Instance that do not contain an explicitly encoded timezone offset.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.8
        </span>
       </p>
       <p>
        The local timezone offset is undefined if this Attribute is absent.
       </p>
