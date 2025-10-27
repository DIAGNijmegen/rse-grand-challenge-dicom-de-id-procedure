-----------------------------
Instance Number | (0020,0013)
-----------------------------
:Action: Keep (K)
:Justication: Identifies and orders image within single study. No PI
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        A number that identifies this image.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute was named Image Number in previous releases of this Standard.
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        A number that identifies this Composite Instance.
       </p>
