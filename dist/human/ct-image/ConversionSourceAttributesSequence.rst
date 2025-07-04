---------------------------------------------------
Conversion Source Attributes Sequence | (0020,9172)
---------------------------------------------------
:Action: Remove (X)
:Justication: Describes source DICOM if conversion: can be safely excluded
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The set of images or other composite SOP Instances that were converted to this Instance.
       </p>
       <p>
        If this Instance was converted from a specific Frame in the source Instance, the reference shall include the Frame Number.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if this Instance was created by conversion from a DICOM source, and Conversion Source Attributes Sequence (0020,9172) is not present in an Item of Shared Functional Groups Sequence (5200,9229) or Per-Frame Functional Groups Sequence (5200,9230).
       </p>
