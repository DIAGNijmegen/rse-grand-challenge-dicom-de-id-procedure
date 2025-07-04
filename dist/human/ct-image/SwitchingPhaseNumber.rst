------------------------------------
Switching Phase Number | (0018,936B)
------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A number, unique within the Sequence, to identify the switching phase.
       </p>
       <p>
        Required if Multi-energy Source Technique (0018,9368) is "SWITCHING_SOURCE".
       </p>
