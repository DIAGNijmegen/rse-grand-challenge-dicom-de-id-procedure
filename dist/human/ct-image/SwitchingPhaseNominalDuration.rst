----------------------------------------------
Switching Phase Nominal Duration | (0018,936C)
----------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Optional (3)]::

       <p>
        Duration, in microseconds, that the energy is nominally in the target KV for this switching phase. I.e., the Switching Phase Nominal Duration does not include the Switching Phase Transition Duration (0018,936D).
       </p>
       <p>
        The target KV is the Value of KVP (0018,0060) for the Item in the CT X-Ray Details Sequence (0018,9325) that identifies the Multi-energy CT Path Index (0018,937A) that corresponds to this X-Ray Source.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Applicable if Multi-energy Source Technique (0018,9368) is "SWITCHING_SOURCE".
        </p>
       </div>
