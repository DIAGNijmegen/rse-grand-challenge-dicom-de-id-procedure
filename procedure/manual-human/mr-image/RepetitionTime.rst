-----------------------------
Repetition Time | (0018,0080)
-----------------------------
:Action: Keep (K)
:Justication: Describes crucial data acquisition details
:Basic Profile: N/A
:In Modules:
   - mr-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The period of time in msec between the beginning of a pulse sequence and the beginning of the succeeding (essentially identical) pulse sequence.
       </p>
       <p>
        Required if Sequence Variant (0018,0021) is SK or if Scanning Sequence (0018,0020) is not EP. May be present otherwise.
       </p>
