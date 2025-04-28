=============================
Integrated Access and Backhaul 
=============================

**Overview**

These RF scenarios emulate wireless environments in densely urban areas around Europe. Specifically, they model environments in Florence, Milan, Barcelona, and Luxembourg. In each scenario, approximately 25 Integrated Access and Backhaul (IAB) nodes are deployed.

Since the current IAB-like implementation requires two different SRNs for each IAB node, the scenario doubles every node by creating two radio nodes in the same location. This approach allows testing of large-scale IAB deployments. However, by ignoring the doubled nodes, the scenarios can also be used to experiment with any kind of mobile network.

**Node Placement**

For the placement of the gNBs, a heuristic developed by Gemmi et al. has been used. The heuristic tries to find the combination of k gNBs location among the perimeter of the buildings that maximizes the Line-of-Sight coverage towards public roads. More details are available in the referenced paper.

**Radio Environment Modeling**

For generating these scenarios, first a visibility graph among all the gNB locations was computed. This allowed discerning Line-of-Sight (LoS) links from Non-Line-of-Sight (NLoS) links. Afterward, the Urban Micro (UMi) channel model documented by ETSI in the technical report TR38.901 was applied.

Since Colosseum has a base pathloss of around 50dB, this value has been subtracted from the calculated pathloss to compensate. More details on this approach are available in the original research: `CaST <https://ece.northeastern.edu/wineslab/papers/villa2022wintech.pdf>`_.

For each scenario, four different variations have been implemented:
* 28GHz with all links
* 28GHz with only LoS links
* 3.6GHz with all links
* 3.6GHz with only LoS links

**Florence, Italy**

.. figure:: /_static/images/iab/iab_map_florence.png
   :width: 300px
   :alt: IAB Florence map
   :align: center

.. table:: Florence Scenario Parameters
   :widths: 30 70
   
   +------------------------+----------------------------------------+
   | **Label**              | **Value**                              |
   +========================+========================================+
   | Area                   | Via di Maragliano, Florence, Italy     |
   +------------------------+----------------------------------------+
   | Coordinates            | 11.232E, 43.786N                       |
   +------------------------+----------------------------------------+
   | RF ID                  | XXXXX (28 GHz)                         |
   |                        |                                        |
   |                        | XXXXX (28 GHz only LoS)                |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz)                        |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz only LoS)               |
   +------------------------+----------------------------------------+
   | Duration               | 1s, cyclable                           |
   +------------------------+----------------------------------------+
   | RF Description         | Single Tap, large scale                |
   +------------------------+----------------------------------------+
   | Center Frequency       | 1GHz                                   |
   +------------------------+----------------------------------------+
   | Number of Nodes        | 40 (20 IAB nodes)                      |
   +------------------------+----------------------------------------+

**Milan, Italy**

.. figure:: /_static/images/iab/iab_map_milan.png
   :width: 300px
   :alt: IAB Milan map
   :align: center

.. table:: Milan Scenario Parameters
   :widths: 30 70
   
   +------------------------+----------------------------------------+
   | **Label**              | **Value**                              |
   +========================+========================================+
   | Area                   | Milan, Italy                           |
   +------------------------+----------------------------------------+
   | Coordinates            | 9.203E, 45.464N                        |
   +------------------------+----------------------------------------+
   | RF ID                  | XXXXX (28 GHz)                         |
   |                        |                                        |
   |                        | XXXXX (28 GHz only LoS)                |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz)                        |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz only LoS)               |
   +------------------------+----------------------------------------+
   | Duration               | 1s, cyclable                           |
   +------------------------+----------------------------------------+
   | RF Description         | Single Tap, large scale                |
   +------------------------+----------------------------------------+
   | Center Frequency       | 1GHz                                   |
   +------------------------+----------------------------------------+
   | Number of Nodes        | 52 (26 IAB nodes)                      |
   +------------------------+----------------------------------------+

**Barcelona, Spain**

.. figure:: /_static/images/iab/iab_map_barcelona.png
   :width: 300px
   :alt: IAB Barcelona map
   :align: center

.. table:: Barcelona Scenario Parameters
   :widths: 30 70
   
   +------------------------+----------------------------------------+
   | **Label**              | **Value**                              |
   +========================+========================================+
   | Area                   | Plaza de Catalunya, Barcelona, Spain   |
   +------------------------+----------------------------------------+
   | Coordinates            | 2.168E, 41.389N                        |
   +------------------------+----------------------------------------+
   | RF ID                  | XXXXX (28 GHz)                         |
   |                        |                                        |
   |                        | XXXXX (28 GHz only LoS)                |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz)                        |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz only LoS)               |
   +------------------------+----------------------------------------+
   | Duration               | 1s, cyclable                           |
   +------------------------+----------------------------------------+
   | RF Description         | Single Tap, large scale                |
   +------------------------+----------------------------------------+
   | Center Frequency       | 1GHz                                   |
   +------------------------+----------------------------------------+
   | Number of Nodes        | 46 (23 IAB nodes)                      |
   +------------------------+----------------------------------------+

**Luxembourg**

.. figure:: /_static/images/iab/iab_map_luxembourg.png
   :width: 300px
   :alt: IAB Luxembourg map
   :align: center

.. table:: Luxembourg Scenario Parameters
   :widths: 30 70
   
   +------------------------+----------------------------------------+
   | **Label**              | **Value**                              |
   +========================+========================================+
   | Area                   | Parc de Merl, Luxembourg               |
   +------------------------+----------------------------------------+
   | Coordinates            | 6.115E, 49.60N                         |
   +------------------------+----------------------------------------+
   | RF ID                  | XXXXX (28 GHz)                         |
   |                        |                                        |
   |                        | XXXXX (28 GHz only LoS)                |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz)                        |
   |                        |                                        |
   |                        | XXXXX (3.6 GHz only LoS)               |
   +------------------------+----------------------------------------+
   | Duration               | 1s, cyclable                           |
   +------------------------+----------------------------------------+
   | RF Description         | Single Tap, large scale                |
   +------------------------+----------------------------------------+
   | Center Frequency       | 1GHz                                   |
   +------------------------+----------------------------------------+
   | Number of Nodes        | 70 (35 IAB nodes)                      |
   +------------------------+----------------------------------------+

**Usage Guidelines**

When using these IAB scenarios, consider the following:

1. For IAB experiments, you'll need to use two SRNs for each IAB node
2. For non-IAB experiments, you can use any subset of the nodes
3. Different frequency variants (28GHz vs 3.6GHz) have different propagation characteristics
4. LoS-only variants provide clearer signal paths but less realistic urban conditions
