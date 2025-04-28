Anechoic Chamber Scenarios (12350 - 12356) 
==========================================

**Overview**

.. list-table:: Overview
   :widths: 30 70
   :header-rows: 1

   * - Label
     - Value
   * - Version
     - Formal
   * - RF ID
     - 12350, 12351, 12352, 12353, 12354, 12356
   * - RF Description
     - **12350** (original, single tap channel with 20dB boost + gain, 12 nodes);
       **12351** (12350 + 20dB);
       **12352** (12350 +40dB);
       **12353** (12350 +60dB);
       **12354** (12351, changing single tap channel to 3-tap fading channel);
       **12356** (12352, with 3 more nodes);
   * - Noise power BW (MHz)
     - 20
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - N/A
   * - Traffic Description
     - N/A
   * - Center Frequency
     - 1.0 GHz
   * - Number of Nodes
     - 12 (15 for 12356)
   * - Duration
     - Node 10 ~ 12 moving repeatedly every 240 seconds

**Narrative**

RF scenario 12350 emulates a wireless environment where nodes 1 ~ 9 are in a fixed 3-by-3 grid mounted on the ceiling, while nodes 10 ~ 12 serve as flying UAVs moving in a circular trajectory repeatedly every 240 seconds.

- For scenarios 12351/12352/12353, the only difference to 12350 is the increased channel gain by 20/40/60 dB.
- For scenario 12353, the only difference to 12350 is the channel changed from single-tap channel to 3-tap fading channel.
- Scenario 12356 has 15 nodes where the first 12 nodes are the same as all other scenarios while the last 3 nodes serve as fixed UEs. The channel condition of 12356 is the same as 12352.

**Node Placement Scenarios 12350-12354**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Node ID #
     - Node Name
   * - 1
     - UAV-1
   * - 2
     - UAV-2
   * - 3
     - UAV-3
   * - 4
     - BS-1
   * - 5
     - BS-2
   * - 6
     - BS-3
   * - 7
     - BS-4
   * - 8
     - BS-5
   * - 9
     - BS-6
   * - 10
     - BS-7
   * - 11
     - BS-8
   * - 12
     - BS-9

**Node Placement Scenario 12356**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Node ID #
     - Node Name
   * - 1
     - BS-1
   * - 2
     - BS-2
   * - 3
     - BS-3
   * - 4
     - BS-4
   * - 5
     - BS-5
   * - 6
     - BS-6
   * - 7
     - BS-7
   * - 8
     - BS-8
   * - 9
     - BS-9
   * - 10
     - UAV-1
   * - 11
     - UAV-2
   * - 12
     - UAV-3
   * - 13
     - UE-1
   * - 14
     - UE-2
   * - 15
     - UE-3

**Nodes Position and Trajectory**

The figure below shows the anechoic chamber environment together with the positions and labels of the 9 base stations and UAV-1. The trajectory of UAV-1 is also shown. UAV-1 performs an 8-shape around the two racks with goods, and it comes back to its original position.

.. figure:: /_static/images/user_guide/wiki/scenarios/anechoic_chamber/anechoic_1.png
   :width: 300px
   :alt: Anechoic Chamber Node Placement
   :align: center

The figure below shows the anechoic chamber environment together with the positions and labels of UAV-2 and UAV-3 for all scenarios, and of the three UEs of scenario 12356. The trajectories for the UAVs are also shown. UAV-2 performs a circle on the left rack, while UAV-3 makes the circle on the rack on the right. The speed of the three UAVs is the same, meaning that UAV-2 and UAV-3 perform twice their trajectories while UAV-1 makes it once.

.. figure:: /_static/images/user_guide/wiki/scenarios/anechoic_chamber/anechoic_2.png
   :width: 300px
   :alt: Anechoic Chamber Node Placement
   :align: center
