---------------------------------------------
Nonidentifying Private Elements | (0008,0304)
---------------------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of Private Data Elements in block that do not contain identifying information (are safe from identity leakage).
       </p>
       <p>
        Elements are identified by the lowest 8-bits of the Date Element Tag (i.e., with a value from 0000H to 00FFH) within the block, stored as an unsigned short integer. Multiple values shall be in increasing order and a given Value shall be listed at most once.
       </p>
       <p>
        Required if Block Identifying Information Status (0008,0303) equals MIXED.
       </p>
