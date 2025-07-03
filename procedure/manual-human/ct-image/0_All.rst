------------------------
Pixel Data | (7FE0,0010)
------------------------
:Action: Keep (K)
:Justication: Critical data
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        A data stream of the pixel samples that comprise the Image. See
        <span href="">
         Section C.7.6.3.1.4
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A data stream of the pixel samples that comprise the Image. See
        <span href="">
         Section C.7.6.3.1.4
        </span>
        for further explanation.
       </p>
       <p>
        Required if Pixel Data Provider URL (0028,7FE0) is not present.
       </p>

------------------------------------
Specific Character Set | (0008,0005)
------------------------------------
:Action: Keep (K)
:Justication: Required if an expanded or replacement character set is used
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Character Set that expands or replaces the Basic Graphic Set.
       </p>
       <p>
        Required if an expanded or replacement character set is used.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.2
        </span>
        for Defined Terms.
       </p>

------------------------
Image Type | (0008,0008)
------------------------
:Action: Keep (K)
:Justication: Generally required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Image identification characteristics. See
        <span href="">
         Section C.8.2.1.1.1
        </span>
        for specialization.
       </p>

   - general-image [Mandatory (M)] [Optional (3)]::

       <p>
        Image identification characteristics. See
        <span href="">
         Section C.7.6.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>

--------------------------
Manufacturer | (0008,0070)
--------------------------
:Action: Keep (K)
:Justication: Required, manufacturer might be relevant
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer of the device.
       </p>

   - device [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer of the device.
       </p>

   - general-equipment [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer of the equipment that produced the Composite Instances.
       </p>

   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Manufacturer of the equipment that contributed to the Composite Instance.
       </p>

   - specimen [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer of the container component.
       </p>

------------------------
Code Value | (0008,0100)
------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if the length of the code value is 16 characters or less, and the code value is not a URN or URL.
       </p>

--------------------------------------
Coding Scheme Designator | (0008,0102)
--------------------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coding Scheme in which the Coded Entry is defined.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) or Long Code Value (0008,0119) is present. May be present otherwise.
       </p>

-----------------------------------
Coding Scheme Version | (0008,0103)
-----------------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        An identifier of the version of the Coding Scheme if necessary to resolve ambiguity.
       </p>
       <p>
        See
        <span href="">
         Section 8.2
        </span>
        . Required if the Value of Coding Scheme Designator (0008,0102) is present and is not sufficient to identify the Code Value (0008,0100) or Long Code Value (0008,0119) unambiguously. Shall not be present if Coding Scheme Designator (0008,0102) is absent. May be present otherwise.
       </p>

------------------------------
Mapping Resource | (0008,0105)
------------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Mapping Resource that defines the Context Group from which Coded Entry was selected.
       </p>
       <p>
        See
        <span href="">
         Section 8.4
        </span>
        . Required if Context Identifier (0008,010F) is present.
       </p>

------------------------------------
Coding Scheme Registry | (0008,0112)
------------------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The name of the external registry where further definition of the identified Coding Scheme may be obtained. Required if Coding Scheme is registered.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           HL7
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>

---------------------------------------
Coding Scheme External ID | (0008,0114)
---------------------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The Coding Scheme identifier as defined in an external registry. Required if Coding Scheme is registered and Coding Scheme UID (0008,010C) is not present.
       </p>

-----------------------------
Long Code Value | (0008,0119)
-----------------------------
:Action: Keep (K)
:Justication: Required, parent sequence should be already be typically removed
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is not a URN or URL.
       </p>

----------------------------
URN Code Value | (0008,0120)
----------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Universal ID: could be traced to all kinds of insitutes or entities
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The identifier of the Coded Entry.
       </p>
       <p>
        See
        <span href="">
         Section 8.1
        </span>
        .
       </p>
       <p>
        Shall be present if Code Value (0008,0100) is not present and the Code Value is a URN or URL.
       </p>

-------------------------------
Coding Scheme UID | (0008,010C)
-------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Coding Scheme UID identifier. Required if Coding Scheme is identified by an ISO 8824 object identifier compatible with the UI VR.
       </p>

---------------------------------------------
Nonidentifying Private Elements | (0008,0304)
---------------------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of Private Data Elements in block that do not contain identifying information (are safe from identity leakage).
       </p>
       <p>
        Elements are identified by the lowest 8-bits of the Date Element Tag (i.e., with a value from 0000H to 00FFH) within the block, stored as an unsigned short integer. Multiple values shall be in increasing order and a given Value shall be listed at most once.
       </p>
       <p>
        Required if Block Identifying Information Status (0008,0303) equals MIXED.
       </p>

--------------------------------------------------
Private Data Element Number of Items | (0008,030B)
--------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Number of Items allowed in a Sequence Data Element.
       </p>
       <p>
        Required if the Value of Private Data Element Value Representation (0008,030A) is SQ.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.7.2
        </span>
        .
       </p>

-------------------------------------
Referenced Frame Number | (0008,1160)
-------------------------------------
:Action: Keep (K)
:Justication: If present, it is required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Frame numbers within the Referenced SOP Instance to which the reference applies. The first Frame shall be denoted as Frame number 1.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be multi-valued.
        </p>
       </div>
       <p>
        Required if the Referenced SOP Instance is a Multi-frame Image and the reference does not apply to all Frames, and Referenced Segment Number (0062,000B) is not present.
       </p>

-------------------------------------
Referenced SOP Sequence | (0008,1199)
-------------------------------------
:Action: Keep (K)
:Justication: Required, child elements of this sequence are handled separately
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

   - patient [Mandatory (M)] [Required with valid value (1)]::

       <p>
        References to object Instances.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Composite SOP Instance Reference value for this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is COMPOSITE or IMAGE or WAVEFORM.
       </p>

-----------------------------------------
Patient Species Description | (0010,2201)
-----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The taxonomic rank value (e.g., genus, subgenus, species or subspecies) of the Patient. See
        <span href="">
         Section C.7.1.1.1.3
        </span>
        .
       </p>
       <p>
        Required if the Patient is a non-human organism and if Patient Species Code Sequence (0010,2202) is not present. May be present otherwise.
       </p>

-------------------------------------------
Patient Species Code Sequence | (0010,2202)
-------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The taxonomic rank value (e.g., genus, subgenus, species or subspecies) of the Patient. See
        <span href="">
         Section C.7.1.1.1.3
        </span>
        .
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if the Patient is a non-human organism and if Patient Species Description (0010,2201) is not present. May be present otherwise.
       </p>

-----------------------------------------
Anatomical Orientation Type | (0010,2210)
-----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The anatomical orientation type used in Instances generated by this equipment.
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
           BIPED
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           QUADRUPED
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if the Patient is a non-human organism and the anatomical Frame of Reference is not bipedal. May be present otherwise. See
        <span href="">
         Section C.7.6.1.1.1
        </span>
        and
        <span href="">
         Section C.7.6.2.1.1
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         If this Attribute is not present, the default human standard anatomical position is used to define the patient orientation of projection images and the Patient-Based Coordinate System of cross-sectional images.
        </p>
       </div>

---------------------------------------
Patient Breed Description | (0010,2292)
---------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The breed of the Patient. See
        <span href="">
         Section C.7.1.1.1.1
        </span>
        .
       </p>
       <p>
        Required if the Patient is a non-human organism and if Patient Breed Code Sequence (0010,2293) is empty. May be present otherwise.
       </p>

-----------------------------------------
Patient Breed Code Sequence | (0010,2293)
-----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The breed of the Patient. See
        <span href="">
         Section C.7.1.1.1.1
        </span>
        .
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if the Patient is a non-human organism.
       </p>

-----------------------------------------
Breed Registration Sequence | (0010,2294)
-----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Information identifying a non-human organism within a breed registry.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if the Patient is a non-human organism.
       </p>

-------------------------------------
Synchronization Channel | (0018,106C)
-------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - synchronization [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifier of waveform channel that records the synchronization channel or trigger, see
        <span href="">
         Section C.7.4.2.1.3
        </span>
        .
       </p>
       <p>
        Required if synchronization channel or trigger is encoded in a waveform in this SOP Instance.
       </p>

------------------------------------------------------------------------
Water Equivalent Diameter Calculation Method Code Sequence | (0018,1272)
------------------------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The method of calculation of Water Equivalent Diameter (0018,1271).
       </p>
       <p>
        Required if Water Equivalent Diameter (0018,1271) is present.
       </p>
       <p>
        Only a single Item is permitted in this Sequence.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The method of calculation of Water Equivalent Diameter (0018,1271).
       </p>
       <p>
        Required if Water Equivalent Diameter (0018,1271) is present.
       </p>
       <p>
        Only a single Item is permitted in this Sequence.
       </p>

------------------------------
Patient Position | (0018,5100)
------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Patient position descriptor relative to the equipment. Required for images where Patient Orientation Code Sequence (0054,0410) is not present and whose SOP Class UID (0008,0016) is one of the following:
                                               "1.2.840.10008.5.1.4.1.1.2" (CT Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4" (MR Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.2.1" (Enhanced CT Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4.1" (Enhanced MR Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4.3" (Enhanced Color MR Image Storage),
                                               "1.2.840.10008.5.1.4.1.1.4.2" (MR Spectroscopy Storage SOP Class).
       </p>
       <p>
        May be present for other SOP Classes if Patient Orientation Code Sequence (0054,0410) is not present.
       </p>
       <p>
        See
        <span href="">
         Section C.7.3.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>

   - patient [Mandatory (M)] [Optional (3)]::

       <p>
        Patient position descriptor relative to the equipment. See
        <span href="">
         Section C.7.1.4.1.1.1
        </span>
        .
       </p>
       <p>
        See
        <span href="">
         Section C.7.3.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>

-----------------------------
Filter Material | (0018,7050)
-----------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The X-Ray absorbing material used in the filter. May be multi-valued.
       </p>
       <p>
        See
        <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_P.html#chapter_P" target="_blank">
         Annex P “Correspondence of X-Ray Filter Material Codes and Defined Terms” in PS3.16
        </a>
        for Defined Terms.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The X-Ray absorbing material used in the filter. May be multi-valued.
       </p>
       <p>
        See
        <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_P.html#chapter_P" target="_blank">
         Annex P “Correspondence of X-Ray Filter Material Codes and Defined Terms” in PS3.16
        </a>
        for Defined Terms.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         At least one Value is required to be present. If a combination of materials is used, they may be listed using multiple Values, or a custom Value may be used to represent a proprietary combination of materials
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL, and the Value of Filter Type (0018,1160) is other than NONE. May be present otherwise.
       </p>

-------------------------------------------------------
Distance Source to Data Collection Center | (0018,9335)
-------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Distance in mm from source to data collection center. See
        <span href="">
         Section C.8.15.3.6.1
        </span>
        .
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

---------------------
CTDIvol | (0018,9345)
---------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Computed Tomography Dose Index (CTDI
        <sub>
         vol
        </sub>
        ), in mGy according to the principles described in
        <span href="">
         [
         <abbr>
          IEC 60601-2-44
         </abbr>
         ]
        </span>
        .
                                               It describes the average dose for this image for the selected CT conditions of operation.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Computed Tomography Dose Index (CTDI
        <sub>
         vol
        </sub>
        ), in mGy according to the principles described in
        <span href="">
         [
         <abbr>
          IEC 60601-2-44
         </abbr>
         ]
        </span>
        .
                                                   The CTDI
        <sub>
         vol
        </sub>
        describes the average dose for this Frame for the selected CT conditions of operation.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

-------------------------------------
Energy Weighting Factor | (0018,9353)
-------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The weighting factor of the data from this additional source in a multiple energy composition image. This factor incorporates the effects of
       </p>
       <div>
        <ul>
         <li>
          <p>
           the specific X-Ray source and kV value
          </p>
         </li>
         <li>
          <p>
           examination specific characteristics.
          </p>
         </li>
        </ul>
       </div>
       <p>
        Required if one Derivation Code Sequence (0008,9215) Item value is
        <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_113097" target="_blank">
         (113097, DCM, "Multi-energy proportional weighting")
        </a>
        . May be present otherwise.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The weighting factor of the data from this Sequence Item.
       </p>
       <p>
        Required if Required if Frame Type (0008,9007) Value 4 of this Frame is ENERGY_PROP_WT or Image Type (0008,0008) Value 4 is ENERGY_PROP_WT. May be present otherwise.
       </p>

------------------------------------------------------
Multi-energy CT Characteristics Sequence | (0018,9364)
------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Multi-energy characteristics of the generated image.
       </p>
       <p>
        Required if Image Type (0008,0008) Value 4 in the CT Image IOD, Image Type (0008,0008) Value 5 in the Enhanced CT Image IOD or Frame Type (0008,9007) Value 5 in the Enhanced CT Image IOD Frame is VMI. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>

------------------------------------
Switching Phase Number | (0018,936B)
------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A number, unique within the Sequence, to identify the switching phase.
       </p>
       <p>
        Required if Multi-energy Source Technique (0018,9368) is "SWITCHING_SOURCE".
       </p>

--------------------------------
Nominal Max Energy | (0018,9374)
--------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal maximum energy in keV of photons that are integrated/counted by the detector (see
        <span href="">
         Section C.8.2.2.1.1
        </span>
        ). Due to energy resolution limits of the detector, some photons above the nominal maximum may be counted.
       </p>
       <p>
        Required if Multi-energy Detector Type (0018,9372) is PHOTON_COUNTING. May be present otherwise.
       </p>

--------------------------------
Nominal Min Energy | (0018,9375)
--------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal minimum energy in keV of photons that are integrated/counted by the detector (see
        <span href="">
         Section C.8.2.2.1.1
        </span>
        ). Due to energy resolution limits of the detector, some photons below the nominal minimum may be counted.
       </p>
       <p>
        Required if Multi-energy Detector Type (0018,9372) is PHOTON_COUNTING. May be present otherwise.
       </p>

-----------------------------------
Referenced Path Index | (0018,9378)
-----------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        References the X-Ray Path Index (0018,937A) in the Multi-energy CT Path Sequence (0018,9379) for this exposure.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may contain multiple Values if this Item describes multiple paths.
        </p>
       </div>
       <p>
        Required if Multi-energy CT Acquisition (0018,9361) is YES.
       </p>

---------------------------------------------
Monoenergetic Energy Equivalent | (0018,937C)
---------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Single energy equivalent in keV.
       </p>
       <p>
        Required if Image Type (0008,0008) Value 4 in the CT Image IOD, Image Type (0008,0008) Value 5 in the Enhanced CT Image IOD or Frame Type (0008,9007) Value 5 in the Enhanced CT Image IOD Frame is EQUAL to VMI. May be present otherwise.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         If the Image Type (0008,0008) Value 4 in the CT Image IOD, Image Type (0008,0008) Value 5 in the Enhanced CT Image IOD or Frame Type (0008,9007) Value 5 in the Enhanced CT Image IOD Frame is (MAT_REMOVED, MAT_MODIFIED) and a VMI image was used as the source then this Value reflects the keV value of the VMI image.
        </p>
       </div>

--------------------------------
Pixel Aspect Ratio | (0028,0034)
--------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Ratio of the vertical size and horizontal size of the pixels in the image specified by a pair of integer values where the first Value is the vertical pixel size, and the second Value is the horizontal pixel size. Required if the aspect ratio values do not have a ratio of 1:1 and the physical pixel spacing is not specified by Pixel Spacing (0028,0030), or Imager Pixel Spacing (0018,1164) or Nominal Scanned Pixel Spacing (0018,2010), either for the entire Image or per-frame in a Functional Group Macro. See
        <span href="">
         Section C.7.6.3.1.7
        </span>
        .
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Ratio of the vertical size and horizontal size of the pixels in the image specified by a pair of integer values where the first Value is the vertical pixel size, and the second Value is the horizontal pixel size. Required if the aspect ratio values do not have a ratio of 1:1 and the physical pixel spacing is not specified by Pixel Spacing (0028,0030), or Imager Pixel Spacing (0018,1164) or Nominal Scanned Pixel Spacing (0018,2010), either for the entire Image or per-frame in a Functional Group Macro. See
        <span href="">
         Section C.7.6.3.1.7
        </span>
        .
       </p>

---------------------------------
Pixel Padding Value | (0028,0120)
---------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Single pixel value or one limit (inclusive) of a range of pixel values used in an image to pad to rectangular format or to signal background that may be suppressed or that may be rendered "transparently" when superimposing images. See
        <span href="">
         Section C.7.5.1.1.2
        </span>
        for further explanation.
       </p>
       <p>
        Required if Pixel Padding Range Limit (0028,0121) is present and either Pixel Data (7FE0,0010) or Pixel Data Provider URL (0028,7FE0) is present. May be present otherwise only if Pixel Data (7FE0,0010) or Pixel Data Provider URL (0028,7FE0) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            The Value Representation of this Attribute is determined by the Value of Pixel Representation (0028,0103).
           </p>
          </li>
          <li>
           <p>
            This Attribute is not used in Presentation State Instances; there is no means in a Presentation State to "override" any Pixel Padding Value (0028,0120) specified in the referenced images.
           </p>
          </li>
          <li>
           <p>
            This Attribute does apply to RT Dose and Segmentation Instances, since they include Pixel Data.
           </p>
          </li>
          <li>
           <p>
            This Attribute does not apply when Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are used instead of Pixel Data (7FE0,0010); Float Pixel Padding Value (0028,0122) or Double Float Pixel Padding Value (0028,0123), respectively, are used instead, and defined at the Image, not the Equipment, level.
           </p>
          </li>
          <li>
           <p>
            Only a single Value is allowed for this Attribute, so it only applies to images with Samples per Pixel (0028,0002) of 1, i.e., images with a Photometric Interpretation (0028,0004) of MONOCHROME1, MONOCHROME2 or PALETTE COLOR. See
            <span href="">
             Section C.7.5.1.1.2
            </span>
            for details.
           </p>
          </li>
         </ol>
        </div>
       </div>

-------------------------------------------------------
Red Palette Color Lookup Table Descriptor | (0028,1101)
-------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the format of the Red Palette Color Lookup Table Data (0028,1201). Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.5
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the format of the Red Palette Color Lookup Table Data (0028,1201). Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.5
        </span>
        for further explanation.
       </p>

---------------------------------------
Pixel Padding Range Limit | (0028,0121)
---------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Pixel value that represents one limit (inclusive) of a range of padding values used together with Pixel Padding Value (0028,0120) as defined in the
        <span href="">
         General Equipment Module
        </span>
        . See
        <span href="">
         Section C.7.5.1.1.2
        </span>
        for further explanation.
       </p>
       <p>
        Required if pixel padding is to be defined as a range rather than a single Value.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            The Value Representation of this Attribute is determined by the Value of Pixel Representation (0028,0103).
           </p>
          </li>
          <li>
           <p>
            Pixel Padding Value (0028,0120) is also required when this Attribute is present.
           </p>
          </li>
         </ol>
        </div>
       </div>

---------------------------------------------------------
Green Palette Color Lookup Table Descriptor | (0028,1102)
---------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the format of the Green Palette Color Lookup Table Data (0028,1202). Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.5
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the format of the Green Palette Color Lookup Table Data (0028,1202). Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.5
        </span>
        for further explanation.
       </p>

--------------------------------------------------------
Blue Palette Color Lookup Table Descriptor | (0028,1103)
--------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the format of the Blue Palette Color Lookup Table Data (0028,1203). Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.5
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the format of the Blue Palette Color Lookup Table Data (0028,1203). Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.5
        </span>
        for further explanation.
       </p>

-------------------------------------------------
Red Palette Color Lookup Table Data | (0028,1201)
-------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Red Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Red Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

---------------------------------------------------
Green Palette Color Lookup Table Data | (0028,1202)
---------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Green Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Green Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

--------------------------------------------------
Blue Palette Color Lookup Table Data | (0028,1203)
--------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Blue Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Blue Palette Color Lookup Table Data. Required if Photometric Interpretation (0028,0004) has a Value of PALETTE COLOR or Pixel Presentation (0008,9205) at the image level equals COLOR or MIXED. See
        <span href="">
         Section C.7.6.3.1.6
        </span>
        for further explanation.
       </p>

--------------------------
Rescale Type | (0028,1054)
--------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the output units of Rescale Slope (0028,1053) and Rescale Intercept (0028,1052).
       </p>
       <p>
        See
        <span href="">
         Section C.11.1.1.2
        </span>
        for Defined Terms and further explanation.
       </p>
       <p>
        Required if the Rescale Type is not HU (Hounsfield Units), or Multi-energy CT Acquisition (0018,9361) is YES. May be present otherwise.
       </p>

------------------------------------------
Referenced Waveform Channels | (0040,A0B0)
------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of channels in Waveform to which the reference applies. See
        <span href="">
         Section C.18.5.1.1
        </span>
        .
       </p>
       <p>
        Required if the Referenced SOP Instance is a Waveform that contains multiple Channels and the reference does not apply to all Channels of all Multiplex Groups.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of channels in Waveform to which the reference applies. See
        <span href="">
         Section C.18.5.1.1
        </span>
        .
       </p>
       <p>
        Required if the Referenced SOP Instance is a Waveform that contains multiple Channels and the reference does not apply to all Channels of all Multiplex Groups.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of channels in Waveform to which the reference applies. See
        <span href="">
         Section C.18.5.1.1
        </span>
        .
       </p>
       <p>
        Required if the Referenced SOP Instance is a Waveform that contains multiple Channels and the reference does not apply to all Channels of all Multiplex Groups.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of channels in Waveform to which the reference applies. See
        <span href="">
         Section C.18.5.1.1
        </span>
        .
       </p>
       <p>
        Required if the Referenced SOP Instance is a Waveform that contains multiple Channels and the reference does not apply to all Channels of all Multiplex Groups.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        List of channels in Waveform to which the reference applies. See
        <span href="">
         Section C.18.5.1.1
        </span>
        .
       </p>
       <p>
        Required if the Referenced SOP Instance is a Waveform that contains multiple Channels and the reference does not apply to all Channels of all Multiplex Groups.
       </p>

------------------------
Text Value | (0040,A160)
------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Free unlimited text in structured report. Not allowed
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Text value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is TEXT.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Text value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is TEXT.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Text value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is TEXT.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Text value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is TEXT.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Text value for this name-value Item.
       </p>
       <p>
        Required if Value Type (0040,A040) is TEXT.
       </p>

----------------------------------
Floating Point Value | (0040,A161)
----------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The floating point representation of Numeric Value (0040,A30A). The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent the value as a string. May be present otherwise.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The floating point representation of Numeric Value (0040,A30A). The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent the value as a string. May be present otherwise.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The floating point representation of Numeric Value (0040,A30A). The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent the value as a string. May be present otherwise.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The floating point representation of Numeric Value (0040,A30A). The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent the value as a string. May be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The floating point representation of Numeric Value (0040,A30A). The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent the value as a string. May be present otherwise.
       </p>

--------------------------------------
Rational Numerator Value | (0040,A162)
--------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer numerator of a rational representation of Numeric Value (0040,A30A), encoded as a signed integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent a rational value as a string. May be present otherwise.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer numerator of a rational representation of Numeric Value (0040,A30A), encoded as a signed integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent a rational value as a string. May be present otherwise.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer numerator of a rational representation of Numeric Value (0040,A30A), encoded as a signed integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent a rational value as a string. May be present otherwise.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer numerator of a rational representation of Numeric Value (0040,A30A), encoded as a signed integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent a rational value as a string. May be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer numerator of a rational representation of Numeric Value (0040,A30A), encoded as a signed integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Numeric Value (0040,A30A) has insufficient precision to represent a rational value as a string. May be present otherwise.
       </p>

----------------------------------------
Rational Denominator Value | (0040,A163)
----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer denominator of a rational representation of Numeric Value (0040,A30A), encoded as a non-zero unsigned integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Rational Numerator Value (0040,A162) is present.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer denominator of a rational representation of Numeric Value (0040,A30A), encoded as a non-zero unsigned integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Rational Numerator Value (0040,A162) is present.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer denominator of a rational representation of Numeric Value (0040,A30A), encoded as a non-zero unsigned integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Rational Numerator Value (0040,A162) is present.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer denominator of a rational representation of Numeric Value (0040,A30A), encoded as a non-zero unsigned integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Rational Numerator Value (0040,A162) is present.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The integer denominator of a rational representation of Numeric Value (0040,A30A), encoded as a non-zero unsigned integer value. The same number of Values as Numeric Value (0040,A30A) shall be present.
       </p>
       <p>
        Required if Rational Numerator Value (0040,A162) is present.
       </p>

-----------------------------------
Concept Code Sequence | (0040,A168)
-----------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Coded concept value of this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is CODE.
       </p>

---------------------------
Numeric Value | (0040,A30A)
---------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Numeric value for this name-value Item. Only a single Value shall be present.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Numeric value for this name-value Item. Only a single Value shall be present.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Numeric value for this name-value Item. Only a single Value shall be present.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Numeric value for this name-value Item. Only a single Value shall be present.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Numeric value for this name-value Item. Only a single Value shall be present.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

---------------------------------------
Referenced Segment Number | (0062,000B)
---------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Segment Number to which the reference applies.
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Segment Number to which the reference applies. Required if the Referenced SOP Instance is a Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the Segment Number to which the reference applies.
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the segments to which the reference applies identified by Segment Number (0062,0004).
       </p>
       <p>
        Required if the Referenced SOP Instance is a Segmentation or Surface Segmentation and the reference does not apply to all segments and Referenced Frame Number (0008,1160) is not present.
       </p>

---------------------------------------
Selector Sequence Pointer | (0072,0052)
---------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Contains the Data Element Tags of the path to the Sequence that contains the Attribute that is identified by Selector Attribute (0072,0026) or to the Item(s) to be selected in Selector Sequence Pointer Items (0074,1057).
       </p>
       <p>
        This Attribute shall have the same number of Values as the level of nesting of Selector Attribute (0072,0026) or the selected Item(s).
       </p>
       <p>
        Required if Selector Attribute (0072,0026) is nested in one or more Sequences or is absent.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.1
        </span>
        .
       </p>

---------------------------------------------
Referenced Defined Device Index | (300A,0602)
---------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Extended device information is not allowed by default
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Value of Device Index (3010,0039) from the Acquisition Device Sequence (3002,0117) corresponding to the Acquisition Device used in this Item.
       </p>
       <p>
        Required if Acquisition Device Sequence (3002,0117) is present and Value 1 of Image Type (0008,0008) has the Value ORIGINAL or the current Instance was derived from an Instance where Referenced Defined Device Index (300A,0602) was present in the Image Receptor Position Sequence (3002,010E). May be present otherwise.
       </p>

----------------------------------------
RT Accessory Slot Distance | (300A,0613)
----------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Distance in mm from the reference location as specified by RT Device Distance Reference Location Code Sequence (300A,0659) to the RT Accessory Device Slot.
       </p>
       <p>
        Required if RT Accessory Device Slot ID (300A,0615) is present and has a Value.
       </p>

------------------------------------------------------
Referenced Patient Setup Procedure Index | (300A,0796)
------------------------------------------------------
:Action: Keep (K)
:Justication: If present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Value of Patient Treatment Preparation Procedure Index (300A,0795) from Patient Treatment Preparation Procedure Sequence (300A,0790) corresponding to the Patient Treatment Preparation Procedure to which this Sequence Item refers.
       </p>
       <p>
        Required if this Patient Setup Photo is associated with a Patient Treatment Preparation Procedure.
       </p>

---------------------------------------------------------
Referenced RT Accessory Holder Device Index | (300A,060E)
---------------------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Extended device information is not allowed by default
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The Value of Device Index (3010,0039) of the RT Accessory Holder Device in the RT Accessory Holder Definition Sequence (300A,0614).
       </p>
       <p>
        Required if RT Accessory Device Slot ID (300A,0615) is not present.
       </p>
       <p>
        See
        <span href="">
         Section C.36.2.2.3.1
        </span>
        .
       </p>

----------------------------------------------
Equipment Frame of Reference UID | (300A,0675)
----------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Extended device information is not allowed by default
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Frame of Reference identifier for the Treatment Delivery Device.
       </p>
       <p>
        Required if either Imaging Equipment to Treatment Delivery Device Relationship Sequence (300A,07A1) or Patient to Equipment Relationship Sequence (300A,07A0) is present.
       </p>
       <p>
        See
        <span href="">
         Section C.36.12.1
        </span>
        and
        <span href="">
         Section C.36.2.4.12.1.1
        </span>
        .
       </p>

----------------------------------------------
Device Alternate Identifier Type | (3010,001C)
----------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Extended device information is not allowed by default
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Defines the type of Device Alternate Identifier.
       </p>
       <p>
        Required if Device Alternate Identifier (3010,001B) has a Value.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           BARCODE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           RFID
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>

------------------------------------------------
Device Alternate Identifier Format | (3010,001D)
------------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Description of the format in which the Device Alternate Identifier (3010,001B) is issued.
       </p>
       <p>
        Required if Device Alternate Identifier (3010,001B) has a Value.
       </p>
       <p>
        See
        <span href="">
         Section 10.36.1.1
        </span>
        .
       </p>

-------------------------------------------------------
Selector Sequence Pointer Private Creator | (0072,0054)
-------------------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the creator of a group of Private Data Elements used to encode Attributes in the Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        This Attribute shall have the same number of Values as Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        For Values of the Selector Sequence Pointer (0072,0052) that are not the Data Element Tag of a Private Attribute, the corresponding Value in Selector Sequence Pointer Private Creator (0072,0054) shall be empty.
       </p>
       <p>
        Required if Selector Sequence Pointer (0072,0052) is present and one or more of the Values of Selector Sequence Pointer (0072,0052) is the Data Element Tag of a Private Attribute.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.2
        </span>
        .
       </p>

--------------------------------------
Certified Timestamp Type | (0400,0305)
--------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The type of certified timestamp used in Certified Timestamp (0400,0310). Required if Certified Timestamp (0400,0310) is present.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           CMS_TSP
          </span>
         </dt>
         <dd>
          <p>
           Internet X.509 Public Key Infrastructure Time Stamp Protocol
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Digital Signature Security Profiles (see
         <a href="http://dicom.nema.org/medical/dicom/current/output/html/part15.html#PS3.15" target="_blank">
          PS3.15
         </a>
         ) may require the use of a restricted subset of these terms.
        </p>
       </div>

-------------------------------------------
Encrypted Attributes Sequence | (0400,0500)
-------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Sequence of Items containing encrypted DICOM data.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if application level confidentiality is needed and certain recipients are allowed to decrypt all or portions of the Encrypted Attributes Data Set. See
        <span href="">
         Section C.12.1.1.4.1
        </span>
        .
       </p>

---------------------------------------------
Selector Sequence Pointer Items | (0074,1057)
---------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the Item indices in the Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        This Attribute shall have the same number of Values as the Selector Sequence Pointer (0072,0052).
       </p>
       <p>
        The Value 1 identifies the first Item of the corresponding Sequence. The Value 0 identifies all Items of the corresponding Sequence.
       </p>
       <p>
        Required if Selector Sequence Pointer (0072,0052) is present.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.1
        </span>
        .
       </p>

------------------------------------------------
Selector Attribute Private Creator | (0072,0056)
------------------------------------------------
:Action: Keep (K)
:Justication: Common: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identification of the creator of a group of Private Data Elements.
       </p>
       <p>
        Required if the Selector Attribute (0072,0026) Value is the Data Element Tag of a Private Attribute.
       </p>
       <p>
        See
        <span href="">
         Section 10.17.1.2
        </span>
        .
       </p>

--------------------------------
Selector Attribute | (0072,0026)
--------------------------------
:Action: Keep (K)
:Justication: Universally used: if present, it is likely required
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Data Element Tag of the Attribute to be referenced.
       </p>
       <p>
        Required if the selected content is not a Sequence Item.
       </p>

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

--------------------------------------
De-identification Method | (0012,0063)
--------------------------------------
:Action: Keep (K)
:Justication: De-identifaction trace, should be kept and extended
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A description or label of the mechanism or method use to remove the Patient's identity. May be multi-valued if successive de-identification steps have been performed.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            This may be used to describe the extent or thoroughness of the de-identification, for example whether or not the de-identification is for a "Limited Data Set" (as per HIPAA Privacy Rule).
           </p>
          </li>
          <li>
           <p>
            The characteristics of the de-identifying equipment and/or the responsible operator of that equipment may be recorded as an additional Item of the Contributing Equipment Sequence (0018,A001) in the
            <span href="">
             SOP Common Module
            </span>
            . De-identifying equipment may use a Purpose of Reference of
            <a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_109104" target="_blank">
             (109104, DCM, "De-identifying Equipment")
            </a>
            .
           </p>
          </li>
         </ol>
        </div>
       </div>
       <p>
        Required if Patient Identity Removed (0012,0062) is present and has a Value of YES and De-identification Method Code Sequence (0012,0064) is not present. May be present otherwise.
       </p>

----------------------------------------------------
De-identification Method Code Sequence | (0012,0064)
----------------------------------------------------
:Action: Keep (K)
:Justication: De-identifaction trace, should be kept and extended
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A code describing the mechanism or method use to remove the Patient's identity.
       </p>
       <p>
        One or more Items shall be included in this Sequence. Multiple Items are used if successive de-identification steps have been performed or to describe options of a defined profile.
       </p>
       <p>
        Required if Patient Identity Removed (0012,0062) is present and has a Value of YES and De-identification Method (0012,0063) is not present. May be present otherwise.
       </p>

-----------------
KVP | (0018,0060)
-----------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Peak kilo voltage output of the X-Ray generator used.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal peak kilo voltage output of the X-Ray generator used.
       </p>
       <p>
        If Multi-energy Source Technique (0018,9368) in Multi-energy CT X-Ray Source Sequence (0018,9365) (of the referenced Multi-energy CT Path Index (0018,937A)) is "SWITCHING_SOURCE", this Value is the nominal peak value for a switching phase. The switching phase is identified by the Value of X-Ray Source Index (0018,9366) in the Multi-energy CT Path Sequence (0018,9379) corresponding to the Value of Referenced Path Index (0018,9378) in this Sequence.
       </p>
       <p>
        Due to limitations of the generating hardware the actual voltage may not reach the nominal peak value.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

--------------------------------------
Data Collection Diameter | (0018,0090)
--------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        The diameter in mm of the region over which data were collected.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The diameter in mm of the region over which data were collected. See
        <span href="">
         Section C.8.15.3.6.1
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         In the case of an Acquisition Type (0018,9302) of CONSTANT_ANGLE, the diameter is that in a plane normal to the central ray of the diverging X-Ray beam as it passes through the data collection center.
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

-----------------------------------------
Distance Source to Detector | (0018,1110)
-----------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Distance in mm from source to detector center.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This value is traditionally referred to as Source Image Receptor Distance (SID).
        </p>
       </div>
       <p>
        Shall not be present if this Attribute is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Distance in mm from source to detector center. See
        <span href="">
         Section C.8.15.3.6.1
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This value is traditionally referred to as Source Image Receptor Distance (SID).
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

--------------------------
Table Height | (0018,1130)
--------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The distance in mm of the top of the patient table to the center of rotation; below the center is positive.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The distance in mm from the top of the patient table to the center of rotation of the source (i.e., the data collection center or isocenter). The distance is positive when the table is below the data collection center.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

----------------------------------
Gantry/Detector Tilt | (0018,1120)
----------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Nominal angle of tilt in degrees of the scanning gantry. Not intended for mathematical computations.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal angle of tilt in degrees of the scanning gantry. Not intended for mathematical computations. Zero degrees means the gantry is not tilted, negative degrees are when the top of the gantry is tilted away from where the table enters the gantry.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

--------------------------------
Rotation Direction | (0018,1140)
--------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        Direction of rotation of the source when relevant, about nearest principal axis of equipment.
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
           CW
          </span>
         </dt>
         <dd>
          <p>
           clockwise
          </p>
         </dd>
         <dt>
          <span>
           CC
          </span>
         </dt>
         <dd>
          <p>
           counter clockwise
          </p>
         </dd>
        </dl>
       </div>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Direction of rotation of the source about the gantry, as viewed while facing the gantry where the table enters the gantry.
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
           CW
          </span>
         </dt>
         <dd>
          <p>
           clockwise
          </p>
         </dd>
         <dt>
          <span>
           CC
          </span>
         </dt>
         <dd>
          <p>
           counter clockwise
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>
       <p>
        Otherwise may be present if Frame Type (0008,9007) Value 1 of this Frame is DERIVED or Image Type (0008,0008) Value 1 is DERIVED, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>

-------------------------
Filter Type | (0018,1160)
-------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Type of filter(s) inserted into the X-Ray beam.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Type of filter(s) inserted into the X-Ray beam.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           WEDGE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           BUTTERFLY
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           MULTIPLE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           FLAT
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           SHAPED
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           NONE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Multiple type of filters can be expressed by a combination, e.g., BUTTERFLY+WEDGE.
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

---------------------------
Focal Spot(s) | (0018,1190)
---------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Used nominal size of the focal spot in mm.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Used nominal size of the focal spot in mm. The Attribute may only have one or two Values, for devices with variable focal spot, small dimension followed by large dimension
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

-----------------------------
Revolution Time | (0018,9305)
-----------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The time in seconds of a complete revolution of the source around the gantry orbit.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The time in seconds of a complete revolution of the source around the gantry orbit. This Value is independent of the Reconstruction Angle (0018,9319) of the Frame.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>
       <p>
        Otherwise may be present if Frame Type (0008,9007) Value 1 of this Frame is DERIVED or Image Type (0008,0008) Value 1 is DERIVED, and Acquisition Type (0018,9302) is other than CONSTANT_ANGLE.
       </p>

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

-------------------------------------
Total Collimation Width | (0018,9307)
-------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The width of the total collimation (in mm) over the area of active X-Ray detection.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This will be equal the number of effective detector rows multiplied by single collimation width.
        </p>
       </div>
       <p>
        Shall not be present if this Attribute is present in Multi-energy CT Acquisition Sequence (0018,9362) and the Value of this Attribute is not the same in all Items of the Multi-energy CT Acquisition Sequence (0018,9362).
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The width of the total collimation (in mm) over the area of active X-Ray detection.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This will be equal to the number of effective detector rows multiplied by single collimation width.
        </p>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

--------------------------------------
Exposure Modulation Type | (0018,9323)
--------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        A label describing the type of exposure modulation used for the purpose of limiting the dose.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           NONE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A label describing the type of exposure modulation used for the purpose of limiting the dose.
       </p>
       <div>
        <p>
         <strong>
          Defined Terms:
         </strong>
        </p>
        <dl>
         <dt>
          <span>
           NONE
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

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

--------------------------------------
X-Ray Tube Current in mA | (0018,9330)
--------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Nominal X-Ray tube current in milliamperes.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Nominal X-Ray tube current in milliamperes.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

-----------------------------
Exposure in mAs | (0018,9332)
-----------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Optional (3)]::

       <p>
        The exposure expressed in milliampere seconds, for example calculated from exposure time and X-Ray tube current.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The exposure expressed in milliampere seconds, for example calculated from exposure time and X-Ray tube current.
       </p>
       <p>
        Required if Frame Type (0008,9007) Value 1 of this Frame is ORIGINAL or Image Type (0008,0008) Value 1 is ORIGINAL. May be present otherwise.
       </p>

--------------------------------------------------
Referenced Defined Protocol Sequence | (0018,990C)
--------------------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Defined Procedure Protocol SOP Instance(s) that were used for this Instance.
       </p>
       <p>
        Required if this instance is a Performed Procedure Protocol that resulted from a Defined Procedure Protocol. May be present otherwise.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section 10.41.1
        </span>
        .
       </p>

----------------------------------------------------
Referenced Performed Protocol Sequence | (0018,990D)
----------------------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Performed Procedure Protocol SOP Instance(s) that describe the conditions by which this Instance was generated.
       </p>
       <p>
        Required if a related Performed Procedure Protocol SOP Instance was created.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section 10.41.1
        </span>
        .
       </p>

--------------------------------
Acquisition Number | (0020,0012)
--------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Allows identification of study. Not allowed
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        A number identifying the single continuous gathering of data over a period of time that resulted in this image.
       </p>

   - general-acquisition [Mandatory (M)] [Optional (3)]::

       <p>
        A number identifying the single continuous gathering of data over a period of time that resulted in this instance.
       </p>

-----------------------------
Instance Number | (0020,0013)
-----------------------------
:Action: Keep (K)
:Justication: Identifies and orders image within single study. No PI
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        A number that identifies this image.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute was named Image Number in previous releases of this Standard.
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        A number that identifies this Composite Instance.
       </p>

---------------------------------
Patient Orientation | (0020,0020)
---------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Patient direction of the rows and columns of the image. Required if image does not require Image Orientation (Patient) (0020,0037) and Image Position (Patient) (0020,0032) or if image does not require Image Orientation (Slide) (0048,0102). May be present otherwise. See
        <span href="">
         Section C.7.6.1.1.1
        </span>
        for further explanation.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         IODs may have Attributes other than Patient Orientation, Image Orientation, or Image Position (Patient) to describe orientation in which case this Attribute will be zero length.
        </p>
       </div>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Patient Orientation values of the source image.
       </p>
       <p>
        Required if the Value of Spatial Locations Preserved (0028,135A) is REORIENTED_ONLY.
       </p>

------------------------
Laterality | (0020,0060)
------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        Laterality of (paired) body part examined. Required if the body part examined is a paired structure and Image Laterality (0020,0062) or Frame Laterality (0020,9072) or Measurement Laterality (0024,0113) are not present.
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
           R
          </span>
         </dt>
         <dd>
          <p>
           right
          </p>
         </dd>
         <dt>
          <span>
           L
          </span>
         </dt>
         <dd>
          <p>
           left
          </p>
         </dd>
        </dl>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            Some IODs support Image Laterality (0020,0062) at the Image level or Frame Laterality (0020,9072) at the Frame level in the Frame Anatomy Functional Group Macro or Measurement Laterality (0024,0113) at the Measurement level, which can provide a more comprehensive mechanism for specifying the laterality of the body part(s) being examined.
           </p>
          </li>
          <li>
           <p>
            There is no value for both left and right, for which Image Laterality (0020,0062) at the Image level or Frame Laterality (0020,9072) may be used instead.
           </p>
          </li>
          <li>
           <p>
            There is no value for median, for which Primary Anatomic Structure Modifier Sequence (0008,2230) or Anatomic Region Modifier Sequence (0008,2220) may be used instead.
           </p>
          </li>
         </ol>
        </div>
       </div>

---------------------------------------------
Measurement Units Code Sequence | (0040,08EA)
---------------------------------------------
:Action: Keep (K)
:Justication: Describes possibly required acquisition details
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Units of measurement for a numeric value in this name-value Item.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        Required if Value Type (0040,A040) is NUMERIC.
       </p>

----------------------------------
Planar Configuration | (0028,0006)
----------------------------------
:Action: Keep (K)
:Justication: Describes crucial data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Indicates whether the pixel data are encoded color-by-plane or color-by-pixel. Required if Samples per Pixel (0028,0002) has a Value greater than 1. See
        <span href="">
         Section C.7.6.3.1.3
        </span>
        for further explanation.
       </p>

   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Indicates whether the pixel data are encoded color-by-plane or color-by-pixel. Required if Samples per Pixel (0028,0002) has a Value greater than 1. See
        <span href="">
         Section C.7.6.3.1.3
        </span>
        for further explanation.
       </p>

------------------------------------------------
Real World Value Last Value Mapped | (0040,9211)
------------------------------------------------
:Action: Keep (K)
:Justication: Sometimes required in a specific module
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the last stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) or Real World Value LUT Data (0040,9212) of this Item.
       </p>
       <p>
        Required if Pixel Data (7FE0,0010) or Real World Value LUT Data (0040,9212) is present or Double Float Real World Value Last Value Mapped (0040,9213) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be used even when Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are used instead of Pixel Data (7FE0,0010) if an integer of the size of this Attribute is sufficient to define the range.
        </p>
       </div>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.11.1
        </span>
        for further explanation.
       </p>

---------------------------------------
Real World Value LUT Data | (0040,9212)
---------------------------------------
:Action: Keep (K)
:Justication: Describes crucial data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        LUT Data in this Sequence.
       </p>
       <p>
        Required if Real World Value Intercept (0040,9224) is not present.
       </p>

-------------------------------------------------------------
Double Float Real World Value Last Value Mapped | (0040,9213)
-------------------------------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the last stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) of this Item.
       </p>
       <p>
        Required if Real World Value Last Value Mapped (0040,9211) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The same Attribute with a double float precision value is used whether or not Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are present, an integer value is not sufficient.
        </p>
       </div>

--------------------------------------------------------------
Double Float Real World Value First Value Mapped | (0040,9214)
--------------------------------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the first stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) of this Item.
       </p>
       <p>
        Required if Real World Value First Value Mapped (0040,9216) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The same Attribute with a double float precision value is used whether or not Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are present, an integer value is not sufficient.
        </p>
       </div>

-------------------------------------------------
Real World Value First Value Mapped | (0040,9216)
-------------------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Specifies the first stored value mapped for the Real Word Value Intercept (0040,9224) and Real World Value Slope (0040,9225) or Real World Value LUT Data (0040,9212) of this Item.
       </p>
       <p>
        Required if Pixel Data (7FE0,0010) or Real World Value LUT Data (0040,9212) is present or Double Float Real World Value First Value Mapped (0040,9214) is absent.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute may be used even when Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are used instead of Pixel Data (7FE0,0010) if an integer of the size of this Attribute is sufficient to define the range.
        </p>
       </div>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.11.1
        </span>
        for further explanation.
       </p>

----------------------------------------
Real World Value Intercept | (0040,9224)
----------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Intercept value in relationship between stored values (SV) and the Real World values.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.11.1.2
        </span>
        for further explanation.
       </p>
       <p>
        Required if Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are present or Real World Value LUT Data (0040,9212) is not present.
       </p>

------------------------------------
Real World Value Slope | (0040,9225)
------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Slope value in relationship between stored values (SV) and the Real World Values.
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.16.2.11.1.2
        </span>
        for further explanation.
       </p>
       <p>
        Required if Float Pixel Data (7FE0,0008) or Double Float Pixel Data (7FE0,0009) are present or Real World Value LUT Data (0040,9212) is not present.
       </p>

--------------------------------------------------------
HL7 Structured Document Reference Sequence | (0040,A390)
--------------------------------------------------------
:Action: Remove (X)
:Justication: References outside UIDs
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Sequence of Items defining mapping between HL7 Instance Identifiers of unencapsulated HL7 Structured Documents referenced from the current SOP Instance as if they were DICOM Composite SOP Instances defined by SOP Class and Instance UID pairs. May also define a means of accessing the Documents.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.6
        </span>
        .
       </p>
       <p>
        Required if unencapsulated HL7 Structured Documents are referenced within the Instance. Every such document so referenced is required to have a corresponding Item in this Sequence.
       </p>

-------------------------------------
HL7 Instance Identifier | (0040,E001)
-------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Is a direct identifier
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Instance Identifier of the encapsulated HL7 Structured Document, encoded as a UID (OID or UUID), concatenated with a caret ("^") and Extension value (if Extension is present in Instance Identifier).
       </p>
       <p>
        Required if Type of Instances (0040,E020) is CDA.
       </p>

   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Instance Identifier of the referenced HL7 Structured Document, encoded as a UID (OID or UUID), concatenated with a caret ("^") and Extension value (if Extension is present in Instance Identifier).
       </p>

-------------------------------------------
Extended Offset Table Lengths | (7FE0,0002)
-------------------------------------------
:Action: Keep (K)
:Justication: Describes critical data format
:Basic Profile: N/A
:In Modules:
   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Byte lengths of the Frames in the Sequence of Items in Encapsulated Pixel Data encoded in Pixel Data (7FE0,0010).
       </p>
       <p>
        See
        <span href="">
         Section C.7.6.3.1.8
        </span>
        .
       </p>
       <p>
        Required if Extended Offset Table (7FE0,0001) is present.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <div>
         <ol type="1">
          <li>
           <p>
            This Attribute is only sent when each Frame is entirely contained within one Fragment as a single contiguous span of bytes so that it is not necessary to assemble the Frame from Fragments with delimiters.
           </p>
          </li>
          <li>
           <p>
            The length encoded in this Attribute may be an odd number if the compressed bitstream for the Frame is an odd length; i.e., it does not include any trailing padding required to make the Item an even length.
           </p>
          </li>
         </ol>
        </div>
       </div>

---------------------------------
Universal Entity ID | (0040,0032)
---------------------------------
:Action: Remove (X)
:Justication: Universal ID: could be traced to all kinds of insitutes or entities
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Universal or unique identifier for an entity. Required if Local Namespace Entity ID (0040,0031) is not present; may be present otherwise.
       </p>

--------------------------------------
Universal Entity ID Type | (0040,0033)
--------------------------------------
:Action: Remove (X)
:Justication: Universal ID: could be traced to all kinds of insitutes or entities
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Standard defining the format of the Universal Entity ID. Required if Universal Entity ID (0040,0032) is present.
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
           DNS
          </span>
         </dt>
         <dd>
          <p>
           An Internet dotted name. Either in ASCII or as integers
          </p>
         </dd>
         <dt>
          <span>
           EUI64
          </span>
         </dt>
         <dd>
          <p>
           An IEEE Extended Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           ISO
          </span>
         </dt>
         <dd>
          <p>
           An International Standards Organization Object Identifier
          </p>
         </dd>
         <dt>
          <span>
           URI
          </span>
         </dt>
         <dd>
          <p>
           Uniform Resource Identifier
          </p>
         </dd>
         <dt>
          <span>
           UUID
          </span>
         </dt>
         <dd>
          <p>
           The DCE Universal Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           X400
          </span>
         </dt>
         <dd>
          <p>
           An X.400 MHS identifier
          </p>
         </dd>
         <dt>
          <span>
           X500
          </span>
         </dt>
         <dd>
          <p>
           An X.500 directory name
          </p>
         </dd>
        </dl>
       </div>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Standard defining the format of the Universal Entity ID. Required if Universal Entity ID (0040,0032) is present.
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
           DNS
          </span>
         </dt>
         <dd>
          <p>
           An Internet dotted name. Either in ASCII or as integers
          </p>
         </dd>
         <dt>
          <span>
           EUI64
          </span>
         </dt>
         <dd>
          <p>
           An IEEE Extended Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           ISO
          </span>
         </dt>
         <dd>
          <p>
           An International Standards Organization Object Identifier
          </p>
         </dd>
         <dt>
          <span>
           URI
          </span>
         </dt>
         <dd>
          <p>
           Uniform Resource Identifier
          </p>
         </dd>
         <dt>
          <span>
           UUID
          </span>
         </dt>
         <dd>
          <p>
           The DCE Universal Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           X400
          </span>
         </dt>
         <dd>
          <p>
           An X.400 MHS identifier
          </p>
         </dd>
         <dt>
          <span>
           X500
          </span>
         </dt>
         <dd>
          <p>
           An X.500 directory name
          </p>
         </dd>
        </dl>
       </div>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Standard defining the format of the Universal Entity ID. Required if Universal Entity ID (0040,0032) is present.
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
           DNS
          </span>
         </dt>
         <dd>
          <p>
           An Internet dotted name. Either in ASCII or as integers
          </p>
         </dd>
         <dt>
          <span>
           EUI64
          </span>
         </dt>
         <dd>
          <p>
           An IEEE Extended Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           ISO
          </span>
         </dt>
         <dd>
          <p>
           An International Standards Organization Object Identifier
          </p>
         </dd>
         <dt>
          <span>
           URI
          </span>
         </dt>
         <dd>
          <p>
           Uniform Resource Identifier
          </p>
         </dd>
         <dt>
          <span>
           UUID
          </span>
         </dt>
         <dd>
          <p>
           The DCE Universal Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           X400
          </span>
         </dt>
         <dd>
          <p>
           An X.400 MHS identifier
          </p>
         </dd>
         <dt>
          <span>
           X500
          </span>
         </dt>
         <dd>
          <p>
           An X.500 directory name
          </p>
         </dd>
        </dl>
       </div>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Standard defining the format of the Universal Entity ID. Required if Universal Entity ID (0040,0032) is present.
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
           DNS
          </span>
         </dt>
         <dd>
          <p>
           An Internet dotted name. Either in ASCII or as integers
          </p>
         </dd>
         <dt>
          <span>
           EUI64
          </span>
         </dt>
         <dd>
          <p>
           An IEEE Extended Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           ISO
          </span>
         </dt>
         <dd>
          <p>
           An International Standards Organization Object Identifier
          </p>
         </dd>
         <dt>
          <span>
           URI
          </span>
         </dt>
         <dd>
          <p>
           Uniform Resource Identifier
          </p>
         </dd>
         <dt>
          <span>
           UUID
          </span>
         </dt>
         <dd>
          <p>
           The DCE Universal Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           X400
          </span>
         </dt>
         <dd>
          <p>
           An X.400 MHS identifier
          </p>
         </dd>
         <dt>
          <span>
           X500
          </span>
         </dt>
         <dd>
          <p>
           An X.500 directory name
          </p>
         </dd>
        </dl>
       </div>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Standard defining the format of the Universal Entity ID. Required if Universal Entity ID (0040,0032) is present.
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
           DNS
          </span>
         </dt>
         <dd>
          <p>
           An Internet dotted name. Either in ASCII or as integers
          </p>
         </dd>
         <dt>
          <span>
           EUI64
          </span>
         </dt>
         <dd>
          <p>
           An IEEE Extended Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           ISO
          </span>
         </dt>
         <dd>
          <p>
           An International Standards Organization Object Identifier
          </p>
         </dd>
         <dt>
          <span>
           URI
          </span>
         </dt>
         <dd>
          <p>
           Uniform Resource Identifier
          </p>
         </dd>
         <dt>
          <span>
           UUID
          </span>
         </dt>
         <dd>
          <p>
           The DCE Universal Unique Identifier
          </p>
         </dd>
         <dt>
          <span>
           X400
          </span>
         </dt>
         <dd>
          <p>
           An X.400 MHS identifier
          </p>
         </dd>
         <dt>
          <span>
           X500
          </span>
         </dt>
         <dd>
          <p>
           An X.500 directory name
          </p>
         </dd>
        </dl>
       </div>

--------------------------
Retrieve URI | (0040,E010)
--------------------------
:Action: Remove (X)
:Justication: Retrieval URI, DANGER Will Robinson!
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Required with valid value (1)]::

       <p>
        URI/URL specifying the location of the referenced Instance(s). Includes fully specified scheme, authority, path, and query in accordance with
        <span href="">
         [
         <abbr>
          RFC3986
         </abbr>
         ]
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The VR of this Data Element has changed from UT to UR.
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Retrieval access path to HL7 Structured Document. Includes fully specified scheme, authority, path, and query in accordance with
        <span href="">
         [
         <abbr>
          RFC3986
         </abbr>
         ]
        </span>
        .
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The VR of this Data Element has changed from UT to UR.
        </p>
       </div>

--------------------------
Content Date | (0008,0023)
--------------------------
:Action: Remove (X)
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

--------------------------
Content Time | (0008,0033)
--------------------------
:Action: Remove (X)
:Justication: Grand-challenge binds together series as a single value
:Basic Profile: Z/D
:In Modules:
   - general-image [Mandatory (M)] [Conditional; must be present but can be empty if condition is met (2C)]::

       <p>
        The time the image pixel data creation started.
       </p>
       <p>
        Required if image is part of a Series in which the images are temporally related. May be present otherwise.
       </p>

---------------------------------------------------
Conversion Source Attributes Sequence | (0020,9172)
---------------------------------------------------
:Action: Remove (X)
:Justication: Describes source DICOM if conversion: can be safely excluded
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The set of images or other composite SOP Instances that were converted to this Instance.
       </p>
       <p>
        If this Instance was converted from a specific Frame in the source Instance, the reference shall include the Frame Number.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>
       <p>
        Required if this Instance was created by conversion from a DICOM source, and Conversion Source Attributes Sequence (0020,9172) is not present in an Item of Shared Functional Groups Sequence (5200,9229) or Per-Frame Functional Groups Sequence (5200,9230).
       </p>

---------------------------------------
Manufacturer's Model Name | (0008,1090)
---------------------------------------
:Action: Remove (X)
:Justication: Optional in a sometimes manditory module
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer's model name of the device.
       </p>

   - device [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer's model name of the device.
       </p>

   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's model name of the equipment that produced the Composite Instances.
       </p>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's model name of the equipment that contributed to the Composite Instance.
       </p>

   - specimen [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer's model name of the container component.
       </p>

-------------------------------------
Responsible Person Role | (0010,2298)
-------------------------------------
:Action: Remove (X)
:Justication: Counter part was removed in basic profile
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Relationship of Responsible Person to the Patient.
       </p>
       <p>
        See
        <span href="">
         Section C.7.1.1.1.2
        </span>
        for Defined Terms.
       </p>
       <p>
        Required if Responsible Person is present and has a Value.
       </p>

-----------------------------
LUT Explanation | (0028,3003)
-----------------------------
:Action: Remove (X)
:Justication: Def. optional, where required the parent-sequence is user optional
:Basic Profile: N/A
:In Modules:
   - general-image [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Free form text explanation of the meaning of the transformation in this Item.
       </p>

   - voi-lut [User Optional (U)] [Optional (3)]::

       <p>
        Free form text explanation of the meaning of the LUT.
       </p>

------------------------------------------------
Purpose of Reference Code Sequence | (0040,A170)
------------------------------------------------
:Action: Remove (X)
:Justication: Def. optional, where required the parent-sequence is user optional
:Basic Profile: N/A
:In Modules:
   - general-reference [User Optional (U)] [Optional (3)]::

       <p>
        Describes the purpose for which the reference is made, that is what role the source Instance(s) played in the derivation of this Instance.
       </p>
       <p>
        Only a single Item single Item is permitted in this Sequence.
       </p>

   - general-series [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Describes the purpose for which the reference is made.
       </p>
       <p>
        Zero or more Items shall be included in this Sequence.
       </p>
       <p>
        When absent, implies that the reason for the reference is unknown.
       </p>

   - sop-common [Mandatory (M)] [Required with valid value (1)]::

       <p>
        Describes the purpose for which the related equipment is being referenced.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>
       <p>
        See
        <span href="">
         Section C.12.1.1.5
        </span>
        for further explanation.
       </p>

-------------------------------------
Pixel Data Provider URL | (0028,7FE0)
-------------------------------------
:Action: Remove (X)
:Justication: URL to gather pixel data from, DANGER Will Robinson!
:Basic Profile: N/A
:In Modules:
   - image-pixel [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        A URL of a provider service that supplies the pixel data of the Image.
       </p>
       <p>
        Required if the image is to be transferred in one of the following presentation contexts identified by Transfer Syntax UID:
       </p>
       <div>
        <ul>
         <li>
          <p>
           1.2.840.10008.1.2.4.94 (DICOM JPIP Referenced Transfer Syntax)
          </p>
         </li>
         <li>
          <p>
           1.2.840.10008.1.2.4.95 (DICOM JPIP Referenced Deflate Transfer Syntax)
          </p>
         </li>
        </ul>
       </div>
       <div>
        <h3>
         Note
        </h3>
        <p>
         The VR of this Data Element has changed from UT to UR.
        </p>
       </div>

---------------------------------
Query/Retrieve View | (0008,0053)
---------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required if special operation has ever occured to the data.
:Basic Profile: N/A
:In Modules:
   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The view requested during the C-MOVE operation that resulted in the transfer of this Instance.
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
           CLASSIC
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           ENHANCED
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        Required if the Instance has ever been converted from its source form as the result of a C-MOVE operation with a specific view.
       </p>

------------------------------
Institution Name | (0008,0080)
------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required, under some condition
:Basic Profile: X/Z/D
:In Modules:
   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Institution where the equipment that produced the Composite Instances is located.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Attribute represents the organizational context only for the Equipment IE, and should not be construed to be a substitute for Issuer of Patient ID (0010,0021) or Issuer of Accession Number (0008,0051).
        </p>
       </div>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Code Sequence (0008,0082) is not present. May be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Code Sequence (0008,0082) is not present. May be present otherwise.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Code Sequence (0008,0082) is not present. May be present otherwise.
       </p>

---------------------------------------
Institution Code Sequence | (0008,0082)
---------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required, under some condition
:Basic Profile: X/Z/D
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Name (0008,0080) is not present. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Name (0008,0080) is not present. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Institution or organization to which the identified individual is responsible or accountable.
       </p>
       <p>
        Required if Institution Name (0008,0080) is not present. May be present otherwise.
       </p>
       <p>
        Only a single Item shall be included in this Sequence.
       </p>

-------------------------------------------------
Context Group Extension Creator UID | (0008,010D)
-------------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Identifies a person or context group, sometimes required
:Basic Profile: N/A
:In Modules:
   - clinical-trial-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - contrast-bolus [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - ct-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - device [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - enhanced-patient-orientation [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - general-equipment [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - general-image [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - general-reference [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - multi-energy-ct-image [Conditional (C)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - sop-common [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies the person or organization who created an extension to the Context Group. See
        <span href="">
         Section 8.7
        </span>
        .
       </p>
       <p>
        Required if the Value of Context Group Extension Flag (0008,010B) is "Y".
       </p>

--------------------------------------------
Patient's Alternative Calendar | (0010,0035)
--------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required under some conditions: dummy if present
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        The Alternative Calendar used for Patient's Birth Date in Alternative Calendar (0010,0033) and Patient's Death Date in Alternative Calendar (0010,0034).
       </p>
       <p>
        See
        <span href="">
         Section C.7.1.5
        </span>
        for Defined Terms.
       </p>
       <p>
        Required if either Patient's Birth Date in Alternative Calendar (0010,0033) or Patient's Alternative Death Date in Calendar (0010,0034) is present.
       </p>

---------------------------------------
Local Namespace Entity ID | (0040,0031)
---------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: Required under some conditions: dummy if present
:Basic Profile: N/A
:In Modules:
   - general-series [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - general-study [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - patient-study [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

   - specimen [User Optional (U)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Identifies an entity within the local namespace or domain. Required if Universal Entity ID (0040,0032) is not present; may be present otherwise.
       </p>

----------------------------------
Device Serial Number | (0018,1000)
----------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: IOD conformance: sometimes required
:Basic Profile: X/Z/D
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer's serial number of the device.
       </p>

   - device [User Optional (U)] [Optional (3)]::

       <p>
        Manufacturer's serial number of the device.
       </p>

   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's serial number of the equipment that produced the Composite Instances.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This identifier corresponds to the device that actually created the images, such as a CR plate reader or a CT console, and may not be sufficient to identify all of the equipment in the imaging chain, such as the generator or gantry or plate.
        </p>
       </div>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's serial number of the equipment that contributed to the Composite Instance.
       </p>

-------------------------------
Software Versions | (0018,1020)
-------------------------------
:Action: Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR (Z)
:Justication: IOD conformance: sometimes required
:Basic Profile: N/A
:In Modules:
   - ct-image [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Manufacturer's designation of software version of the equipment.
       </p>

   - general-equipment [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's designation of software version of the equipment that produced the Composite Instances. See
        <span href="">
         Section C.7.5.1.1.3
        </span>
        .
       </p>

   - sop-common [Mandatory (M)] [Optional (3)]::

       <p>
        Manufacturer's designation of the software version of the equipment that contributed to the Composite Instance. See
        <span href="">
         Section C.7.5.1.1.3
        </span>
        .
       </p>

--------------------------------------
DICOM Retrieval Sequence | (0040,E021)
--------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances via the DICOM Retrieve Service.
       </p>
       <p>
        Required if DICOM Media Retrieval Sequence (0040,E022), WADO Retrieval Sequence (0040,E023), WADO-RS Retrieval Sequence (0040,E025) and XDS Retrieval Sequence (0040,E024) are not present. May be present otherwise.
       </p>
       <p>
        This Sequence shall only identify sources known to have Instances referenced in Referenced SOP Sequence (0008,1199).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

--------------------------------------------
DICOM Media Retrieval Sequence | (0040,E022)
--------------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances from Media.
       </p>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), WADO Retrieval Sequence (0040,E023), and WADO-RS Retrieval Sequence (0040,E025) and XDS Retrieval Sequence (0040,E024) are not present. May be present otherwise.
       </p>
       <p>
        This Sequence shall only identify media known to have Instances referenced in Referenced SOP Sequence (0008,1199).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

-------------------------------------
WADO Retrieval Sequence | (0040,E023)
-------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances available via WADO-URI.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         This Sequence addresses use of the URI-based Web Access to DICOM Objects. Retrieval via the IHE XDS-I.b RAD-69 Transaction
         <span href="">
          [
          <abbr>
           IHE RAD TF-2
          </abbr>
          ]
         </span>
         is addressed in the XDS Retrieval Sequence (0040,E024).
        </p>
       </div>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), DICOM Media Retrieval Sequence (0040,E022), WADO-RS Retrieval Sequence (0040,E025) and XDS Retrieval Sequence (0040,E024) are not present. May be present otherwise.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

------------------------------------
XDS Retrieval Sequence | (0040,E024)
------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances using the IHE XDS-I.b RAD-69 Transaction.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Retrieval via WADO-URI is addressed by the WADO Retrieval Sequence (0040,E023). Retrieval via WADO-RS is addressed by the WADO-RS Retrieval Sequence (0040,E025).
        </p>
       </div>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), DICOM Media Retrieval Sequence (0040,E022), WADO-RS Retrieval Sequence (0040,E025) and WADO Retrieval Sequence (0040,E023) are not present. May be present otherwise.
       </p>
       <p>
        This Sequence shall only identify repositories known to have Instances referenced in Referenced SOP Sequence (0008,1199).
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

----------------------------------------
WADO-RS Retrieval Sequence | (0040,E025)
----------------------------------------
:Action: Replace with a non-zero length value that may be a dummy value and consistent with the VR (D)
:Justication: No retrieval will be done; parent sequence should have been removed
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Conditional; required with valid value if condition is met (1C)]::

       <p>
        Details for retrieving Instances via WADO-RS.
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Retrieval via WADO-URI is addressed in the WADO Retrieval Sequence (0040,E023). Retrieval via the IHE XDS-I.b RAD-69 Transaction
         <span href="">
          [
          <abbr>
           IHE RAD TF-2
          </abbr>
          ]
         </span>
         is addressed in the XDS Retrieval Sequence (0040,E024).
        </p>
       </div>
       <p>
        Required if DICOM Retrieval Sequence (0040,E021), DICOM Media Retrieval Sequence (0040,E022), WADO Retrieval Sequence (0040,E023) and XDS Retrieval Sequence (0040,E024) are not present. May be present otherwise.
       </p>
       <p>
        One or more Items shall be included in this Sequence.
       </p>

-----------------------------
Slice Thickness | (0018,0050)
-----------------------------
:Action: Keep (K)
:Justication: Generally required for viewers
:Basic Profile: N/A
:In Modules:
   - image-plane [Mandatory (M)] [Required; value may be empty (2)]::

       <p>
        Nominal slice thickness, in mm.
       </p>
