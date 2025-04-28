Fixed Pathloss Scenarios
=====================

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Formal
   * - RF ID
     - 51005, 51010, 51015, 51020, 51025, 51030
   * - RF Description
     - 51005 (All Paths 5dB)
     - 51010 (All Paths 10dB)
     - 51015 (All Paths 15dB)
     - 51020 (All Paths 20dB)
     - 51025 (All Paths 25dB)
     - 51030 (All Paths 30dB)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Center Frequency
     - 1 GHz
   * - Number of Nodes
     - 20
   * - Duration
     - 1 second

**Narrative**

This set of scenarios derives from the base test scenario 1009 (All Paths 0 dB) with the main difference of not having a 0 dB pathloss, but instead a fixed synthetic loss for all links which changes based on the RF ID. The goal is to have a group of scenarios with all same channel characteristics and different from 0 dB for testing and experiment purposes.

**Node Placement**

The locations of the nodes are not applicable in this set of scenarios. The channel characteristics have been created in a synthetic way. All the nodes are static, and the channel does not change during the whole scenario duration.

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Title
     - All Paths [5, 10, 15, 20, 25, 30]dB
   * - Scenario ID
     - 51005, 51010, 51015, 51020, 51025, 51030
   * - Scenario Duration
     - 1 second
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 20
   * - Center Frequency
     - 1 GHz
   * - Max Scenario Bandwidth
     - 80 MHz
   * - Node Mobility
     - No

**Channel Characteristics**

.. list-table::
   :widths: 25 25 25 25 25
   :header-rows: 1

   * - Scenario ID
     - Frequency
     - Link
     - # Taps
     - Taps Delay [ns]
     - Taps Gain [dB]
   * - 51005
     - 1 GHz
     - All links
     - 1
     - 0
     - -5
   * - 51010
     - 1 GHz
     - All links
     - 1
     - 0
     - -10
   * - 51015
     - 1 GHz
     - All links
     - 1
     - 0
     - -15
   * - 51020
     - 1 GHz
     - All links
     - 1
     - 0
     - -20
   * - 51025
     - 1 GHz
     - All links
     - 1
     - 0
     - -25
   * - 51030
     - 1 GHz
     - All links
     - 1
     - 0
     - -30

All scenarios have the same channel characteristics, i.e. single-tap with a tap delay of 0 ns for all links (also loopback 11, 22...) at 1 GHz center frequency, and differ just for the tap gain, which varies from 5 to 30 dB with 5 dB steps.

**Base 0dB Scenarios at Various Frequencies (52000-52100)**

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Formal
   * - RF ID
     - 52001, 52002, 52003, 52004, 52005, 52006
   * - RF Description
     - 52001 (All Paths 0dB - 832 MHz)
     - 52002 (All Paths 0dB - 2.4 GHz)
     - 52003 (All Paths 0dB - 2.54 GHz)
     - 52004 (All Paths 0dB - 3.6 GHz)
     - 52005 (All Paths 0dB - 5.5 GHz)
     - 52006 (All Paths 0dB - 5.9 GHz)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Center Frequency
     - Various
   * - Number of Nodes
     - 20
   * - Duration
     - 1 second

**Narrative**

This set of scenarios derives from the base test scenario 1009 with the main difference of a center frequency that changes based on the RF ID. The goal is to have a group of scenarios with all same channel characteristics, i.e. 0 dB pathloss, and different center frequencies for testing and experiment purposes.

**Node Placement**

The locations of the nodes are not applicable in this set of scenarios. The channel characteristics have been created in a synthetic way. All the nodes are static, and the channel does not change during the whole scenario duration.

**Channel Characteristics**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Scenario ID
     - Frequency
     - Link
     - # Taps
     - Taps Delay [ns]
     - Taps Gain [dB]
   * - 52001
     - 832 MHz
     - All links
     - 1
     - 10
     - 0
   * - 52002
     - 2.4 GHz
     - All links
     - 1
     - 10
     - 0
   * - 52003
     - 2.54 GHz
     - All links
     - 1
     - 10
     - 0
   * - 52004
     - 3.6 GHz
     - All links
     - 1
     - 10
     - 0
   * - 52005
     - 5.5 GHz
     - All links
     - 1
     - 10
     - 0
   * - 52006
     - 5.9 GHz
     - All links
     - 1
     - 10
     - 0

All scenarios have the same channel characteristics, i.e. single-tap with a tap delay of 10 ns for all links (also loopback 11, 22...) and 0 dB pathloss, and differ just for the center frequency of operation, which varies from 832 MHz to 5.9 GHz.
