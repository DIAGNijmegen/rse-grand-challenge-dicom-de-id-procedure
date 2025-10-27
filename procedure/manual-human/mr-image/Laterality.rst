------------------------
Laterality | (0020,0060)
------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Laterality of (paired) body part examined. Required if the body part examined is a paired structure and Image Laterality (0020,0062) or Frame Laterality (0020,9072) or Measurement Laterality (0024,0113) are not present.
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
           R
          </span>
         </dt>
         <dd>
          <p>
           right
          </p>
         </dd>
         <dt>
          <span>
           L
          </span>
         </dt>
         <dd>
          <p>
           left
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
            Some IODs support Image Laterality (0020,0062) at the Image level or Frame Laterality (0020,9072) at the Frame level in the Frame Anatomy Functional Group Macro or Measurement Laterality (0024,0113) at the Measurement level, which can provide a more comprehensive mechanism for specifying the laterality of the body part(s) being examined.
           </p>
          </li>
          <li>
           <p>
            There is no value for both left and right, for which Image Laterality (0020,0062) at the Image level or Frame Laterality (0020,9072) may be used instead.
           </p>
          </li>
          <li>
           <p>
            There is no value for median, for which Primary Anatomic Structure Modifier Sequence (0008,2230) or Anatomic Region Modifier Sequence (0008,2220) may be used instead.
           </p>
          </li>
         </ol>
        </div>
       </div>
