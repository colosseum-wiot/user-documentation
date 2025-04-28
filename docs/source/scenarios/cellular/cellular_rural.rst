Cellular Rural Small Static Scenarios (35001-35005)
===================================================

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
