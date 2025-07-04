-------------------------------------
Lossy Image Compression | (0028,2110)
-------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        Specifies whether an Image has undergone lossy compression (at a point in its lifetime).
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
           00
          </span>
         </dt>
         <dd>
          <p>
           Image has not been subjected to lossy compression.
          </p>
         </dd>
         <dt>
          <span>
           01
          </span>
         </dt>
         <dd>
          <p>
           Image has been subjected to lossy compression.
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Once this Attribute has been set to a Value of "01" it shall not be reset.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.1.1.5
        </span>
        .
       </p>
