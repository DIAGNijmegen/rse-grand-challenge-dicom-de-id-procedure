-----------------------------------
Extended Offset Table | (7FE0,0001)
-----------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - image-pixel [Mandatory (M)] [Optional (3)]::

       <p>
        Byte offsets of the Item Tags of the Frames in the Sequence of Items in Encapsulated Pixel Data encoded in Pixel Data (7FE0,0010).
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.3.1.8
        </span>
        .
       </p>
       <p>
        May only be present when:
       </p>
       <div>
        <ul>
         <li>
          <p>
           Pixel Data (7FE0,0010) is present, and
          </p>
         </li>
         <li>
          <p>
           the Transfer Syntax uses Encapsulated Format for the Pixel Data (7FE0,0010), and
          </p>
         </li>
         <li>
          <p>
           the Transfer Syntax encodes Frames in separate Fragments, and
          </p>
         </li>
         <li>
          <p>
           the Basic Offset Table is not present (i.e., the first Item of Pixel Data (7FE0,0010) has zero length), and
          </p>
         </li>
         <li>
          <p>
           each Frame is entirely contained within one Fragment.
          </p>
         </li>
        </ul>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            Unlike a Basic Offset Table, an Extended Offset Table, if the Attribute is present, is not permitted to be empty.
           </p>
          </li>
          <li>
           <p>
            If this Instance is part of a Concatenation, only the offset and lengths of the Frames encoded in the Pixel Data (7FE0,0010) of this Instance are indexed in the Extended Offset Table (7FE0,0001) and Extended Offset Table Lengths (7FE0,0002) in this Instance, not those of the entire Concatenation. I.e., the Values of these two Attributes are specific to each Instance. See also
            <span href="">
             Section C.7.6.16.2.2.4
            </span>
            .
           </p>
          </li>
          <li>
           <p>
            If the Data Set is re-encoded (such as in a different Transfer Syntax) any Extended Offset Table may need to be recomputed or removed.
           </p>
          </li>
         </ol>
        </div>
       </div>
