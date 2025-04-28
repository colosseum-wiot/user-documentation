Arena Digital Twin Scenarios
=========================

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Formal
   * - RF ID
     - 45001, 45002, 45003
   * - RF Description
     - 45001 (Arena static 1 GHz + 40dB)
     - 45002 (Arena static 2.4 GHz + 40dB)
     - 45003 (Arena Mobile 42 nodes 1 GHz + 50dB)
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Center Frequency
     - 1 GHz (45001, 45003), 2.4 GHz (45002)
   * - Number of Nodes
     - 32 (45001, 45002), 42 (45003)
   * - Duration
     - 1 second (45001, 45002), 37 seconds (45003)

**Narrative**

This set of scenarios replicates the Arena testbed, an over-the-air 64-antenna SDR-based ceiling grid testing platform for sub-6 GHz 5G-and-Beyond radio spectrum research, hosted in the indoor laboratory space at Northeastern University. The goal is to create a Digital Twin to be able to run experiments on both a real environment and an emulated one. These scenarios have been created and validated via the CaST toolchain.

**Node Placement**

**Scenarios 45001 and 45002**

The locations of the 32 nodes for scenarios 45001 and 45002 have all nodes at fixed locations following the real positions in a 4x8 grid at 2.84 meters from the ground.

**Scenario 45003**

Scenario 45003 consists of the same 32 nodes of previous scenarios, with the addition of 10 nodes at a height of 1 meter of which:
- 8 nodes (blue squares, 33-40) are at static locations around the environment
- 2 nodes (41-42) are mobile nodes that traverse the lab from one side to the other at a constant speed of 1.2 m/s and take a total of 37 seconds to cover their paths

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Modeled Location
     - Arena indoor environment in Northeastern University lab space
   * - Scenario Duration
     - Static 1 second (45001, 45002)
     - Mobile 37 seconds (45003)
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 32 (45001, 45002)
     - 42 (45003)
   * - Ray-tracing simulation frequency
     - 2.4 GHz
   * - Emulation Center Frequency
     - 1 GHz (45001, 45003)
     - 2.4 GHz (45002)
   * - Max Scenario Bandwidth
     - 80.0 MHz
   * - Node Mobility
     - Linear/Arc following the lab space at 1.2 m/s
   * - Link Reciprocity
     - None
   * - Self Channel (Gain to Own Antenna)
     - Only reflections considered
   * - Antenna Pattern
     - Omni
   * - Number of Antennas Per Node
     - 2 (identical channel)
   * - Antenna Spacing
     - N/A

Alleys of Austin (7013/7014)
---------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Formal
   * - RF ID
     - 7013/7014
   * - RF Description
     - Single tap (7013), 4 taps (7014); large scale
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 70130, 70140, 84010, 84110
   * - Traffic Description
     - VOIP; BFT; Imagery; UAV Video; UAV CC; Body Cam Video
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Incumbent Nodes
     - 0
   * - Number of Competitor Nodes
     - 50

**Narrative**

A platoon from the Texas Army National Guard at Camp Mabry is practicing urban maneuvers and communications in Austin. The platoon is split into five squads consisting of 9 squad members and one UAV. The squads move through the Heritage neighborhood in the following three stages:

Stage 1: 39th street to 41st street. The squads progress from five starting locations and establish basic voice communications.

Stage 2: 41st street to 43th street. The squads begin to also exchange imagery video and imagery.

Stage 3: 43rd street to 45th street. The squads significantly increase their traffic.

The scenario is designed to run for 930 seconds, with 300 seconds per stage for 900 seconds of competitive time and 15 seconds appended on either end. The scenario smoothly transitions between stages.

In this scenario, all offered traffic is part of the stage's mandated outcome. Five teams (50 nodes) are rendered and all five teams are playable in this release.

**Node Placement**

.. list-table::
   :widths: 15 15 15 15 15 15 15
   :header-rows: 1

   * - #
     - Gateway
     - Team 1
     - Team 2
     - Team 3
     - Team 4
     - Team 5
   * - 1
     - Gateway
     - Gateway
     - Gateway
     - Gateway
     - Gateway
   * - 10
     - UAV
     - UAV
     - UAV
     - UAV
     - UAV
   * - 20
     - UAV Control
     - UAV Control
     - UAV Control
     - UAV Control
     - UAV Control
   * - 30
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier
   * - 40
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier
   * - 50
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier
   * - 60
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier
   * - 70
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier
   * - 80
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier
   * - 90
     - Soldier
     - Soldier
     - Soldier
     - Soldier
     - Soldier

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Modeled Location
     - Austin TX
   * - Scenario Duration
     - 930.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 50
   * - Number of Teams
     - 5
   * - Government Controlled Radios
     - 0
   * - Center Frequency
     - 1000.0 MHz
   * - Max Scenario Bandwidth
     - 80.0 MHz
   * - SRN Separation Range
     - 5 m - 200 m
   * - Node Mobility
     - Pedestrian + UAV
   * - Link Reciprocity
     - TRUE
   * - Self Channel (Gain to Own Antenna)
     - 1
   * - Antenna Pattern
     - Omni
   * - Number of Antennas Per Node
     - 2
   * - Antenna Spacing
     - 0.1 m

**Traffic Flow Details**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Scenario Traffic
     - Flow
     - Thput
     - Points
   * - VOIP
     - VOIP
     - 100%
     - 4
   * - BFT
     - Telemetry
     - 100%
     - 1
   * - UAV CC
     - UAV CC
     - NaN
     - 0
   * - Imagery
     - Imagery
     - NaN
     - 2
   * - UAV Video
     - Video
     - 100%
     - 9
   * - Body Cam
     - Video
     - 100%
     - 9

**Thresholds**

Thresholds are applied to each team equally:
- Stage 1: 50%
- Stage 2: 50%
- Stage 3: 50%
