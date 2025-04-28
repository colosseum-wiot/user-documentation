Qualification Scenarios
====================

SCE Qualification (9988)
---------------------

**Summary**

.. list-table::
   :widths: 30 30 30 30 30
   :header-rows: 1

   * - Stage
     - Duration
     - Link SNR
     - Offered Traffic / Flow
     - Mandated Throughput / Flow
   * - 0
     - 15 sec
     - 20 dB
     - NaN
     - NaN
   * - 1
     - 120 sec
     - 20 dB
     - 1.25 Mbps
     - 1.15 Mbps
   * - 2
     - 120 sec
     - 15 dB
     - 1.25 Mbps
     - 0.8 Mbps
   * - 3
     - 120 sec
     - 10 dB
     - 1.25 Mbps
     - 0.5 Mbps
   * - 4
     - 120 sec
     - 5 dB
     - 1.25 Mbps
     - 0.25 Mbps
   * - 5
     - 120 sec
     - 20 dB
     - 1.25 Mbps
     - 1.15 Mbps
   * - 6
     - 15 sec
     - 20 dB
     - NaN
     - NaN

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Practice
   * - RF ID
     - 9988
   * - RF Description
     - Single tap; large scale
   * - Noise power BW (MHz)
     - 10
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 99880
   * - Traffic Description
     - Streaming UDP
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Incumbent Nodes
     - 0
   * - Number of Competitor Nodes
     - 10

**Narrative**

Scenario 9988 is a test scenario that supports practice for SCE qualification testing and updates the previous version to implement new Mandated Outcome fields required for compliance with Phase 3 scoring criteria.

The scenario contains 10 nodes arrayed on a hypersphere so that every node has the same propagation loss to every other node. Propagation losses are designed so that per link SNR changes in two minute intervals according to the following schedule:

* 0:00->2:15: Per link SNR = 20 dB
* 2:15->4:15: Per link SNR = 15 dB
* 4:15->6:15: Per link SNR = 10 dB
* 6:15->8:15: Per link SNR = 5 dB
* 8:15->10:30: Per link SNR = 20 dB at 1010.0 MHz

Path losses are large scale, single tap only. SNR values assume a 10 MHz RF front end.

A constant 25 Mbps per team is offered per team, which corresponds to 1.25 Mbps per flow with two outbound flows per node (20 flows). This same load is offered for every stage. Traffic starts 15 seconds into the first stage and ends 15 seconds before the end of the scenario.

Mandated outcomes are provided for every stage that correspond to the qualification objectives mapped to a per-flow throughput. Note that this means that in all stages (after an initial 15 seconds for network sync), more traffic is offered than is mandated, with significantly more traffic offered than mandated at the later stages.

Environment Update messages are used to communicated the frequency change in stage 5.

No GPS is provided as a theoretical geometry (hypersphere) is used to create the path losses.

**Node Mapping**

.. list-table::
   :widths: 30 30 30
   :header-rows: 1

   * - Position
     - Label
     - Node #
   * - 1
     - Competitor
     - 1
   * - 2
     - Competitor
     - 2
   * - 3
     - Competitor
     - 3
   * - 4
     - Competitor
     - 4
   * - 5
     - Competitor
     - 5
   * - 6
     - Competitor
     - 6
   * - 7
     - Competitor
     - 7
   * - 8
     - Competitor
     - 8
   * - 9
     - Competitor
     - 9
   * - 10
     - Competitor
     - 10

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 630.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 10
   * - Number of Teams
     - 1
   * - Government Controlled Radios
     - 0
   * - Center Frequency
     - 1000.0 MHz
   * - Max Scenario Bandwidth
     - 80.0 MHz
   * - SRN Separation Range
     - N/A
   * - Node Mobility
     - Fixed
   * - Link Reciprocity
     - True
   * - Self Channel (Gain to Own Antenna)
     - 1
   * - Antenna Pattern
     - Omni
   * - Number of Antennas Per Node
     - 2
   * - Antenna Spacing
     - 0.1 m

**Mandated Outcome Parameters**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Traffic Type
     - TOS
     - Delay (Sec)
     - Throughput (Kbps)
     - Goal Set
   * - Qual_1
     - 0x60
     - 0.37
     - 1000
     - Qual
   * - Qual_2
     - 0x60
     - 0.5
     - 750
     - Qual
   * - Qual_3
     - 0x60
     - 0.75
     - 500
     - Qual
   * - Qual_4
     - 0x60
     - 1
     - 250
     - Qual
   * - Qual_5
     - 0x60
     - 0.37
     - 1000
     - Qual

SCE CIL Qualification - Easy 13db Staring Pathloss (9991)
---------------------------------------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 9991
   * - Release Date
     - 2019-08-01 17:03:56.028221
   * - Center Frequency (MHz)
     - 1000.0
   * - Noise power BW (MHz)
     - 40.0
   * - Usable BW for transmissions (MHz)
     - 80.0
   * - Stages
     - 3
   * - Total Length (sec)
     - 630
   * - Stage Lengths (sec)
     - {'1': 195, '2': 210, '3': 225}
   * - Scoring Stage Lengths (sec)
     - {'1': 180, '2': 210, '3': 210}
   * - Number of Competitor Nodes
     - 50
   * - Number of Incumbents
     - 1
   * - Number of Observers
     - 0
   * - RF Description
     - Single tap; large scale
   * - MCHEM Gains
     - RX: 7db, TX: 20db
   * - Traffic ID
     - 99910
   * - Traffic Types
     - BFT, File, VOIP
   * - Scenario Repeats at End?
     - False

**Narrative**

Scenario 9991 is an easier version of 9990 where the interference thresholds for the incumbent have been reduced to the point where the incumbent should never complain.

It repurposes the 7025 Passive Incumbent scenario for CIL validation purposes by modifying the stage 2 center frequency to stimulate CIL message reporting.

Only a single team position is populated (excluding the Passive Incumbent) in this scenario so taps from 7025 can be reused.

9991 is:

* Large scale
* 50 node
* Small Packet
* Formal

**Node Assignments**

.. list-table::
   :widths: 30 50 20
   :header-rows: 1

   * - 
     - Nodes
     - Gateway
   * - Team #1
     - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
     - 1
   * - Team #2
     - 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
     - 11
   * - Team #3
     - 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
     - 21
   * - Team #4
     - 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
     - 31
   * - Team #5
     - 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
     - 41
   * - Incumbents #1
     - 51
     - 51

**Mandated Flows**

Flow types: BFT, File, VOIP

.. list-table:: Flow Counts by Team By Stage
   :widths: 20 20 20 20
   :header-rows: 1

   * - Team
     - Stage #1
     - Stage #2
     - Stage #3
   * - Team #1
     - 70
     - 70
     - 70
   * - Team #2
     - 70
     - 70
     - 70
   * - Team #3
     - 70
     - 70
     - 70
   * - Team #4
     - 70
     - 70
     - 70
   * - Team #5
     - 70
     - 70
     - 70

.. list-table:: Flow Types by Stage
   :widths: 30 30 30
   :header-rows: 1

   * - Stage #1
     - Stage #2
     - Stage #3
   * - VOIP_1, BFT_1, File_1
     - File_2, VOIP_2, BFT_2
     - File_3, VOIP_3, BFT_3

**Points**

Points are accumulated by measurement period. Flows need to be held for the steady state period of 10 seconds in order to count.

.. list-table:: Points by Flow Type by MP
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Points
   * - BFT
     - 1
   * - File
     - 1
   * - VOIP
     - 1

.. list-table:: Scoring Stage Lengths (sec)
   :widths: 30 30 30
   :header-rows: 1

   * - Stage #1
     - Stage #2
     - Stage #3
   * - 180
     - 210
     - 210

.. list-table:: Max Points per MP by Team By Stage
   :widths: 20 20 20 20
   :header-rows: 1

   * - Team
     - Stage #1
     - Stage #2
     - Stage #3
   * - Team #1
     - 70
     - 70
     - 70
   * - Team #2
     - 70
     - 70
     - 70
   * - Team #3
     - 70
     - 70
     - 70
   * - Team #4
     - 70
     - 70
     - 70
   * - Team #5
     - 70
     - 70
     - 70

.. list-table:: Max Points by Team By Stage (may be more if flows span stages)
   :widths: 20 20 20 20
   :header-rows: 1

   * - Team
     - Stage #1
     - Stage #2
     - Stage #3
   * - Team #1
     - 11900
     - 14000
     - 14000
   * - Team #2
     - 11900
     - 14000
     - 14000
   * - Team #3
     - 11900
     - 14000
     - 14000
   * - Team #4
     - 11900
     - 14000
     - 14000
   * - Team #5
     - 11900
     - 14000
     - 14000

**Thresholds**

Points earned in a measurement period above the threshold score bonus points.

.. list-table::
   :widths: 30 30 30
   :header-rows: 1

   * - Stage #1
     - Stage #2
     - Stage #3
   * - 50
     - 50
     - 50

.. list-table:: Threshold Points per MP by Team By Stage
   :widths: 20 20 20 20
   :header-rows: 1

   * - Team
     - Stage #1
     - Stage #2
     - Stage #3
   * - Team #1
     - 35
     - 35
     - 35
   * - Team #2
     - 35
     - 35
     - 35
   * - Team #3
     - 35
     - 35
     - 35
   * - Team #4
     - 35
     - 35
     - 35
   * - Team #5
     - 35
     - 35
     - 35
