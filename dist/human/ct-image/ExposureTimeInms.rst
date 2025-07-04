---------------------------------
Exposure Time in ms | (0018,9328)
---------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Duration of exposure for this Frame in milliseconds. If Acquisition Type (0018,9302) equals SPIRAL the duration of the exposure time for this Frame shall be Revolution Time (0018,9305) divided by the Spiral Pitch Factor (0018,9311). See
        <span href="">
         Section C.8.15.3.8.1
        </span>
        .
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL, or if Image Type (0008,0008) Value 1 is ORIGINAL and Multi-energy CT Acquisition (0018,9361) is YES. May be present otherwise.
       </p>
