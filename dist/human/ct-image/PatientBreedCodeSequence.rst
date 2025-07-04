-----------------------------------------
Patient Breed Code Sequence | (0010,2293)
-----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The breed of the Patient. See
        <span href="">
         Section C.7.1.1.1.1
        </span>
        .
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if the Patient is a non-human organism.
       </p>
