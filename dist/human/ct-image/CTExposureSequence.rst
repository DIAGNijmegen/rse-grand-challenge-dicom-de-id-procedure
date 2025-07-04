----------------------------------
CT Exposure Sequence | (0018,9321)
----------------------------------
:Action: Keep (K)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Required with valid value (1)]::

       <p>
        Contains the Attributes defining exposure information.
       </p>
       <p>
        If Multi-energy CT Acquisition (0018,9361) is NO or is absent, only a single Item shall be included in this Sequence.
       </p>
       <p>
        If Multi-energy CT Acquisition (0018,9361) is YES, one or more Items shall be included in this Sequence.
       </p>
