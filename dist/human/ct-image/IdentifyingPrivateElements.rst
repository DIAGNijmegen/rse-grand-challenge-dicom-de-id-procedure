------------------------------------------
Identifying Private Elements | (0008,0306)
------------------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        List of Private Data Elements in block that may contain identifying information (are unsafe from identity leakage).
       </p>
       <p>
        Elements are identified by the lowest 8-bits of the Data Element Tag (i.e., with a value from 0000H to 00FFH) within the block, stored as an unsigned short integer. Multiple values shall be in increasing order and a given Value shall be listed at most once.
       </p>
