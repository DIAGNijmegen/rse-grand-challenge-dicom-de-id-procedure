------------------------------------
Dimension Index Values | (0020,9157)
------------------------------------
:Action: Keep (K)
:Justication: Multi-frame meta data
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Contains the Values of the indices defined in the Dimension Index Sequence (0020,9222) for this multi-frame header Frame. The number of Values is equal to the number of Items of the Dimension Index Sequence and shall be applied in the same order.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.17.1
        </span>
        for a description.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         In
         <span href="">
          Section C.7.6.17.1
         </span>
         , the index values are defined to start from 1 and monotonically increase by 1, within the scope of the Dimension Organization UID (0020,9164).
        </p>
       </div>
       <p>
        Required if the Value of Dimension Index Sequence (0020,9222) exists.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         For some IODs, such as the VL Whole Slide Microscopy Image IOD, the entire Frame Content Sequence (0020,9111) may be omitted, but if it is present and Dimensions are explicitly defined, then the index values need to be supplied here.
        </p>
       </div>
       <h3>
        Note
       </h3>
       <p>
        Part of the Frame Content Functional Group Macro with usage: U
       </p>
