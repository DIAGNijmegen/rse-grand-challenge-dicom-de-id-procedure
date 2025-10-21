--------------------------------------------------
Per-Frame Functional Groups Sequence | (5200,9230)
--------------------------------------------------
:Action: Keep (K)
:Justication: Common multiframe meta-data: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Sequence that contains the Functional Group Sequence Attributes corresponding to each Frame of the Multi-frame Image. The first Item corresponds with the first Frame, and so on.
       </p>
       <p>
        One or more Items shall be included in this Sequence. The number of Items shall be the same as the number of Frames in the Multi-frame Image. See
        <span href="">
         Section C.7.6.16.1.2
        </span>
        for further explanation.
       </p>
       <p>
        Required if for any Frame, there are Per-Frame Functional Groups that are not empty.
       </p>
