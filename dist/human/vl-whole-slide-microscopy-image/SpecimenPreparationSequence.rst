-------------------------------------------
Specimen Preparation Sequence | (0040,0610)
-------------------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: [AUTO] Basic Profile
:Basic Profile: Z
:In Modules:
   - specimen [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Sequence of Items identifying the process steps used to prepare the specimen for image acquisition. This includes description of all processing necessary to interpret the image.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
       <p>
        This Sequence includes description of the specimen sampling step from an ancestor specimen, potentially back to the original part collection.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.22.1.3
        </span>
        .
       </p>
