-----------------
KVP | (0018,0060)
-----------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Peak kilo voltage output of the X-Ray generator used.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal peak kilo voltage output of the X-Ray generator used.
       </p>
       <p>
        If Multi-energy Source Technique (0018,9368) in Multi-energy CT X-Ray Source Sequence (0018,9365) (of the referenced Multi-energy CT Path Index (0018,937A)) is "SWITCHING_SOURCE", this Value is the nominal peak value for a switching phase. The switching phase is identified by the Value of X-Ray Source Index (0018,9366) in the Multi-energy CT Path Sequence (0018,9379) corresponding to the Value of Referenced Path Index (0018,9378) in this Sequence.
       </p>
       <p>
        Due to limitations of the generating hardware the actual voltage may not reach the nominal peak value.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
