---------------------------------------
Referenced Image Sequence | (0008,1140)
---------------------------------------
:Action: Remove (X)
:Justication: References other Images, this is not supported
:Basic Profile: X/Z/U*
:In Modules:
   - general-reference [User Optional (U)] [Optional (3)]::

       <p>
        Other images significantly related to this image (e.g., post-localizer CT image, Mammographic biopsy or partial view images, or slide images containing control material).
       </p>
       <p>
        One or more Items are permitted in this Sequence.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        The set of images or other composite SOP Instances used to plan the acquisition, if any, and other significant related images. See
        <span href="">
         Section C.7.6.16.2.5.1
        </span>
        for further explanation. Zero or more Items shall be included in this Sequence.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Referenced Image Functional Group Macro with usage: U
       </p>
