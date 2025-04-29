Collaboration Network
=====================

The Colosseum supports a collaboration channel which allows users and bots to exchange messages outside of the RF environment. The collaboration system will be comprised of a wired IP network that connects user containers, bots, and the collaboration server. The server will act as a PUB/SUB for tracking which users and bots are available for collaboration messages. The collaboration server will publish the IPs of each user subscribed. For scrimmages and competition events, each team will only be allowed a single collaboration gateway in their network. For batch mode sessions, the user defines which nodes will function as a collaboration gateway. For interactive sessions, all nodes will be configured as a collaboration gateway to facilitate development.

Network Design
-------------

A collaboration network and server will be allocated to each reservation. The network and server will only be accessible by nodes within the reservation. The collaboration network will consist of a single /24 broadcast domain and will only require link local host routes. The IP address 3rd octet will be the same for all nodes and server in a reservation and will be defined at allocation time. Each collaboration gateway interface will be named col0. The servers IP address 4th octet will always be 2. Table 1 summarizes the network design for the Collaboration System.

.. list-table:: Table 1 - Collaboration System Network Addresses
   :header-rows: 1
   :widths: 50 50

   * - Item
     - Value
   * - Collaboration Container Interface
     - col0
   * - Collaboration Network
     - 172.30.<res>.<node> / 24
   * - CollabNet101 – 228
     - Host IDs (for SRNs 1 – 128)
   * - Host IDs (for SRNs 1 – 128)
     - 101 – 228
   * - Collaboration Server IPs
     - 172.30.<res>.2 / 24

Configuration File
~~~~~~~~~~~~~~~~~

A configuration file will be pushed into each user container that provides the IP address of the collaboration server. For information on this file, see the colosseum_config.ini section of the :doc:`Radio Command and Control (C2) API </radio_api_traffic/radio_command_and_control_c2_api>`.

Interactive Practice Sessions
----------------------------

For interactive sessions, all SRNs will be attached to the collaboration system and have an attached col0 interface. A single server will be allocated to the reservation and identified via both the 3rd octet of the col0 interface and the configuration file. The col0 interface can be shut down or brought up at any time by the user inside their container.

Batch Mode Sessions
------------------

For batch sessions, the user must specify which nodes will have the collaboration gateway interface attached. The user can choose that all, some, or none of the nodes have a collaboration gateway attached. A single server will be allocated to the reservation and identified via both the 3rd octet of the col0 interface and the configuration file. 

In order to specify that a node be attached to the collaboration network, the user should set the variable of the batch file "isGateway" to true or false. For more information on the batch file format, see the :doc:`Batch Mode Format and Process </reservations/batch_mode_format>` document.

SC2 Matches and Scrimmages
-------------------------

For all competition events, the user collaboration gateway will be assigned by the event coordinators. Only one node in the user network will serve as a collaboration gateway and thus only one node will have a col0 interface attached. This single node will be the only system capable of accessing the collaboration server and other teams or bots via the collaboration network. In scrimmage mode, containers should use the existence of the col0 interface to determine that they are a gateway node. A single server will be allocated to the reservation and identified via both the 3rd octet of the col0 interface and the configuration file.

Log Files
--------

Collaboration server log files and packet captures of all collaboration gateways will be saved for each session. The log files will be moved to the user's team folder on the NAS at the end of each reservation and stored in a folder named ``RESERVATION-###`` where the number corresponds to the reservation ID. The files will be named according to Table 3.

.. list-table:: Table 3 - Collaboration System Log Files
   :header-rows: 1
   :widths: 50 50

   * - File Type
     - Naming Format
   * - Collaboration Server Log
     - <team name>_<ReservationID>_<SRN ID>_<Date-Time>.log
   * - Packet Capture Files
     - <team name>_<ReservationID>_<SRN ID>_<SRN_Network Bridge>_<Date-Time>.pcap
