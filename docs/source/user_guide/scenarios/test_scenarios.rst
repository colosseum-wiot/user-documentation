Test Scenarios
=============

This section describes the basic test scenarios available in the Colosseum system. These scenarios are designed with controlled parameters for testing and calibration purposes.

All Paths 0 dB (1009)
--------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Test
   * - RF ID
     - 1009
   * - RF Description
     - Single tap; small scale
   * - Noise power BW (MHz)
     - 5
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 10090
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 10

**Narrative**

Test scenario that yields constant 0 dB path-loss (besides the contributions of the hardware components of Colosseum). Duration is set to 1200 seconds, but it is cyclable and can last as long as needed.

This is a simple 10-node scenario where all paths between all nodes have the same loss for the whole duration of the scenario.

**Notes**

* No GPS is provided by this scenario.
* Power levels assume default radio configurations.

**Scenario Parameters**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Label
     - Value
   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 1200.0 s
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

**Traffic Flow Detail**

Bodycam video traffic for 1190 seconds with 83.66 packets per second and 1400 bytes per packet.

All Paths 0 dB (10009)
---------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Test
   * - RF ID
     - 10009
   * - RF Description
     - Single tap; small scale
   * - Scenario BW (MHz)
     - 10
   * - Traffic ID
     - 100090
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 25

**Narrative**

Test scenario that yields constant 0 dB path-loss. Duration is set to 700 seconds, but it is cyclable and can last as long as needed.

This is a simple 25-node scenario where all paths between all nodes have the same loss for the whole duration of the scenario.

**Notes**

* No GPS is provided by this scenario.
* Power levels assume default radio configurations.

**Scenario Parameters**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Label
     - Value
   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 700.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 25
   * - Number of Teams
     - 1
   * - Government Controlled Radios
     - 0
   * - Center Frequency
     - 1000.0 MHz
   * - Max Scenario Bandwidth
     - 10.0 MHz
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

**Traffic Flow Detail**

Bodycam traffic for 690 seconds with 83.66 packets per second and 1400 bytes per packet.

All Paths 0 dB (10024)
---------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Test
   * - RF ID
     - 10024
   * - RF Description
     - Single tap; small scale
   * - Noise power BW (MHz)
     - 10
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 100240
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 2400.0 MHz
   * - Number of Nodes
     - 10

**Narrative**

Test scenario that yields constant 0 dB path-loss. Duration is set to 1200 seconds, but it is cyclable and can last as long as needed.

This is a simple 10-node scenario where all paths between all nodes have the same loss for the whole duration of the scenario.

**Notes**

* No GPS is provided by this scenario.
* Power levels assume default radio configurations.

**Scenario Parameters**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Label
     - Value
   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 1200.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 10
   * - Number of Teams
     - 1
   * - Government Controlled Radios
     - 0
   * - Center Frequency
     - 2400.0 MHz
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

**Traffic Flow Detail**

Bodycam traffic for 1190 seconds with 83.66 packets per second and 1400 bytes per packet.

Test Scenario -50dbFS (9971)
--------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Test
   * - RF ID
     - 9971
   * - RF Description
     - Single tap; large scale
   * - Noise power BW (MHz)
     - 10
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 99711
   * - Traffic Description
     - None
   * - Center Frequency
     - 1000.0 MHz
   * - Number of User Nodes
     - 5

**Narrative**

Test scenario that yields constant -50 dBFS received power under default configuration. 5 minute duration.

This is a simple 5-node scenario where all paths between all nodes have the same loss for the duration of the scenario.

**Notes**

* No traffic is provided by this scenario.
* No GPS is provided by this scenario.
* Power levels assume default radio configurations.

**Node Placement**

The table below indicates which node id's map to which team position.

.. list-table::
   :widths: 30 30 30
   :header-rows: 1

   * - Position
     - Label
     - Node #
   * - 1
     - Gateway
     - 1
   * - 2
     - Node
     - 2
   * - 3
     - Node
     - 3
   * - 4
     - Node
     - 4
   * - 5
     - Node
     - 5

**Scenario Parameters**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Label
     - Value
   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 300.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
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

**Traffic Flow Detail**

There is no traffic in this test scenario.

**Mandated Outcome Parameters**

There are no mandated outcomes in this test scenario.

Test Scenario -70dbFS (9972)
--------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Test
   * - RF ID
     - 9972
   * - RF Description
     - Single tap; large scale
   * - Noise power BW (MHz)
     - 10
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 99721
   * - Traffic Description
     - None
   * - Center Frequency
     - 1000.0 MHz
   * - Number of User Nodes
     - 5

**Narrative**

Test scenario that yields constant -70 dBFS received power under default configuration. 5 minute duration.

This is a simple 5-node scenario where all paths between all nodes have the same loss for the duration of the scenario.

**Notes**

* No traffic is provided by this scenario.
* No GPS is provided by this scenario.
* Power levels assume default radio configurations.

**Node Placement**

The table below indicates which node id's map to which team position.

.. list-table::
   :widths: 30 30 30
   :header-rows: 1

   * - Position
     - Label
     - Node #
   * - 1
     - Gateway
     - 1
   * - 2
     - Node
     - 2
   * - 3
     - Node
     - 3
   * - 4
     - Node
     - 4
   * - 5
     - Node
     - 5

**Scenario Parameters**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Label
     - Value
   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 300.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
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
     - TRUE
   * - Self Channel (Gain to Own Antenna)
     - 1
   * - Antenna Pattern
     - Omni
   * - Number of Antennas Per Node
     - 2
   * - Antenna Spacing
     - 0.1 m

**Traffic Flow Detail**

There is no traffic in this test scenario.

**Mandated Outcome Parameters**

There are no mandated outcomes in this test scenario.

Test Scenario -90dbFS (9973)
--------------------------

**Overview**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - Version
     - Test
   * - RF ID
     - 9973
   * - RF Description
     - Single tap; large scale
   * - Noise power BW (MHz)
     - 10
   * - Usable BW for transmissions (MHz)
     - 80
   * - Traffic ID
     - 99731
   * - Traffic Description
     - None
   * - Center Frequency
     - 1000.0 MHz
   * - Number of User Nodes
     - 5

**Narrative**

Test scenario that yields constant -90 dBFS received power under default configuration. 5 minute duration.

This is a simple 5-node scenario where all paths between all nodes have the same loss for the duration of the scenario.

**Notes**

* No traffic is provided by this scenario.
* No GPS is provided by this scenario.
* Power levels assume default radio configurations.

**Node Placement**

The table below indicates which node id's map to which team position.

.. list-table:: Node Mapping
   :widths: 30 30 30
   :header-rows: 1

   * - Position
     - Label
     - Node #
   * - 1
     - Gateway
     - 1
   * - 2
     - Node
     - 2
   * - 3
     - Node
     - 3
   * - 4
     - Node
     - 4
   * - 5
     - Node
     - 5

**Scenario Parameters**

.. list-table:: Scenario Parameters
   :widths: 50 50
   :header-rows: 1

   * - Label
     - Value
   * - Modeled Location
     - N/A
   * - Scenario Duration
     - 300.0 s
   * - Scenario Repeats at End?
     - True
   * - Number of Nodes
     - 5
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
     - TRUE
   * - Self Channel (Gain to Own Antenna)
     - 1
   * - Antenna Pattern
     - Omni
   * - Number of Antennas Per Node
     - 2
   * - Antenna Spacing
     - 0.1 m

**Traffic Flow Detail**

There is no traffic in this test scenario.

**Mandated Outcome Parameters**

There are no mandated outcomes in this test scenario.
