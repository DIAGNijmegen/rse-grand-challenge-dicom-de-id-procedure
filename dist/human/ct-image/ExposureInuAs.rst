-----------------------------
Exposure in µAs | (0018,1153)
-----------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The exposure expressed in µAs, for example calculated from Exposure Time and X-Ray Tube Current.
       </p>
       <p>
        Shall not be present if the corresponding Attribute, Exposure in mAs (0018,9332), is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>
