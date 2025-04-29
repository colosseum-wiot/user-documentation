Colosseum Architecture
=====================

The Colosseum has four Internet-facing components that users will interact with once connected to the VPN:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Resource
     - Address
     - Description
   * - SSH Gateway
     - gw.colosseum.net
     - This is the gateway for the user to access Colosseum resources 
   * - User Website
     - https://experiments.colosseum.net
     - This is the website which can be used by set up Colosseum resource reservations

From the SSH Gateway, users can access the following resources:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Resource
     - Address
     - Description
   * - File Proxy Server
     - file-proxy
     - File Proxy is a server that users can use to access their Colosseum network storage, including the images directory, where SRN images may be uploaded.
   * - SRNs
     - teamname-srn#
     - *hostnames provided in reservation info*
       Once a reservation becomes active, users may access their allocated SRNs which will have the specified container preloaded per the reservation settings.

This diagram shows a logical representation of Colosseum resources available to the user perspective.

.. figure:: /_static/resources/user_guide/wiki/colosseum_architecture/colosseum_logical_diagram.png
   :alt: Colosseum Architecture Diagram
   :align: center
   
   Logical representation of Colosseum resources