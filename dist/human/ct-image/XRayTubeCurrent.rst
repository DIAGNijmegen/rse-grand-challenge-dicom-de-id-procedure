--------------------------------
X-Ray Tube Current | (0018,1151)
--------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        X-Ray Tube Current in mA.
       </p>
       <p>
        Shall not be present if the corresponding Attribute, X-Ray Tube Current in mA (0018,9330), is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>
