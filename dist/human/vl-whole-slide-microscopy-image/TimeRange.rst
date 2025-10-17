------------------------
Time Range | (0008,1163)
------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - frame-extraction [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The start and end times of the Frames that were extracted.
       </p>
       <p>
        Required if object extraction is based on a Frame Level Retrieve using Time Range (0008,1163).
       </p>
       <p>
        See
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part04.html#PS3.4" target="_blank">
         PS3.4
        </a>
        "Instance and Frame Level Retrieve SOP Classes".
       </p>
