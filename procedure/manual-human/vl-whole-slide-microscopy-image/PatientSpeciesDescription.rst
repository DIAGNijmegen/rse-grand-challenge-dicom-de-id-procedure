-----------------------------------------
Patient Species Description | (0010,2201)
-----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The taxonomic rank value (e.g., genus, subgenus, species or subspecies) of the Patient. See
        <span href="">
         Section C.7.1.1.1.3
        </span>
        .
       </p>
       <p>
        Required if the Patient is a non-human organism and if Patient Species Code Sequence (0010,2202) is not present. May be present otherwise.
       </p>
