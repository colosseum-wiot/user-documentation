=============
RF Scenarios
=============

Colosseum offers a variety of RF scenarios for different research purposes. These scenarios emulate various real-world environments and wireless conditions to enable repeatable and controlled experiments.

Overview
--------

Colosseum's scenarios are characterized by:

* **RF ID**: Unique identifier for each scenario
* **RF Description**: Brief description of the scenario
* **Duration**: Length of the scenario in seconds
* **Noise Power BW**: Bandwidth over which noise power is calculated
* **Usable BW**: Bandwidth available for transmissions
* **Traffic ID**: Associated traffic scenario ID (if applicable)
* **Center Frequency**: Default center frequency for the scenario
* **Number of Nodes**: Maximum number of nodes supported in the scenario

Scenario Categories
------------------

1. **LTE and Wi-Fi Coexistence** - Scenarios for studying interference between LTE and Wi-Fi networks
2. **Integrated Access and Backhaul (IAB)** - Scenarios for testing large-scale IAB deployments in urban environments
3. **Base Tests** - Simple scenarios with fixed pathloss, useful for basic testing
4. **Cellular Scenarios** - Various cellular network scenarios in different locations
5. **Urban Environments** - Scenarios modeling different urban areas (Rome, Boston, etc.)
6. **Specialized Scenarios** - Anechoic chamber, LoRa, channel sounding, etc.

Choosing a Scenario
------------------

When selecting a scenario for your experiment, consider:

* The number of nodes required
* The wireless technology being tested
* The environmental characteristics needed (urban, rural, etc.)
* The desired signal propagation conditions (multipath, fading, etc.)
* The mobility patterns of nodes (static, mobile, specific routes)

For assistance with scenario selection or to request custom scenarios, please contact the Colosseum support team.

Selected Scenarios
------------------

.. toctree::
   :maxdepth: 2
   :caption: Available Scenarios:

   lte_wifi
   iab
   other
