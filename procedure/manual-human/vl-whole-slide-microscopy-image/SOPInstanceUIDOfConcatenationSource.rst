------------------------------------------------------
SOP Instance UID of Concatenation Source | (0020,0242)
------------------------------------------------------
:Action: Replace with a non-zero length UID that is internally consistent within a set of Instances (U)
:Justication: Keeps the concatenation internally consistent
:Basic Profile: N/A
:In Modules:
   - vl-whole-slide-microscopy-image-multi-frame-functional-groups [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The SOP Instance UID of the single composite SOP Instance of which the Concatenation is a part. All SOP Instances of a Concatenation shall use the same Value for this Attribute, see
        <span href="">
         Section C.7.6.16.1.3
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         May be used to reference the entire Instance rather than individual Instances of the Concatenation, which may be transient (e.g., from a presentation state).
        </p>
       </div>
       <p>
        Required if Concatenation UID (0020,9161) is present.
       </p>
