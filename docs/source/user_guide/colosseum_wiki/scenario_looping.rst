Scenario Looping
===============

**Created:** 2020-03-31T14:59:39-04:00  
**Updated:** 2020-03-31T14:59:39-04:00  

**Tags:** FD_V2_537243 Import

Content
-------

Overview
-------

Scenario looping is a special operation of batch mode that allows users to execute RF for the same scenario multiple times.  

The looping number is configurable and there are not currently any limitations to the number of loops. However, if more loops are selected than the reservation allows, the reservation will terminate before the loops are complete. Please ensure enough time is allocated in your reservation to account for loop execution. 

Note that the /logs directory within an SRN is used for the entire duration of the reservation and is **NOT** copied per loop. When writing files to /logs/, users should ensure their files do not accidentally get overwritten between each scenario iteration.

Radio API in Scenario Looping
----------------------------

RadioAPI functionality has not changed with scenario looping but please note the following:

- **Each loop has an associated start.sh and stop.sh call**.
- **The status.sh RadioAPI script must return "READY" status for each loop iteration**. 
- For more details on Radio API please refer to: https://colosseumneu.freshdesk.com/support/solutions/articles/61000253495-radio-command-and-control-c2-api

Scenario Looping Batch File Specification
---------------------------------------

Scenario looping is specified using batch file definitions. One new parameter is used to specify scenario looping in a batch file: "Loopinfo." The definition is provided in the table below:

+------------+-------------+------------+--------------------------------------------------+
| Key        | Type        | Mandatory  | Description                                      |
+============+=============+============+==================================================+
| Loopinfo   | Array       | Yes        | Identifies the special operation                 |
|            |             |            | See format below.                                |
+------------+-------------+------------+--------------------------------------------------+
| Enabled    | Boolean     | Yes        | True/False - if set to true this will enable     |
|            |             |            | scenario looping.                                |
|            |             |            | See format below.                                |
+------------+-------------+------------+--------------------------------------------------+
| NumOfLoops | Integer     | Yes        | Indicates the number of times that the user      |
|            |             |            | wants to loop the scenario                       |
|            |             |            | See format below.                                |
+------------+-------------+------------+--------------------------------------------------+

This example batch file demonstrates the usage of the "Loopinfo" parameter: 

.. code-block:: json

    {
     "BatchName": "Two Node Example",                                                                                                                                    
        "Duration": 600,
        "Loopinfo": {
            "Enabled": "True",
            "NumOfLoops": 2
        },
        "NodeData": [
            {
                "ImageName": "my-image",
                "ModemConfig": "my-config.conf",
                "RFNode_ID": 1,
                "TrafficNode_ID": 1,
                "isGateway": true,
                "node_type": "competitor"
            },
            {
                "ImageName": "my-image",
                "ModemConfig": "my-config.conf",
                "RFNode_ID": 2,
                "TrafficNode_ID": 2,
                "isGateway": false,
                "node_type": "competitor"
            }
        ],
        "RFScenario": 8981,
        "TrafficScenario": 95571
    }

References
---------

`Batch Mode Format and Process <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253519-batch-mode-format-and-process>`_
