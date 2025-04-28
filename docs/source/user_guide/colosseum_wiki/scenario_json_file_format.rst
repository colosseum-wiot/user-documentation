Scenario JSON File Format
=======================

RF Scenario Radio Map JSON File
------------------------------

JSON file format is used for configuring the radio mapping for a RF scenario request. Each user has the option to let Colosseum automatically configure the radio mapping during a RF scenario request. In the event a user wants to self configure the radio mapping, see below for an example of the JSON structure: test.json

.. code-block:: json

    {
      "Node 1":{"SRN":1,"RadioA":1,"RadioB":2},
      "Node 2":{"SRN":12,"RadioA":1,"RadioB":2},
      "Node 3":{"SRN":123,"RadioA":1,"RadioB":2},
      "Node 4":{"SRN":23,"RadioA":1,"RadioB":2},
      "Node 5":"None"
    }

To use this JSON file in the RF scenario request see the colosseum cli command below:

.. code-block:: bash

    $ colosseumcli rf start 1 -m test.json

``--radio-map`` and the name of the json must be added 

JSON Examples and Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The JSON format allows SRN and M-CHEM daughtercards to be arbitrarily mapped within a reservation. The utility of this feature will depend on the RF scenario being used, and if important, will be indicated in the documentation for that scenario.

Below are some descriptions of the entries in the above example:

- ``"Node 1":{"SRN":1,"RadioA":1,"RadioB":2}`` denotes a conventional mapping of SRN-001 USRP daughtercard A to M-CHEM daughtercard 1 and SRN-001 USRP daughtercard B to M-CHEM daughtercard 2. **Note: Batch mode applies this daughtercard mapping to all RF nodes within a batch reservation.**
- ``"Node 2":{"SRN":12,"RadioA":2,"RadioB":1}`` denotes a mapping of SRN-012 USRP daughtercard A to M-CHEM daughtercard 2 and SRN-012 USRP daughtercard B to M-CHEM daughtercard 1, which is the opposite mapping of the previous example
- ``"Node 4":{"SRN":23,"RadioA":0,"RadioB":1}`` indicates that SRN-023 USRP daughtercard A is disconnected and SRN-023 daughtercard B will be mapped to M-CHEM daughtercard 1
- ``"Node 5":"None"`` will disregard the node completely and will not be mapped to an SRN.

.. note::
    If a scenario has 10 Nodes, the user MUST include ALL 10 nodes in the JSON format. Colosseum will not automatically configure remaining nodes left out of the JSON file.

Traffic Scenario Node Map JSON File
---------------------------------

JSON file format is used for configuring the node mapping for a traffic scenario request. Each user has the option to let Colosseum automatically configure the node mapping during a traffic scenario request. In the event a user wants to self configure the node mapping, see below for an example of the JSON structure: tg_test.json

.. code-block:: json

    {
      "1":1,
      "2":45,
      "4":23
    }

The key (first column) of the JSON file is the node id in the scenario. The value (second column) of the JSON file is the SRN id. Omitted nodes will not be used in the scenario.

In the above example traffic scenario node 1 will run on SRN 1, traffic scenario node 2 will run on SRN 45, traffic scenario node 4 will run on SRN 23, and traffic scenario node 3 will be omitted.

To use this JSON file in the scenario request see the colosseum cli command below:

.. code-block:: bash

    $ colosseumcli tg start 1 -m tg_test.json
