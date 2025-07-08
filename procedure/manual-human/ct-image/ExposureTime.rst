---------------------------
Exposure Time | (0018,1150)
---------------------------
:Action: Keep (K)
:Justication: Possibly relevant aquisition data
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Time of X-Ray exposure in msec.
       </p>
       <p>
        If Acquisition Type (0018,9302) equals SPIRAL, the Value of this Attribute shall be Revolution Time (0018,9305) divided by the Spiral Pitch Factor (0018,9311). See
        <span href="">
         Section C.8.15.3.8.1
        </span>
        and
        <span href="">
         Section C.8.15.3.2.1
        </span>
        .
       </p>
       <p>
        Shall not be present if the corresponding Attribute, Exposure Time in ms (0018,9328), is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>
