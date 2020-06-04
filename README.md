 requires: 

  * 3 tasks:
    * gather hostname
    * gather ip 
    * launch vm with values gathered 

  * 3 option Types:
    * 1 vro script return value for hostnames
    * 2 vro script return value for ips 
    * 3 text for appliance url  

  * Cypher secret:
    * reference in launch task as Command Arguments:
      * <%= cypher.read('secret/authtoken') %>


