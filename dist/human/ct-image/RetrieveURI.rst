--------------------------
Retrieve URI | (0040,E010)
--------------------------
:Action: Remove (X)
:Justication: Retrieval URI, DANGER Will Robinson!
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Required with valid value (1)]::

       <p>
        URI/URL specifying the location of the referenced Instance(s). Includes fully specified scheme, authority, path, and query in accordance with
        <span href="">
         [
         <abbr>
          RFC3986
         </abbr>
         ]
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The VR of this Data Element has changed from UT to UR.
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Retrieval access path to HL7 Structured Document. Includes fully specified scheme, authority, path, and query in accordance with
        <span href="">
         [
         <abbr>
          RFC3986
         </abbr>
         ]
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The VR of this Data Element has changed from UT to UR.
        </p>
       </div>
