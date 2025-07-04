--------------------------------
NTP Source Address | (0018,1803)
--------------------------------
:Action: Remove (X)
:Justication: [AUTO] Attribute-Module type
:Basic Profile: N/A
:In Modules:
   - synchronization [Conditional (C)] [Optional (3)]::

       <p>
        IP Address of NTP, SNTP, or PTP time source. IPv4 addresses shall be in dotted decimal (e.g., 192.168.1.1). The IPv6 addresses shall be in colon separated hexadecimal (e.g., 12:34:56:78:9a:bc:de:f0).
       </p>
       <div>
        <h3>
         Note
        </h3>
        <p>
         Identity of this value in two Instances acquired contemporaneously implies a common time base. The NTP Source Address might not persist over time.
        </p>
       </div>
