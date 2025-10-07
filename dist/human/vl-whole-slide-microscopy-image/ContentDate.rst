--------------------------
Content Date | (0008,0023)
--------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: Grand-challenge binds together series as a single value
:Basic Profile: Z/D
:In Modules:
   - general-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The date the image pixel data creation started.
       </p>
       <p>
        Required if image is part of a Series in which the images are temporally related. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute was formerly known as Image Date.
        </p>
       </div>

   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The date the data creation was started.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         For Instance, this is the date the pixel data is created, not the date the data is acquired.
        </p>
       </div>
