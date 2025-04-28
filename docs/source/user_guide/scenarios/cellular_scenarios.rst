Cellular Scenarios
================

SCOPE Scenarios
---------------

These are a set of RF cellular scenarios to use with the Colosseum wireless network emulator. Scenarios have been designed in three different urban setups:

1. Rome, Italy
2. Boston, MA, US
3. Salt Lake City, UT, US (POWDER scenario)

For the Rome and Boston scenarios, the locations of the base station reflect real cell tower deployments taken from the OpenCelliD database. For the POWDER scenario, locations mirror the coordinates of the rooftop base stations deployed in the POWDER testbed in Salt Lake City.

Different versions of the above scenarios have been created for different numbers of base stations and users, different distances from the base stations users are deployed, and different mobility speeds of the users. 

Available distances between users and base stations:

- **Close**: users are deployed within 20 m from the base stations
- **Medium**: users are deployed within 50 m from the base stations
- **Far**: users are deployed within 100 m from the base stations

Available user mobility speeds:

- **Static**: users do not move for the whole duration of the scenario
- **Moderate**: users move at 3 m/s
- **Fast**: users move at 5 m/s

.. note::
  These scenarios cluster nodes in groups of 5. This means that nodes 1-5 are emulated to be closer to each other than they are to the other nodes of the scenario. The same holds for the remaining nodes, i.e., nodes 6-10, 11-15, 16-20, 21-25, 26-30, 31-35, 36-40, 41-45, and 46-50.

Rome Scenarios
^^^^^^^^^^^^^^

The Rome scenario captures the dynamics of the city center of Rome, Italy. A total of 50 nodes are involved: 10 BSs and 40 UEs (4 UEs assigned to each BS randomly scattered around it). This is one of the densest scenarios in Colosseum and covers an area of 0.5 km².

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/rome.jpg
   :width: 300px
   :alt: Rome Cellular Scenario
   :align: center

**Node Pattern**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Node in Colosseum
     - Node in the Scenario
   * - Node 1
     - BS 1
   * - Node 2
     - UE 1 assigned to BS 1
   * - Node 3
     - UE 2 assigned to BS 1
   * - Node 4
     - UE 3 assigned to BS 1
   * - Node 5
     - UE 4 assigned to BS 1
   * - Node 6
     - BS 2
   * - Node 7
     - UE 5 assigned to BS 2
   * - ...
     - ...
   * - Node 46
     - BS 10
   * - Node 47
     - UE 37 assigned to BS 10
   * - Node 48
     - UE 38 assigned to BS 10
   * - Node 49
     - UE 39 assigned to BS 10
   * - Node 50
     - UE 40 assigned to BS 10

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 1017 (close static), 1018 (close moderate), 1028 (close fast), 1035 (medium static), 1019 (far static)
   * - Duration
     - 600 s, cyclable
   * - RF Description
     - Single tap; large scale
   * - Traffic ID
     - 10170, 10180, 10190, 10280, 10350
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 50
   * - Number of Base Station Nodes
     - 10
   * - Number of Users per Base Station
     - 4

Boston Scenarios
^^^^^^^^^^^^^^^^

The Boston scenario captures the dynamics of downtown Boston, U.S. A total of 50 nodes are involved: 10 BSs and 40 users. This scenario covers an area of 0.95 km².

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/boston.jpeg
   :width: 300px
   :alt: Boston Cellular Scenario
   :align: center

The sequence of the nodes in the scenario follows the same pattern as the Rome scenarios shown above.

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 1031 (close static), 1033 (close moderate), 1034 (close fast), 1036 (medium static), 1024 (far static)
   * - Duration
     - 600 s, cyclable
   * - RF Description
     - Single tap; large scale
   * - Traffic ID
     - 10310, 10330, 10340, 10360, 10240
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 50
   * - Number of Base Station Nodes
     - 10
   * - Number of Users per Base Station
     - 4

POWDER Scenarios
^^^^^^^^^^^^^^^^

The POWDER scenario mirrors the setup of the rooftop BSs deployed in the POWDER platform in Salt Lake City, U.S. A total of 40 nodes are involved: 8 BSs and 32 UEs. This scenario is the sparsest with an area of 3.6 km².

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/powder.jpg
   :width: 300px
   :alt: POWDER Testbed Cellular Scenario
   :align: center

The sequence of the nodes in the scenario follows the same pattern as the Rome scenarios shown above, but stops at node 40.

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 1025 (close static), 1026 (close moderate), 1030 (close fast), 1041 (medium static), 1027 (far static)
   * - Duration
     - 600 s, cyclable
   * - RF Description
     - Single tap; large scale
   * - Traffic ID
     - 10250, 10260, 10300, 10410, 10270
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 40
   * - Number of Base Station Nodes
     - 8
   * - Number of Users per Base Station
     - 4

**References**

- L. Bonati, S. D'Oro, S. Basagni, and T. Melodia, "SCOPE: An Open and Softwarized Prototyping Platform for NextG Systems," in Proceedings of ACM MobiSys, June 2021. [`pdf <https://ece.northeastern.edu/wineslab/papers/bonati2021scope.pdf>`_] [`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/bonati2021scope.txt>`_]

- POWDER Deployment. 2021. https://www.powderwireless.net/area.


Cellular Rural Small Static Scenarios (35001-35005)
------------------------------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Label
     - Value
   * - Version
     - Formal
   * - RF ID
     - 35001, 35002, 35003, 35004, 35005
   * - RF Description
     - 35001 (Cellular Rural Small 1 GHz Static 1 + 40 dB)
       35002 (Cellular Rural Small 3.6 GHz Static 1 + 51 dB)
       35003 (Cellular Rural Small 3.6 GHz Static 1 + 40 dB)
       35004 (Cellular Rural Small 3.6 GHz Static 1 at 3.6 GHz + 51 dB)
       35005 (Cellular Rural Small 3.6 GHz Static 1 at 3.6 GHz + 40 dB)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - N/A
   * - Traffic Description
     - N/A
   * - Center Frequency
     - 1 GHz (35001, 35002, 35003)
       3.6 GHz (35004, 35005)
   * - Number of Nodes
     - 13
   * - Duration
     - 1 second

**Narrative**

This set of scenarios aims at replicating a generic rural environment with one center node (e.g., a Base Station (BS)) and 12 others (e.g., User Equipments (UE)) randomly scattered around. The channel has been created via a mathematical model at two center frequencies: 1 GHz and 3.6 GHz. Only the links between the BS and the UEs (and vice-versa) have been defined, all others are set to 0.

**Node Placement**

The BS is located in the center of a 20x20 meters area, with the UEs randomly scattered around. The height of the nodes is:

- BS-01 height: 3 meters
- UE height: 1 meter

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/cellular_rural_node_placement.png
   :width: 300px
   :alt: Cellular Rural Node Placement
   :align: center

**Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Cellular Rural Small [1 GHz - 3.6 GHz] Static 1 [at 3.6 GHz] + [40 - 51] dB
   * - Scenario ID
     - 35001, 35002, 35003, 35004, 35005
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 13
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No
   * - Channel Simulation Frequency
     - 1 GHz (35001)
       3.6 GHz (35002, 35003, 35004, 35005)
   * - Emulation Center Frequency
     - 1 GHz (35001, 35002, 35003)
       3.6 GHz (35004, 35005)

**Channel Characteristics**

The channel characteristics have been computed by following the free-space path loss formula:

.. math::
   FSPL = 20log_{10}\left(\frac{4\pi df}{c}\right)

Where:

- f = center frequency, which is equal to 1 GHz (35001) or 3.6 GHz (35002, 35003, 35004, 35005)
- c = speed of light
- d = 3D distance BS-UE

The link is only defined between BS and UE. The link UE-UE and loopback links (BS-BS and same UE) are not defined and they are set to be empty channels with no transmission. Moreover, to compensate for the Colosseum Base Loss and to make the scenarios falling inside the Colosseum dynamic range, an increase in the path gains has been added equal for all the links: 40 dB (35001, 35003, 35005), and 51 dB (35002, 35004).

**References**

- D. Villa, M. Tehrani-Moayyed, C. Robinson,  L. Bonati, P. Johari, M. Polese, S. Basagni, T. Melodia, "Colosseum as a Digital Twin: Bridging Real-World Experimentation and Wireless Network Emulation," arXiv:2303.17063 [cs.NI], pp. 1-15, March 2023. [`pdf <https://arxiv.org/pdf/2303.17063>`_][`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2024dt.txt>`_]

- D. Villa, M. Tehrani-Moayyed, P. Johari, S. Basagni, T. Melodia, "CaST: A Toolchain for Creating and Characterizing Realistic Wireless Network Emulation Scenarios", Proc. of the 16th ACM Workshop on Wireless Network Testbeds, Experimental evaluation & CHaracterization (WiNTECH 2022), Sydney, Australia, October 2022. [`pdf <https://ece.northeastern.edu/wineslab/papers/villa2022wintech.pdf>`_][`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2022wintech.txt>`_]

Waikiki Beach, Honolulu, HI (45101-45104)
-----------------------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 45101, 45102, 45103, 45104
   * - RF Description
     - 45101 (Honolulu Waikiki Beach Ship - 1 GHz + 70dB)
       45102 (Honolulu Waikiki Beach Ship Static at 20s - 1 GHz + 70dB)
       45103 (Honolulu Waikiki Beach Ship (+ Sensor) - 1 GHz + 70dB)
       45104 (Honolulu Waikiki Beach Ship Static at 20s (+ Sensor) - 1 GHz + 70dB)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - N/A
   * - Traffic Description
     - N/A
   * - Center Frequency
     - 1 GHz
   * - Number of Nodes
     - 8 (45101, 45102), 9 (45103, 45104)
   * - Duration
     - 40 seconds (45101, 45103), 1 second (45102, 45104)

**Narrative**

This set of scenarios replicates an outdoor environment, specifically emulating a portion of Waikiki Beach in Honolulu, HI, USA. The original goal of these scenarios is to simulate the movement of a ship performing radar operations and a cellular network, consisting of 1 Base Station (BS) and 6 User Equipments (UEs). The BS needs to detect the incumbent radar and react accordingly. To detect the incumbent transmissions, it leverages a sensor node located in the same position as the BS.

These scenarios have been created and validated via the CaST toolchain, which combines OpenStreetMap for the STL model generation and Matlab Ray-tracing for channel estimation.

**Node Placement**

The locations of the nodes in Waikiki Beach aim to reflect a generic combination of static BS and UEs, with a mobile ship moving along the beach in a linear trajectory at a constant speed of 10 m/s. The BS location is sourced from the OpenCelliD database of real-world cellular deployments, while the UEs are randomly scattered along the beach.

**Scenario 45101**

Contains 8 nodes with the ship moving along the beach at 10 m/s for 40 seconds.

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/waikiki_45101.png
   :width: 300px
   :alt: Waikiki Beach  45101
   :align: center

.. list-table:: Parameters of the Waikiki Beach scenario.
   :widths: 30 70
   :header-rows: 0

   * - Parameter
     - Value
   * - Antenna height (BS and Ship)
     - 3 meters
   * - Antenna height (UEs)
     - 1 meter
   * - Ship speed
     - 10 m/s
   * - Emulation area
     - 700x800 m²

**Scenario 45102**

Contains the same 8 nodes as 45101, but with the ship static at the position corresponding to t=20 seconds (midpoint of trajectory).

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/waikiki_45102.png
   :width: 300px
   :alt: Waikiki Beach  45102
   :align: center

**Scenario 45103**

Contains 9 nodes (same 8 as 45101 plus a sensor node positioned at the same location as the BS).

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/waikiki_45103.png
   :width: 300px
   :alt: Waikiki Beach  45103
   :align: center

**Scenario 45104**

Contains 9 nodes (same as 45103), but with the ship static at the position corresponding to t=20 seconds.

.. figure:: /_static/images/user_guide/wiki/scenarios/cellular/waikiki_45104.png
   :width: 300px
   :alt: Waikiki Beach  45104
   :align: center

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Modeled Location
     - Waikiki Beach, Honolulu, HI (from OSM)
   * - Scenario Duration
     - Mobile 40 seconds (45101, 45103)
       Static 1 second (45102, 45104)
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 8 (45101, 45102)
       9 (45103, 45104)
   * - Ray-tracing Simulation Frequency
     - 3.6 GHz
   * - Emulation Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 80.0 MHz
   * - Node Mobility
     - Ship-08: Linear 10 m/s
   * - Link Reciprocity
     - None
   * - Self Channel (Gain to Own Antenna)
     - Only reflections considered
   * - Max Number of Reflections
     - 3
   * - Sampling Time
     - 1 second
   * - Building Material
     - Concrete
   * - Transmit power (BS and Ship)
     - 30 dBm
   * - Transmit power (UEs)
     - 20 dBm
   * - Antenna Pattern
     - Omni
   * - Number of Antennas Per Node
     - 2 (identical channel)
   * - Antenna Spacing
     - N/A

**References**

- D. Villa, D. Uvaydov, L. Bonati, P. Johari, J. M. Jornet, and T. Melodia, "Twinning Commercial Radio Waveforms in the Colosseum Wireless Network Emulator," Proc. of the 17th ACM Workshop on Wireless Network Testbeds, Experimental evaluation & CHaracterization (WiNTECH 2023), Madrid, Spain, October 2023. [`pdf <https://ece.northeastern.edu/wineslab/papers/villa2023wintech.pdf>`_] [`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2023wintech.txt>`_]    

- D. Villa, M. Tehrani-Moayyed, P. Johari, S. Basagni, T. Melodia, "CaST: A Toolchain for Creating and Characterizing Realistic Wireless Network Emulation Scenarios", Proc. of the 16th ACM Workshop on Wireless Network Testbeds, Experimental evaluation & CHaracterization (WiNTECH 2022), Sydney, Australia, October 2022. [`pdf <https://ece.northeastern.edu/wineslab/papers/villa2022wintech.pdf>`_][`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2022wintech.txt>`_]

- Unwired Labs. Accessed April 2025. OpenCelliD. https://opencellid.org.
