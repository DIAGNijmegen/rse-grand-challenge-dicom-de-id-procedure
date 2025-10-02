---------------------------
Tiles Overlap | (0048,0304)
---------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - microscope-slide-layer-tile-organization [Mandatory (M)] [Optional (3)]::

       <p>
        Whether or not tiles in this Instance overlap with one or more adjacent tiles in the same Instance.
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
           ALL
          </span>
         </dt>
         <dd>
          <p>
           All tiles overlap with at least one adjacent tile
          </p>
         </dd>
         <dt>
          <span>
           SOME
          </span>
         </dt>
         <dd>
          <p>
           Some tiles overlap with at least one adjacent tile
          </p>
         </dd>
         <dt>
          <span>
           UNDEFINED
          </span>
         </dt>
         <dd>
          <p>
           Some tiles might overlap
          </p>
         </dd>
         <dt>
          <span>
           NONE
          </span>
         </dt>
         <dd>
          <p>
           No tiles overlap
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Shall be NONE if this Attribute is present and Dimension Organization Type (0020,9311) is present with a Value of TILED_FULL.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         If the Value is NONE, then a receiving application to which this matters does not need to check the position of every tile in this respect, since it can be assured that no tiles overlap. If the Value is UNDEFINED or SOME or ALL, or the Attribute is absent, then a receiving application might need to check the position of every tile.
        </p>
       </div>
