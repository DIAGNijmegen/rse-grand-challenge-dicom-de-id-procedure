-----------------------------------
Selector Value Number | (0072,0028)
-----------------------------------
:Action: Keep (K)
:Justication: Universally used: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Non-negative integer identifying which Value of a multi-valued Attribute identified by Selector Attribute (0072,0026) is to be referenced. The Value 1 identifies the first Value. The Value 0 identifies all Values.
       </p>
       <p>
        When the Value Multiplicity of the Selector Attribute (0072,0026) is 1 then the Value of this Attribute shall be 1.
       </p>
       <p>
        Required if the selected content is a single Attribute of any VR other than SQ.
       </p>
