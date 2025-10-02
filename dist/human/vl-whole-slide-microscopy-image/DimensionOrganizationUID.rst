----------------------------------------
Dimension Organization UID | (0020,9164)
----------------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: [AUTO] Basic Profile
:Basic Profile: U
:In Modules:
   - multi-frame-dimension [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Uniquely identifies a set of dimensions referenced within the containing SOP Instance. In particular the dimension described by this Sequence Item is associated with this Dimension Organization UID. See
        <span href="">
         Section C.7.6.17.2
        </span>
        for further explanation.
       </p>
