-------------------------------------
Quality Control Subject | (0010,0200)
-------------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - patient [Mandatory (M)] [Optional (3)]::

       <p>
        Indicates whether or not the subject is a quality control phantom.
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
           YES
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
         <dt>
          <span>
           NO
          </span>
         </dt>
         <dd>
          <p>
          </p>
         </dd>
        </dl>
       </div>
       <p>
        If this Attribute is absent, then the subject may or may not be a phantom.
       </p>
       <p>
        This Attribute describes a characteristic of the Imaging Subject. It is distinct from Quality Control Image (0028,0300) in the
        <span href="">
         General Image Module
        </span>
        , which is used to describe an image acquired.
       </p>
