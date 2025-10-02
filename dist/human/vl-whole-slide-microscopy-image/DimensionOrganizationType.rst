-----------------------------------------
Dimension Organization Type | (0020,9311)
-----------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - multi-frame-dimension [Mandatory (M)] [Optional (3)]::

       <p>
        Dimension organization of the Instance.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           3D
          </span>
         </dt>
         <dd>
          <p>
           Spatial Multi-frame Image of equally spaced parallel planes (3D volume set)
          </p>
         </dd>
         <dt>
          <span>
           3D_TEMPORAL
          </span>
         </dt>
         <dd>
          <p>
           Temporal loop of equally spaced parallel-plane 3D volume sets.
          </p>
         </dd>
         <dt>
          <span>
           TILED_FULL
          </span>
         </dt>
         <dd>
          <p>
           Tiled image in which each Frame represents a single tile and the positions of the tiles are implicitly defined as per
           <span href="">
            Section C.7.6.17.3
           </span>
           .
          </p>
         </dd>
         <dt>
          <span>
           TILED_SPARSE
          </span>
         </dt>
         <dd>
          <p>
           Tiled image in which each Frame represents a single tile and the positions of tiles are explicitly defined by per-frame Functional Group Macro entries.
          </p>
         </dd>
        </dl>
       </div>
