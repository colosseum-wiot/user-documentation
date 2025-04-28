Channel Sounding Scenarios
=======================

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Label
     - Value
   * - Version
     - Formal
   * - RF ID
     - 90000, 90001, 90002, 90003, 90004, 90005, 90006, 90007, 90008, 90009
   * - RF Description
     - 90000 (Single tap 0dB 32 nodes),
       90001 (Test 1), 90002 (Test 2), 90003 (Test 3),
       90004 (Increasing losses - 1GHz), 90005 (Increasing losses - 2GHz),
       90006 (Increasing losses - 3GHz), 90007 (Increasing losses - 4GHz),
       90008 (Increasing losses - 5GHz), 90009 (Increasing losses - 6GHz)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - N/A
   * - Traffic Description
     - N/A
   * - Center Frequency
     - Various (1-6 GHz)
   * - Number of Nodes
     - 32 for 90000 and 5 for others
   * - Duration
     - 1 second

**Narrative**

This set of scenarios has been intended to study the behavior of the channel emulation that is happening in the Colosseum system and performed by the Massive CHannel EMulator (MCHEM) through channel sounding. The main tool used to achieve these goals is CaST (Channel emulation scenario generator and Sounder Toolchain), which is a toolchain for creating and characterizing realistic wireless network emulation scenarios.

Each of these scenarios has been developed with different channel characteristics to study how the emulation performs in various conditions, i.e. by varying the tap delay, the tap gain, the number of taps, and/or the center frequency of operation. Based on the scenario, all nodes are affected by the same channel conditions (i.e., 90000, 90004, 90005, 90006, 90007, 90008, 90009), or each pair of the node shows a different one (i.e., 90001, 90002, 90003). In the former, the purpose is to see how a particular condition affects different nodes and to analyze the various discrepancies. In the latter, the goal is to study how very different and particular channel conditions are addressed by MCHEM.

**Node Placement**

The locations of the nodes are not applicable in this set of scenarios. The channel characteristics have been created in a synthetic way, with the sole purpose of studying the Colosseum emulation behavior. All the nodes are static, and the channel does not change during the whole scenario duration.

Scenario 90000
--------------

.. list-table:: Parameters
   :widths: 30 70
   :header-rows: 0

   * - Title
     - Single tap 0dB 32 nodes
   * - Scenario ID
     - 90000
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 32
   * - Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 5 MHz
   * - Node Mobility
     - No

**Channel Characteristics**

Scenario 90000 is an extension of scenario 1009. All 32 nodes have a single tap channel with a nominal loss of 0 dB, i.e. a tap iq equal to 1, and a tap delay of 10 ns.

Scenario 90001
--------------

.. list-table:: Parameters
   :widths: 30 70
   :header-rows: 0

   * - Title
     - Channel Sounding Test 1
   * - Scenario ID
     - 90001
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 5 MHz
   * - Node Mobility
     - No

.. list-table:: Channel Characteristics
   :widths: 30 30 30 30
   :header-rows: 1

   * - Link
     - # Taps
     - Taps Delay [ns]
     - Taps IQ
   * - 1↔2
     - 2
     - [0, 256]
     - [1, 1]
   * - 1↔3
     - 2
     - [0, 256]
     - [1, 1j]
   * - 1↔4
     - 2
     - [0, 256]
     - [1, -1]
   * - 1↔5
     - 2
     - [0, 256]
     - [1, 0.01]
   * - 2↔3
     - 2
     - [0, 500]
     - [1, 1]
   * - 2↔4
     - 2
     - [0, 500]
     - [1, 1j]
   * - 2↔5
     - 2
     - [0, 500]
     - [1, -1]
   * - 3↔4
     - 2
     - [0, 1]
     - [1, 1]
   * - 3↔5
     - 2
     - [0, 1]
     - [1, -1]
   * - 4↔5
     - 4
     - [0, 128, 200, 400]
     - [0.5+0.5j, 0.1, -0.01+0.1j, -0.5j]

Each node channel link has its own set of values of: number of taps, delays, and IQ. The loopback links, i.e. 1↔1, 2↔2, ..., do not have any channel defined.

Scenario 90002
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding Test 2
   * - Scenario ID
     - 90002
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

.. list-table:: Channel Characteristics
   :widths: 15 15 35 35
   :header-rows: 1

   * - Link
     - # Taps
     - Taps Delay [ns]
     - Taps IQ
   * - 1 ↔ 2
     - 2
     - [0, 128]
     - [1, 1]
   * - 1 ↔ 3
     - 3
     - [0, 128, 256]
     - [1, 1, 1]
   * - 1 ↔ 4
     - 2
     - [0, 128]
     - [1, 0.5]
   * - 1 ↔ 5
     - 2
     - [0, 128]
     - [1, -0.5]
   * - 2 ↔ 3
     - 4
     - [0, 100, 200, 300]
     - [1, 1, 1, 1]
   * - 2 ↔ 4
     - 2
     - [0, 256]
     - [1, 1+1j]
   * - 2 ↔ 5
     - 2
     - [0, 150]
     - [1, 0.4+0.4j]
   * - 3 ↔ 4
     - 3
     - [0, 150, 300]
     - [0.8+0.5j, 0.4+0.2j, 0.3-0.1j]
   * - 3 ↔ 5
     - 2
     - [150, 300]
     - [1, 0.5]
   * - 4 ↔ 5
     - 4
     - [0, 128, 256, 512]
     - [1, 0.8, 0.6, 0.4]

Each node channel link has its own set of values of: number of taps, delays, and IQ. The loopback links, i.e. 1↔1, 2↔2, ..., do not have any channel defined.

Scenario 90003
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding Test 3
   * - Scenario ID
     - 90003
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

.. list-table:: Channel Characteristics
   :widths: 10 10 30 50
   :header-rows: 1

   * - Link
     - # Taps
     - Taps Delay [ns]
     - Taps IQ
   * - 1 ↔ 2
     - 3
     - [0, 185, 426]
     - [1, 1, 1]
   * - 1 ↔ 3
     - 4
     - [0, 211, 582, 900]
     - [1, 0.4, 0.7, 0.9]
   * - 1 ↔ 4
     - 4
     - [0, 128, 200, 400]
     - [0.7079, 0.1, 0.1778, 0.3981]
   * - 1 ↔ 5
     - 4
     - [0, 128, 200, 400]
     - [0.6645, 0.0891, 0.0178, 0.1778]
   * - 2 ↔ 3
     - 4
     - [120, 540, 570, 880]
     - | [-2.644206750692318e-04 - 1.412260154503784e-04i, 
       | -4.268363147882066e-05 - 3.938027770581668e-05i, 
       | 5.442117323698082e-06 + 2.082972343014769e-04i, 
       | 7.924659274078076e-06 - 3.426350880829577e-06i]
   * - 2 ↔ 4
     - 4
     - [80, 140, 200, 260]
     - | [-0.000425856538648683 - 0.000233637915879671i, 
       | -4.15329049906667e-06 + 0.000214255242998177i, 
       | -3.55942480332183e-05 - 4.66396609971528e-05i, 
       | 1.72968112739254e-06 - 1.18230107301641e-05i]
   * - 2 ↔ 5
     - 4
     - [0, 128, 200, 400]
     - [0.6645, 0.1585, 0.0178, 0.0891]
   * - 3 ↔ 4
     - 4
     - [0, 128, 200, 350]
     - [0.6645, 0.1585, 0.3548, 0.0398]
   * - 3 ↔ 5
     - 4
     - [0, 110, 240, 300]
     - [1, 0.8, 0.6, 0.5]
   * - 4 ↔ 5
     - 4
     - [0, 128, 200, 400]
     - [0.6645, 0.1585, 0.3548, 0.0282]

Scenario 90004
--------------

.. list-table:: Parameters
   :widths: 30 70
   :header-rows: 0

   * - Title
     - Channel Sounding - Increasing losses - 1GHz
   * - Scenario ID
     - 90004
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

.. list-table:: Channel Characteristics
   :widths: 30 30 30 30
   :header-rows: 1

   * - Link
     - # Taps
     - Taps Delay [ns]
     - Taps Gain [dB]
   * - 1→2
     - 1
     - [0]
     - [0]
   * - 1→3
     - 1
     - [0]
     - [-5]
   * - 1→4
     - 1
     - [0]
     - [-10]
   * - 1→5
     - 1
     - [0]
     - [-15]
   * - 2→3
     - 1
     - [0]
     - [-20]
   * - 2→4
     - 1
     - [0]
     - [-25]
   * - 2→5
     - 1
     - [0]
     - [-30]
   * - 3→4
     - 1
     - [0]
     - [-35]
   * - 3→5
     - 1
     - [0]
     - [-40]
   * - 4→5
     - 1
     - [0]
     - [-45]

The loopback links, i.e. 1↔1, 2↔2, ..., do not have any channel defined.

.. note::
  All scenarios from 90004 through 90009 are the same, the only difference is the center frequency of operation, which ranges from 1 GHz to 6 GHz.

Scenario 90005
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding - Increasing losses - 2 GHz
   * - Scenario ID
     - 90005
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 2 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

The channel characteristics are equal to scenario 90004. The only difference here is the center frequency of operation, which is set to 2 GHz.

Scenario 90006
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding - Increasing losses - 3 GHz
   * - Scenario ID
     - 90006
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 3 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

The channel characteristics are equal to scenario 90004. The only difference here is the center frequency of operation, which is set to 3 GHz.

Scenario 90007
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding - Increasing losses - 4 GHz
   * - Scenario ID
     - 90007
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 4 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

The channel characteristics are equal to scenario 90004. The only difference here is the center frequency of operation, which is set to 4 GHz.

Scenario 90008
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding - Increasing losses - 5 GHz
   * - Scenario ID
     - 90008
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 5 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

The channel characteristics are equal to scenario 90004. The only difference here is the center frequency of operation, which is set to 5 GHz.

Scenario 90009
--------------

.. list-table:: Parameters
   :widths: 40 60
   :header-rows: 1

   * - Label
     - Value
   * - Title
     - Channel Sounding - Increasing losses - 6 GHz
   * - Scenario ID
     - 90009
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
   * - Center Frequency
     - 6 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

The channel characteristics are equal to scenario 90004. The only difference here is the center frequency of operation, which is set to 6 GHz.

**References**

- D. Villa, M. Tehrani-Moayyed, P. Johari, S. Basagni, T. Melodia, "CaST: A Toolchain for Creating and Characterizing Realistic Wireless Network Emulation Scenarios", Proc. of the 16th ACM Workshop on Wireless Network Testbeds, Experimental evaluation & CHaracterization (WiNTECH 2022), Sydney, Australia, October 2022. [`pdf <https://ece.northeastern.edu/wineslab/papers/villa2022wintech.pdf>`_][`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2022wintech.txt>`_]

- L. Bonati, P. Johari, M. Polese, S. D'Oro, S. Mohanti, M. Tehrani-Moayyed, D. Villa, S. Shrivastava, C. Tassie, K. Yoder, A. Bagga, P. Patel, V. Petkov, M. Seltser, F. Restuccia, A. Gosain, K.R. Chowdhury, S. Basagni, T. Melodia, "Colosseum: Large-Scale Wireless Experimentation Through Hardware-in-the-Loop Network Emulation," Proc. of IEEE Intl. Symp. on Dynamic Spectrum Access Networks (DySPAN), Virtual Conference, December 2021. [`pdf <https://ece.northeastern.edu/wineslab/papers/bonati2021colosseum.pdf>`_] [`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/bonati2021colosseum.txt>`_]

