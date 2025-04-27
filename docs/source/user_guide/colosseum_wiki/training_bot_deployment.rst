Training Bot Deployment and Configuration
=======================================

**Created:** 2020-03-31T14:59:13-04:00  
**Updated:** 2020-03-31T14:59:13-04:00  

**Tags:** bot, training bot, FD_V2_537243 Import

Content
-------

VERSIONING NOTE: The original TrainingBotV6 had a critical networking issue. The fix has been resolved in the current and recommended image: **TrainingBotV6b.tar.gz**, md5 = e6f2ae5007804bd49736a0f9446e5354

I. Overview of the Bots
----------------------

1.1 Bot Multi-Frequency TDMA (MF-TDMA) Scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the "Increment 1" version, Bots communicate using QPSK at the physical layer, and Multi-Frequency TDMA (MF-TDMA) at the MAC layer. In the MF-TDMA scheme, Bots organize their transmissions across multiple time and frequency slots.

The MF-TDMA time slots are organized into (repeating) epochs, whose duration is currently 400 msec. This epoch duration is divided equally among the specified number of time slots. Bots currently communicate using a fixed total bandwidth of 2 MHz, which is divided equally among the specified number of frequency slots.

1.2 STATIC and REACTIVE modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two modes for the MF-TDMA MAC scheme. In the STATIC mode, the time-frequency slot allocations are specified statically, via a JSON-based configuration file. In the REACTIVE mode, these slot allocations are updated dynamically by a separate "Remapper" process that runs on the Master Bot, according to observed network performance. When used in Interactive session, the REACTIVE Bots require additional initialization steps as specified in Section III. When used in a Batch mode execution, users need only specify the REACTIVE mode in the Bot config file used in the Batch job. More details on each case are offered in Sections 2 and 3 below.

Note: The Reactive Bots only adapt to their own interference, they don't attempt to mitigate interference to other networks in the scenario.

1.3 Bot Collaboration Channel Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a user CIRN sends out an *InformationalDeclaration* message on the SC2 Collaboration Channel, this message is received by the REACTIVE Bot Collaboration Client (collab client) running on the Master Bot (which is always the Collaboration Gateway). The Master Bot will interpret the *scalar_performance_metric S* field of this message as a measure of the normalized goodput currently achieved by that CIRN, e.g.

- S = 0 is interpreted to mean that the CIRN is not able to service any of its offered traffic load
- S = 1 is interpreted to mean that the CIRN is able to service its entire traffic load (all ingress packets are successfully received at their respective destinations)

The Master Bot will periodically update its time-frequency slot assignments to optimize the sum of its own normalized goodput with that reported by the other CIRNs in the scenario. Conversely, each Master Bot will send its own achieved normalized goodput to all of its Collaboration Channel peers, using the same Collaboration Protocol message. The *network_id* field within the *InformationalDeclaration* message will be used to distinguish among the CIRNs in a scenario.

For the V4 release, the Bots will ignore all fields other than the *scalar_performance_metric* and *network_id* field.

II. Bot Description
-----------------

Users will make reservations for Bot SRNs in the same way they make reservations for their own SRNs. Users will control the initial version of the Bots directly through shell access to the deployed Bot container, which is located in /share/nas/common. The user password for the container is "spectrum".

Each Bot is a separate instantiation of a common GNU Radio flowgraph containing several custom blocks. As of this writing, the flowgraph contains no GUI elements, and it interfaces to applications via specified network device (currently only TUN devices are supported). This flowgraph should be used to interface the Bots to the Colosseum traffic generators (via the tr0 interface). The Bot flowgraph is named 'mf_tdma_xcvr_nogui_tun.py,' it has several command line switches, as well as a Bot config file. The Bot config file must be identical for every Bot node in the network, and its format is described in Section III.

As a debugging option, the Bots can also generate their own traffic using an internal packet generator. This mode is instantiated by running a separate flowgraph 'mf_tdma_xcvr_nogui.py'.

2.1 Bot Initialization
~~~~~~~~~~~~~~~~~~~~

The bots go through several steps when starting, the steps can vary depending on the particular bot. If the bots are in reactive mode then the Master Bot will also start the remapper and collab client. Other than the Master Bot in Reactive Mode all the bots follow the same start up process. There start up steps are:

1. Start the Bot Discovery Agent
2. Start the Remapper (for the Master Bot when in Reactive Mode)
3. Start the Collab Client (for Master Bot when in Reactive Mode)
4. Setup IP routing
5. Start the GNU Radio Flowgraph

In the current version of the bots this entire startup process has been automated with an Ubuntu Upstart script. Upstart is an init system similar to SystemD. If you are interested in how the bots startup look at this file:

/var/upstart/sc2-bot.conf

Here are some details about each step.

Step 1: Bot Discovery
^^^^^^^^^^^^^^^^^^^^

The first step in using the Bots is to initiate a rendezvous of the Bot SRNs in the network. Once the Bot Discovery Agent has been started the Bots will share their network information with each other. This will allow them to properly route IP packets from the Colosseum Traffic Generator according to the MF-TDMA mapping specified in the Bot config file.

The information the Bots share is only the SRN ID and the IP Address, for example:

.. code-block:: none

    SRN ID = 97, IP Address 172.16.197.2
    SRN ID = 98, IP Address 172.16.198.2
    SRN ID = 99, IP Address 172.16.199.2
    SRN ID = 100, IP Address 172.16.200.2
    SRN ID = 101, IP Address 172.16.201.2

Note that these five bots make up one "Bot Network" and they must all share the same Network ID, which is given in the config file. If you want to have multiple Bot Networks operating simultaneously (even if they are on different reservations) each Bot Network must have it's own config file with a Bot Network ID that is unique for each Bot Network.

Step 2: Start Remapper (only required for REACTIVE mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To instantiate the REACTIVE Bots, you will need to start a separate process known as the "Remapper" on the SRN you designate to be the Master Bot node (the Master Bot). This process dynamically assigns Bot links to MF-TDMA slots based on observed interference.

Step 3: Start Collaboration Client (only required for collaborative Bots)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to collaborate with the Bots through the Colosseum Collaboration Channel, initiate the Collaboration Client (collab client). The collab client the bots use is a modified version of the collab client that can be found `here <https://gitlab.com/darpa-sc2-phase1/collaboration-protocol-prerelease/blob/master/python/collab_client.py>`_. The modifications allow for daemonizing the collab client and for communication with the remapper.

Step 4: Setup Packet Routes
^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, setup routing between the MGEN traffic (coming from the tr0 interface) and the GNU Radio flowgraph (which consumes packets from the tun0 interface).

Step 5: Start Bot Transceiver Flowgraph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, the Bot flowgraph will be started on each Bot SRN independently. The flowgraph requires two critical arguments: the Bot ID to assign to the Bot, which is used to assign time and frequency channels (see Appendix V for details), and the path to the Bot configuration file.

III. Description of the Bot Configuration File
-------------------------------------------

When using the Bots in Batch mode the Bots require a config file which is specified in the "ModemConfig" field of the Batch JSON file. When using the Bot sin Interactive mode, you must specify the path to the config file via the "-c" option described in Section 3. The Bot config file parameters are described below. Most of the items in the config file can be left to the default options in the Example below; however there are a few items that you may want to change and there are a few items that are dependent on each other. Here is a description of each field in the config file:

**BOT_MODE** Can be either "STATIC" or "REACTIVE" (NOTE: "REACTIVE" is required for the Bots to be Collaborative.)

**MODE_OPTIONS** These are the options for the given mode. There are two sets of options to configure depending on the traffic generator.

**GENERATOR** Must be "NETWORK" (Note: "PACKET_SOURCE" is no longer supported.)

**NETWORK** Configure the Bot network to accept packets via a given network device

**DEVICE** The network device to use, usually "tun0"

**MTU** The maximum transmission unit (MTU) to use. Packets with size greater than the MTU will be dropped. At this time only setting the MTU to 1000 has been tested.

**CONFIG_PORT** (Not currently used)

**INIT_ASSIGN:** This input is a matrix specifying the mapping of links to time and frequency slots. The rows of the matrix represent frequency slots, and the columns represent time slots. The *ij*-th entry of the table is the Link ID assigned to the *i*-th frequency slot and *j-*th time slot. The default input is:

.. code-block:: json

    "INIT_ASSIGN": [[0, 1, 2, 3],
                    [4, 5, 6, 7],
                    [8, 9, 10, 11],
                    [12, 13, 14, 15]
                    [16, 17, 18, 19]]

In this example, Link ID 6 is assigned to Frequency Slot 2 and Time Slot 3.

It is possible to assign a Link ID to multiple slots, or not assign it to any slots. Link IDs are enumerated in ascending order of the transmitting Bot ID in the link, first, and receiver Bot ID, second. The Link ID assignments for a 5-Node Bot network are given in Table A.1 in the Appendix.

Frequency slots are enumerated from lowest to highest frequency slot.

**NUM_NODES** The number of Bot nodes in the network. This must be an integer between 2 and 5. (NOTE: The number of elements in INIT_ASSIGN must equal (NUM_NODES) * (NUM_NODES - 1). So in the default case of NUM_NODES = 5, the INIT_ASSIGN table will have 5x4 = 20 elements.)

**USE_BOT_DISCOVERY** Turns on bot discovery, an out of band agent that each bot uses to find the other bots in it the bot network. (Default = true)

**USE_COLOSSEUM_INI** Instructs the bot use use the Colosseum INI file, if false the bot will use default options. (Default = true)

**BOT_DISCOVERY_NETWORK_ID** Set to any positive integer which is distinct for each Bot network running in the Batch job.

**FC_OFFSET** The offset, in Hz, from the given center frequency. (Default = 5e6)

**TX_GAIN** The transmit gain, in dB, as set on the USRP

**RX_GAIN** The receive gain, in dB, as set on the USRP

An Example Bot Radio Config File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example bot config file, it is also the recommended configuration.

.. code-block:: json

    {
        "BOT_MODE": "REACTIVE",
        "MODE_OPTIONS": {"GENERATOR": "NETWORK", "DEVICE": "tun0", "MTU": 1000, "CONFIG_PORT": 34000},
        "INIT_ASSIGN": [[ 0,  1,  2,  3],
                        [ 4,  5,  6,  7],
                        [ 8,  9, 10, 11],
                        [12, 13, 14, 15],
                        [16, 17, 18, 19]],
        "NUM_NODES" : 5,
        "USE_BOT_DISCOVERY": true,
        "USE_COLOSSEUM_INI": true,
        "BOT_DISCOVERY_NETWORK_ID": 1,
        "FC_OFFSET": 5e6,
        "TX_GAIN": 20,
        "RX_GAIN": 20
    }

IV. Bot Usage in Batch Mode
-------------------------

Bot Networks can be activated in Batch Mode using the normal Batch-Mode submission process.

The JSON file for the Batch job should specify the following parameters:

**ImageName**: "TrainingBotV4"
(*NOTE: this image can be copied from the "common" sub-directory of the Colosseum NAS, i.e. /share/nas/common*)

**ModemConfig**: To use the default Bot config file, specify "srn_default_config_nX.json", where "X" is to be replaced with the index of the Bot network being deployed. For example, if two Bot networks are being deployed, use "srn_default_config_n1.json" for the first network, and "srn_default_config_n2.json" for the second network. See Section IV for information on creating custom Bot config files

**node_type:** "bot"

**isgateway:** "yes" (*NOTE: although currently "yes" must be chosen for all Bots, only one Bot per network will be selected as a Gateway*)

An example Batch JSON config file specifying a 15-node scenario with two Bot networks and a single user network is located in /share/nas/common/batch. The default Bot config files necessary to run this Batch job (i.e. "srn_default_config_nX.json" mentioned above) are provided in /share/nas/common/config. With the default config files specified, the Bots will run in REACTIVE mode and also exchange *InformationalDeclaration* messages over the Collaboration channel. For information on the individual config file parameters, please see Section IV.

*For additional help with the Bots*: A tutorial on using the STATIC Bots in Batch mode is included as part of the Webinar accessible from the top-level Colosseum page.

V. Bot Usage in Interactive Mode
-----------------------------

Using the bots in interactive mode is almost as simple as it is in Batch Mode. The process is to start all the SRNs, setup RF and Traffic with the colosseumcli tool and then start the sc2-bot Upstart service. The bot will read the config file from /root/radio_api/radio.conf, this is the same default config file that the bot uses in Batch Mode.

.. code-block:: bash

    service sc2-bot start

When you're ready to stop the bots, stop the service on each bot.

.. code-block:: bash

    service sc2-bot stop

You can also use the commands in combination with a sleep in between

.. code-block:: bash

    service sc2-bot start; sleep 300; service sc2-bot stop

You can check the status of each bot by looking at the log file in

.. code-block:: bash

    /var/log/upstart/sc2-bot.conf

You can also find the logs for the collab client and the remapper in /logs/.

One problem the bots currently have in interactive mode is that when the sc2-bot Upstart service is not properly shut down the remapper and collab_client processes are sometimes left running. Since these processes bind sockets on specific ports this can be problematic. When running multiple experiments back to back in interactive mode it's good practice to check for these processes on the master node. If the processes are running after the service has stopped, you can just kill them.

A. Appendix
----------

A.1. Link ID Assignments
~~~~~~~~~~~~~~~~~~~~~~

**Table A.1 Link ID Assignments for 5-Node Bot Network**

+---------------------+--------------------+---------------------+
| Link ID             | Transmitting Bot ID| Receiving Bot ID    |
+=====================+====================+=====================+
| 0                   | 0                  | 1                   |
+---------------------+--------------------+---------------------+
| 1                   | 0                  | 2                   |
+---------------------+--------------------+---------------------+
| 2                   | 0                  | 3                   |
+---------------------+--------------------+---------------------+
| 3                   | 0                  | 4                   |
+---------------------+--------------------+---------------------+
| 4                   | 1                  | 0                   |
+---------------------+--------------------+---------------------+
| 5                   | 1                  | 2                   |
+---------------------+--------------------+---------------------+
| 6                   | 1                  | 3                   |
+---------------------+--------------------+---------------------+
| 7                   | 1                  | 4                   |
+---------------------+--------------------+---------------------+
| 8                   | 2                  | 0                   |
+---------------------+--------------------+---------------------+
| 9                   | 2                  | 1                   |
+---------------------+--------------------+---------------------+
| 10                  | 2                  | 3                   |
+---------------------+--------------------+---------------------+
| 11                  | 2                  | 4                   |
+---------------------+--------------------+---------------------+
| 12                  | 3                  | 0                   |
+---------------------+--------------------+---------------------+
| 13                  | 3                  | 1                   |
+---------------------+--------------------+---------------------+
| 14                  | 3                  | 2                   |
+---------------------+--------------------+---------------------+
| 15                  | 3                  | 4                   |
+---------------------+--------------------+---------------------+
| 16                  | 4                  | 0                   |
+---------------------+--------------------+---------------------+
| 17                  | 4                  | 1                   |
+---------------------+--------------------+---------------------+
| 18                  | 4                  | 2                   |
+---------------------+--------------------+---------------------+
| 19                  | 4                  | 3                   |
+---------------------+--------------------+---------------------+
