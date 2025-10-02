----------------------
Stack ID | (0020,9056)
----------------------
:Action: Keep (K)
:Justication: Keeps the concatenation internally consistent
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of a group of Frames, with different positions and/or orientations that belong together, within a dimension organization.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.2.4
        </span>
        for further explanation.
       </p>
       <p>
        Required if the Value of SOP Class UID (0008,0016) equals "1.2.840.10008.5.1.4.1.1.130" (Enhanced PET Image Storage) or Functional MR Sequence (0018,9621) is present. May be present otherwise. See
        <span href="">
         Section C.7.6.16.2.2.7
        </span>
        and
        <span href="">
         Section C.7.6.16.2.2.8
        </span>
        .
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Frame Content Functional Group Macro with usage: U
       </p>
