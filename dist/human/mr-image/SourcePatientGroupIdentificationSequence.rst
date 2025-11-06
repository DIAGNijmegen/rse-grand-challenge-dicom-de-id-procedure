----------------------------------------------------------
Source Patient Group Identification Sequence | (0010,0026)
----------------------------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Optional (3)]::

       <p>
        A Sequence containing the Patient ID (0010,0020) and related Attributes in the source Composite Instances that contained a group of subjects whose data was acquired at the same time, from which this Composite Instance was extracted. See
        <span href="">
         Section C.7.1.4.1.1
        </span>
        .
       </p>
       <p>
        Only a single Item is permitted in this Sequence.
       </p>
