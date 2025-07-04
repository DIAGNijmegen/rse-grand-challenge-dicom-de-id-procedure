--------------------------------------
Single Collimation Width | (0018,9306)
--------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The width of a single row of acquired data (in mm).
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Adjacent physical detector rows may have been combined to form a single effective acquisition row.
        </p>
       </div>
       <p>
        Shall not be present if this Attribute is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The width of a single row of acquired data (in mm).
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Adjacent physical detector rows may have been combined to form a single effective acquisition row.
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>
