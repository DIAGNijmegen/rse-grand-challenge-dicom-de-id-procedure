-------------------------------------------------
MAC Calculation Transfer Syntax UID | (0400,0010)
-------------------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The Transfer Syntax UID used to encode the values of the Data Elements included in the MAC calculation. Only Transfer Syntaxes that explicitly include the VR and use Little Endian encoding shall be used.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Certain Transfer Syntaxes, particularly those that are used with compressed data, allow the fragmentation of the pixel data to change. If such fragmentation changes, Digital Signatures generated with such Transfer Syntaxes could become invalid.
        </p>
       </div>
