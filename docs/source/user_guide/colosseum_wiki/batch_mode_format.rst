Batch Mode Format and Process
===========================

:Created: 2020-03-31T15:00:24-04:00
:Updated: 2020-03-31T15:00:25-04:00

:Tags: batch, json, format, batchjob, batch job, FD_V2_537243 Import

Batch Mode File Locations
------------------------

Batch configuration files must be saved to the network storage on the File Proxy at ``/share/nas/teamname/batch/``

Modem configuration files must be saved to the network storage on the File Proxy at ``/share/nas/teamname/config/``

Batch Mode JSON File Format
--------------------------

The file format will be a json file with the following parameters:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Key
     - Type
     - Mandatory?
     - Value Requirements
   * - BatchName
     - String
     - Yes
     - The name that the user wants to be displayed on the page 
   * - Duration
     - Integer
     - Yes
     - The duration of the batch job in seconds. Must be greater than 0.
   * - RFScenario
     - Integer
     - Yes
     - The RF Scenario number to be run. Must be a valid value. :doc:`Scenarios Summary List <scenarios_summary_list>`
   * - TrafficScenario
     - integer
     - Yes
     - The Traffic Scenario to be run. Must be a valid value. :doc:`Scenarios Summary List <scenarios_summary_list>`
   * - NodeData
     - array(batch_srn_map)
     - Yes
     - The mapping of SRNs to nodes in the scenarios. The table below describes the content of the array.

Each SRN will be mapped with an entry in the NodeData array defined as:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Key
     - Type
     - Mandatory?
     - Value Requirements
   * - RFNode_ID
     - Integer
     - Yes
     - Which node in the RF scenario this SRN should be mapped to. Each node in the NodeData array must be uniquely numbered 1 to NumSRNs
   * - ImageName
     - string
     - Yes
     - | The container image that should be loaded on the SRN. DefaultImage will be used if this is not provided. 
       | If there are two images with identical names in the team's /images directory and in the /nas/common directory, then the image in the team's /images directory will be loaded on the SRN.
       | Alphanumerics and dash "-" only
   * - ModemConfig
     - string
     - Yes
     - | The location of the modem config file in the /share/nas/teamname/config/ directory which will get copied into the container at /root/radio_api/radio.conf
       | Different config files can be specified for each Node and will all be pushed as "radio.conf" when the container is provisioned.
   * - isGateway
     - Boolean
     - Yes
     - | Determines if the collaboration gateway is connected to this node. If set to true this node will be connected to the collaboration network. 
       | The user can choose that all, some, or none of the nodes have a collaboration gateway attached.
       | More information on :doc:`Collaboration Network <collaboration_network>` can be found in this :doc:`link <collaboration_network>`.
       | Can only be true or false
   * - TrafficNode_ID
     - Integer
     - Yes
     - | Which node in the traffic scenario this SRN should be mapped to (if the RF and traffic scenarios are linked, this value is ignored)
       | Must be uniquely numbered 1 to min(NumSRNs,NumTrafficNodes), where NumTrafficNodes is defined in the Traffic Scenario.
   * - node_type
     - string
     - Yes
     - | The type of this node
       | Valid values are: 'competitor' or 'bot'. This parameter should be specified as 'competitor' for a standard batch mode job. 
       | If 'bot' mode is used, users can ssh into the node during a batch job, e.g., for debugging purposes.

This example batch file would map the first SRN to be the gateway node with a specially configured container, and the rest acting as client nodes:

.. code-block:: json

   {
     "BatchName": "My Test Batch",
     "Duration": 300,
     "RFScenario": 6742,
     "TrafficScenario": 1,
     "NodeData": [
       {
         "RFNode_ID"       : 1,
         "ImageName"       : "modem-image-v1",
         "ModemConfig"     : "modem_config_file_1",
         "isGateway"       : true,
         "TrafficNode_ID"  : 1,
         "node_type"       : "competitor"
       },
       {
         "RFNode_ID"       : 2,
         "ImageName"       : "modem-image-v1",
         "ModemConfig"     : "modem_config_file_2",
         "isGateway"       : false,
         "TrafficNode_ID"  : 2,
         "node_type"       : "competitor"
       },
       {
         "RFNode_ID"       : 3,
         "ImageName"       : "TrainingBotV1",
         "ModemConfig"     : "bot_config_file",
         "isGateway"       : false,
         "TrafficNode_ID"  : 3,
         "node_type"       : "bot"
       },
       {
         "RFNode_ID"       : 4,
         "ImageName"       : "TrainingBotV1",
         "ModemConfig"     : "bot_config_file",
         "isGateway"       : true,
         "TrafficNode_ID"  : 4,
         "node_type"       : "bot"
       }
    ]
   }

Batch Mode Process Overview
--------------------------

In batch mode, user radio applications and scenarios are controlled automatically by Colosseum. In this mode, users will need to have their container pre-configured to use the Radio API which will allow Colosseum to control their radio applications. Users need to be aware that in batch mode the container does not have access to the can0 interface, which restricts access from the container to some Colosseum resources, specifically:

* Containers will not have access to the teams' network storage folders. All radio application files need to be included in the container;
* Containers will not be accessible by SSH through the SSH Gateway. (Except for the nodes with node_type set to 'bot'.

.. note::
   Tokens are consumed in a discounted rate (70%) in the batch mode. This is to encourage teams to run their extensive jobs in the batch mode which allows for more efficient utilization of the Colosseum resources.

.. note::
   If the image name is not found in your team's /images directory, then Colosseum will check the /nas/common directory and if an image with the given name exists there, it will be loaded on the SRN. If there are two images with identical names in the team's /images directory and in the /nas/common directory, then the image in the team's /images directory will be loaded on the SRN.

.. note::
   Scrimmages and Tournament Events will be executed using batch mode with 'competitor' set for the node_type, so users can consider batch mode to be a representative test environment to prepare for those events.

Batch Mode Steps
---------------

1. User creates container with radio application that complies with the Radio API as described in :doc:`Radio Command and Control (C2) API <radio_command_and_control_c2_api>`.
2. User uploads their container to their network storage images/ folder using the File Proxy. 
3. User creates a batch mode configuration file following the Batch Mode File Format and uploads it to their network storage folder as indicated in those instructions. The batch file will specify radio.conf files to be used in their containers for the batch job. These files must also be available in the network storage folder indicated in the Batch Mode File Format instructions.
4. User configures and requests a batch job through the website by selecting the desired batch file which will be executed as resources become available.
5. Colosseum begins the batch job, which includes the following steps:

   a. The specified containers are loaded on the SRNs, and the colosseum.ini file is copied into the container. If specified, the radio configuration is pre-loaded into the container. For information on this, see :doc:`Radio Command and Control (C2) API <radio_command_and_control_c2_api>`.
   b. Any scripts written by the user to execute on initialization are executed. Users are encouraged to consider making use of upstart (Reference 1) or sysvinit (Reference 2) to execute scripts at startup. This can be used to start the radio application, any supporting applications, and connect the traffic network interface to the radio application. Some useful tips to consider:

      * **Tip**: By placing an upstart script in /etc/init/, you can automatically execute your radio application on start. See Reference 1 and the existing scripts in /etc/init/ for examples.
      * **Tip**: Within your upstart script, console logging can be used to log stdout and stderr. You can change the logging directory to /logs/ so they are automatically saved at the end of the batch job. See: http://upstart.ubuntu.com/cookbook/#console.

   c. After boot, the SRN controller periodically calls the status.sh RadioAPI script to check the state of each container radio to check for the READY state.
   d. When the radio container is ready to begin the scenario, it needs to ensure that the status.sh script returns the READY state. Five minutes after container boot, the SRN controller calls the start.sh RadioAPI script regardless of whether or not the container radio is in the READY state.
   e. Once start.sh has been called, the M-CHEM and traffic systems begin executing the scenario. At this point, radios will be able to communicate over the M-CHEM. The radio container needs to ensure that the status.sh script now returns ACTIVE.
   f. When the scenario is completed, the stop.sh Radio API script is called to indicate to the container to begin preparing for teardown of the container. Users may wish to use this to begin copying files to the /logs/ directory which will be made available to the users on their team network storage directory after the batch job ends. The radio container needs to ensure that the status.sh script now returns STOPPING.
   g. When the radio application has ended, the radio container needs to ensure that the status.sh script now returns FINISHED.
   h. Two minutes after stop.sh is called, the container deallocates, regardless of whether or not the container radio is in the FINISHED state.

Batch Mode Timeline
-----------------

Below is an example of the batch mode timeline for a batch mode reservation which specifies a 600 second duration (28 minute total reservation). Aside from the scenario duration, all the other intervals are fixed.

* **00:00 - 13:00** - Batch job starts; 13 minutes is given to flash the USRP, allocate/instantiate container, and run any initial startup scripts
* **13:00** - Check components for readiness (assuming answer to all is yes)
   * Did all the containers' status.sh report a 'ready' state? 
   * Did the RF subsystem report ready? (Colosseum internal readiness check)
   * Did the Traffic subsystem report ready? (Colosseum internal readiness check)
* **13:00 - 16:00** - 3 minutes for Colosseum scenario preparation
* **16:00** - Scenario Starts
   * All SRNs receive a call to start.sh
* **26:00** - Scenario Stops after 600 seconds (or after number of seconds specified in the batch file "Duration" field)
   * All SRNs receive a call to stop.sh 
* **26:00 - 28:00** - 2 minutes for user radio application cleanup (e.g., copying any data to /logs/)

References
---------

1. Upstart: http://upstart.ubuntu.com/cookbook/
2. SysVinit: http://www.manpages.info/linux/init.8.html