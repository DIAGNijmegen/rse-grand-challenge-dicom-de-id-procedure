---------------------------------------
Referenced Segment Number | (0062,000B)
---------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - acquisition-context [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Segment Number to which the reference applies.
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Segment Number to which the reference applies. Required if the Referenced SOP Instance is a Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Segment Number to which the reference applies.
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - specimen [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>
       <h3>
        Note
       </h3>
       <p>
        Part of the Real World Value Mapping Functional Group Macro with usage: U
       </p>
