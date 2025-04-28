Channel Sounding Scenarios
=======================

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Formal
   * - RF ID
     - 90000, 90001, 90002, 90003, 90004, 90005, 90006, 90007, 90008, 90009
   * - RF Description
     - 90000 (Single tap 0dB 32 nodes)
     - 90001 (Test 1)
     - 90002 (Test 2)
     - 90003 (Test 3)
     - 90004 (Increasing losses - 1GHz)
     - 90005 (Increasing losses - 2GHz)
     - 90006 (Increasing losses - 3GHz)
     - 90007 (Increasing losses - 4GHz)
     - 90008 (Increasing losses - 5GHz)
     - 90009 (Increasing losses - 6GHz)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
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

**Scenario 90000**

**Parameters**

.. list-table::
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

.. list-table::
   :widths: 30 30 30
   :header-rows: 1

   * - Link
     - # Taps
     - Taps Delay [ns]
     - Taps IQ
   * - All links
     - 1
     - 10
     - 1 (0dB)

Scenario 90000 is an extension of scenario 1009. All 32 nodes have a single tap channel with a nominal loss of 0dB, i.e. a tap iq equal to 1, and a tap delay of 10 ns.

**Scenario 90001**

**Parameters**

.. list-table::
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

**Channel Characteristics**

.. list-table::
   :widths: 30 30 30 30
   :header-rows: 1

   * - Link
     - # Taps
     - Taps Delay [ns]
     - Taps IQ
   * - 1→2
     - 2
     - [0, 256]
     - [1, 1]
   * - 1→3
     - 2
     - [0, 256]
     - [1, 1j]
   * - 1→4
     - 2
     - [0, 256]
     - [1, -1]
   * - 1→5
     - 2
     - [0, 256]
     - [1, 0.01]
   * - 2→3
     - 2
     - [0, 500]
     - [1, 1]
   * - 2→4
     - 2
     - [0, 500]
     - [1, 1j]
   * - 2→5
     - 2
     - [0, 500]
     - [1, -1]
   * - 3→4
     - 2
     - [0, 1]
     - [1, 1]
   * - 3→5
     - 2
     - [0, 1]
     - [1, -1]
   * - 4→5
     - 4
     - [0, 128, 200, 400]
     - [0.5+0.5j, 0.1, -0.01+0.1j, -0.5j]

Each node channel link has its own set of values of: number of taps, delays, and IQ. The loopback links, i.e. 1→1, 2→2..., do not have any channel defined.

**Scenarios 90004-90009**

**Parameters (for 90004)**

.. list-table::
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

**Channel Characteristics**

.. list-table::
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

The loopback links, i.e. 1→1, 2→2..., do not have any channel defined. All scenarios from 90004 through 90009 are the same, the only difference is the center frequency of operation, which ranges from 1 GHz to 6 GHz.
