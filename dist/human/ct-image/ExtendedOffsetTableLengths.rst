-------------------------------------------
Extended Offset Table Lengths | (7FE0,0002)
-------------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Byte lengths of the Frames in the Sequence of Items in Encapsulated Pixel Data encoded in Pixel Data (7FE0,0010).
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.3.1.8
        </span>
        .
       </p>
       <p>
        Required if Extended Offset Table (7FE0,0001) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            This Attribute is only sent when each Frame is entirely contained within one Fragment as a single contiguous span of bytes so that it is not necessary to assemble the Frame from Fragments with delimiters.
           </p>
          </li>
          <li>
           <p>
            The length encoded in this Attribute may be an odd number if the compressed bitstream for the Frame is an odd length; i.e., it does not include any trailing padding required to make the Item an even length.
           </p>
          </li>
         </ol>
        </div>
       </div>
