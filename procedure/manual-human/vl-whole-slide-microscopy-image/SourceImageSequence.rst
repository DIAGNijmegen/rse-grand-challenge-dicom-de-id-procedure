-----------------------------------
Source Image Sequence | (0008,2112)
-----------------------------------
:Action: Remove (X)
:Justication: References other Images, this is not supported
:Basic Profile: X/Z/U*
:In Modules:
   - general-reference [User Optional (U)] [Optional (3)]::

       <p>
        The set of Image SOP Class/Instance pairs of the Images that were used to derive this Image.
       </p>
       <p>
        One or more Items are permitted in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section C.12.4.1.2
        </span>
        for further explanation.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        The set of Images or other Composite SOP Instances that were used to derive this Frame.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence. See
        <span href="">
         Section C.12.4.1.2
        </span>
        for further explanation.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Derivation Image Functional Group Macro with usage: C
       </p>
       <p>
        Required if the image or Frame has been derived from another SOP Instance.
       </p>
