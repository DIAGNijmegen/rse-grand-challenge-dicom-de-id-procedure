-----------------------------------------
Spatial Locations Preserved | (0028,135A)
-----------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Module usage
:Basic Profile: N/A
:In Modules:
   - general-reference [User Optional (U)] [Optional (3)]::

       <p>
        The extent to which the spatial locations of all pixels are preserved during the processing of the source image that resulted in the current image
       </p>
       <div>
        <p>
         <strong>
          Enumerated Values:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           YES
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           NO
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           REORIENTED_ONLY
          </span>
         </dt>
         <dd>
          <p>
           A projection radiograph that has been flipped, and/or rotated by a multiple of 90 degrees
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            This applies not only to images with a known relationship to a 3D space, but also to projection images. For example, a projection radiograph such as a mammogram that is processed by a point image processing operation such as contrast enhancement, or a smoothing or edge enhancing convolution, would have a Value of YES for this Attribute. A projection radiograph that had been magnified or warped geometrically would have a Value of NO for this Attribute. A projection radiograph that has been flipped, and/or rotated by a multiple of 90 degrees, such that transformation of pixel locations is possible by comparison of the Values of Patient Orientation (0020,0020) would have a Value of REORIENTED_ONLY. This Attribute is typically of importance in relating images with Presentation Intent Type (0008,0068) Values of FOR PROCESSING and FOR PRESENTATION.
           </p>
          </li>
          <li>
           <p>
            When the Value of this Attribute is NO, it is not possible to locate on the current image any pixel coordinates that are referenced relative to the source image, such as for example, might be required for rendering CAD findings derived from a referenced FOR PROCESSING image on the current FOR PRESENTATION image.
           </p>
          </li>
         </ol>
        </div>
       </div>
