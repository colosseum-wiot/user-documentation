Colosseum Architecture
=====================

:Created: 2020-03-31T14:59:22-04:00
:Updated: 2020-03-31T14:59:23-04:00

:Tags: architecture, FD_V2_537243 Import

The Colosseum has four Internet-facing components that users will interact with:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Resource
     - Address
     - Description
   * - SSH Gateway
     - 129.10.14.202
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

.. figure:: /_static/images/architecture.png
   :alt: Colosseum Architecture Diagram
   :align: center
   
   Logical representation of Colosseum resources