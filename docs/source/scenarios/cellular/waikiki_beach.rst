Waikiki Beach, Honolulu, HI (45101-45104)
=========================================

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

.. figure:: /_static/resources/scenarios/cellular/waikiki_45101.png
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

.. figure:: /_static/resources/scenarios/cellular/waikiki_45102.png
   :width: 300px
   :alt: Waikiki Beach  45102
   :align: center

**Scenario 45103**

Contains 9 nodes (same 8 as 45101 plus a sensor node positioned at the same location as the BS).

.. figure:: /_static/resources/scenarios/cellular/waikiki_45103.png
   :width: 300px
   :alt: Waikiki Beach  45103
   :align: center

**Scenario 45104**

Contains 9 nodes (same as 45103), but with the ship static at the position corresponding to t=20 seconds.

.. figure:: /_static/resources/scenarios/cellular/waikiki_45104.png
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

**Acknowledgments**

Partially supported by Keysight Technologies and by the U.S. National Science Foundation under grants CNS-1925601 and CNS-2112471.
