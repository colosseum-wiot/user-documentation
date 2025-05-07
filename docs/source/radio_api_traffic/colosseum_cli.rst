Colosseum CLI
=============

The ColosseumCLI is a command-line module to be installed in a user's container. The ColosseumCLI gives the users the ability to configure and control Colosseum resources (ex., traffic, RF, GPS, etc) during an interactive reservation. Note the ColosseumCLI is disabled during a batch reservation.

Installing/Updating ColosseumCLI to v19.0.0
------------------------------------------

The source code for ColosseumCLI of the newer version 19.0.0 is available on the following public GitHub repo: `colosseumcli-public <https://github.com/colosseum-wiot/colosseumcli-public>`_. Installation and update instructions for this version can be found in the README of that repository.

Using the ColosseumCLI
---------------------

General
~~~~~~~

See version currently installed:

.. code-block:: bash

   $ colosseumcli --version

See list of available commands:

.. code-block:: bash

   $ colosseumcli --help

See detailed help for specific commands:

.. code-block:: bash

   $ colosseumcli [rf | tg | gps] --help

RF Scenario Control Process
~~~~~~~~~~~~~~~~~~~~~~~~~~

The *rf* family of commands allows the user to query, start, and stop RF scenarios for the current reservation. To see a detailed description of all RF scenarios and their respective scenario IDs, see :doc:`Scenarios </scenarios/index>`.

Get a list of available RF scenarios:

.. code-block:: bash

   $ colosseumcli rf scenario list

Get a list of nodes and antennas for an available RF scenario:

.. code-block:: bash

   $ colosseum rf scenario nodelist <rfid>

where ``<rfid>`` is a 4-digit ID from "rf scenario list"

Start a RF scenario:

.. code-block:: bash

   $ colosseumcli rf start <rfid> [-m <radiomap>] [--cycle | -c]

- ``<rfid>`` is a 4-digit ID from "rf scenario list"
- optional: ``-m <radiomap>`` is a JSON-formatted file that specifies a custom SRN-to-ScenarioNode mapping.

   - A description of the JSON format can be found on :doc:`Scenario JSON File Format </radio_api_traffic/scenario_json_file_format>`.
   - If not provided, the Colosseum will automatically create a mapping based on the following rules:

      - There will be one to one mapping of SRN IDs to Scenario Nodes.
      - The mapping starts by mapping the lowest SRN ID to the lowest Scenario Node number.
      - The mapping will sequentially progress from there until the number of nodes in the scenario is exhausted. If there are less SRNs allocated than number of nodes in the scenario, the higher unmapped nodes in the scenario will be disregarded by the channel emulator.
      - If there are more SRNs than nodes in the scenario, SRNs with higher IDs will not be mapped into the channel emulator scenario.
      - If a radiomap is used, it must define a mapping for every node in the scenario. The colosseum will NOT fill in omitted nodes in the radiomap.

- optional: ``--cycle`` (or ``-c``) is a flag to enable scenario repeat.

   - If this flag is not specified (read: do not repeat scenario), the MCHEM will clear all channels after the scenario completes and signals will not pass until a new scenario is started.

Stop a RF scenario:

.. code-block:: bash

   $ colosseumcli rf stop

- The stop command is processed immediately, but the MCHEM RF channels may take up to 15 seconds until it is truly stopped. Therefore, it is good practice to run "rf info" after every "rf stop" to ensure MCHEM RF channels are in a stop state.

Get current/last RF scenario state:

.. code-block:: bash

   $ colosseumcli rf info

Get the radio map for the current/last RF scenario:

.. code-block:: bash

   $ colosseumcli rf radiomap

Traffic Scenario Control Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *tr* family of commands allows the user to query, start, and stop Traffic scenarios for the current reservation. To see a detailed description of all Traffic scenarios and their respective scenario IDs, see :doc:`Scenarios </scenarios/index>`.

Get a list a of available traffic scenarios:

.. code-block:: bash

   $ colosseumcli tg scenario list

Start a traffic scenario:

.. code-block:: bash

   $ colosseumcli tg start <trafid> [-m <nodemap>]


- ``<trafid>`` is a 5-digit ID from "tg scenario list".
- In interactive mode, all traffic starts 120 seconds after "tg start". So for example, if the mgn file specifies a start of 15.0, then traffic won't begin until 135 seconds after the user does "tg start."
- optional: ``-m <nodemap>`` is a JSON-formatted file that specifies a custom SRN-to-ScenarioNode mapping.

   - A description of the JSON format can be found on :doc:`Scenario JSON File Format </radio_api_traffic/scenario_json_file_format>`.
   - If not provided, the Colosseum will automatically create a mapping based on the following rules:

      - There will be one to one mapping of SRN IDs to Scenario Nodes.
      - The mapping starts by mapping the lowest SRN ID to the lowest Scenario Node number.
      - The mapping will sequentially progress from there until the number of nodes in the scenario is exhausted. If there are less SRNs allocated than number of nodes in the scenario, the higher unmapped nodes in the scenario will be disregarded by the traffic generator.
      - If there are more SRNs than nodes in the scenario, SRNs with higher IDs will not be mapped into the traffic scenario.
      - Colosseum will not assign SRNs to omitted nodes in the node map.

Stop a traffic scenario:

.. code-block:: bash

   $ colosseumcli tg stop

- The stop command is processed immediately, but the traffic generator may take up to 15 seconds before it truly stops. Therefore, it is good practice to run "tg info" after every "tg stop" to ensure the traffic generators are in a stop state.

Get current/last traffic scenario state:

.. code-block:: bash

   $ colosseumcli tg info

Get the traffic node map for the current/last traffic scenario:

.. code-block:: bash

   $ colosseumcli tg nodemap

USRP Control Process
~~~~~~~~~~~~~~~~~~

The *usrp* family of commands allows the user to interact with the USRP SDR connected to the node where the command is executed during the current reservation.

Get information on the USRP device:

.. code-block:: bash

   $ colosseumcli usrp info

The info command queries the USRP device and returns a message containing:

- The status of the USRP device, for example:

  - IDLE: the device is free and ready to use.
  - RUNNING: the device is busy operating.

- The return message code (e.g., 200).

Flash the USRP with a new UHD bitfile:

.. code-block:: bash

   $ colosseumcli usrp flash [-f <bitfile>]


- The flash command flashes the USRP image with a new UHD bitfile.
- If the ``-f <bitfile>`` option is not used, the command will flash the default USRP bitfile *usrp_x310_fpga_HGS_3_09.bit*
- ``-f`` is optional, and specifies the name of the UHD bitfile.

   - The bitfile must be hosted in ``/share/<teamname>/usrp_images/``
   - By default, all teams have an ``usrp_images`` folder in their directory with some default bitfiles
   - After the bitfile image has been copied into the usrp_images directory, the command can be simply executed as ``colosseumcli usrp flash -f usrp_x310_fpga_HG.bit``

Legacy ColosseumCLI 18.0.1 Installation (Not tested)
-------------------------------------------------

Follow the steps below to install or update the latest ColosseumCLI in your container.

1. From the File Proxy server (file-proxy), navigate to ``/share/nas/common/other/colosseumcli/``.

2. In this folder you will find two files. Copy both of these files to your team's NAS folder (ex., ``/share/nas/<teamname>/my_colosseumcli/``)
   - colosseumcli-X.X.X.tar.gz
   - colosseum_cli_prereqs.tar.gz

3. At the Reservation Portal, create an interactive reservation with the container image that you want to install the ColosseumCLI in.

4. When the reservation is up, SSH into your container as root via the colosseum gateway (129.10.14.202).

5. When inside your container, run the following commands to copy the two ColosseumCLI tar balls from your team's NAS to your container:

   .. code-block:: bash

      root@cont:$ su srn-user
      srn-user@cont:$ cd /share/my_colosseumcli/ # Note: this /share/ folder is automatically mapped to your team's NAS folder.
      srn-user@cont:$ cp *.tar.gz /tmp/
      srn-user@cont:$ exit
      root@cont:$ cd /tmp/
      root@cont:$ mv colosseumcli-X.X.X.tar.gz /root/
      root@cont:$ mv colosseum_cli_prereqs.tar.gz /root/
      root@cont:$ cd
      root@cont:$ tar xzvf colosseumcli-X.X.X.tar.gz
      root@cont:$ tar xzvf colosseum_cli_prereqs.tar.gz

6. Run the following commands to install the ColossemCLI prereqs package:

   .. code-block:: bash

      root@cont:$ cd /root/colosseum_cli_prereqs/
      root@cont:$ ./install_prereqs.sh
      # Note: some packages can not be installed concurrently -- repeat the install until there are no errors.

7. Run the following commands to install the ColosseumCLI:

   .. code-block:: bash

      root@cont:$ tar xzvf colosseumcli-X.X.X.tar.gz
      root@cont:$ cd colosseumcli-X.X.X
      root@cont:$ python3 setup.py install

8. Verify ColosseumCLI by entering the following commands:

   .. code-block:: bash

      root@cont:$ colosseumcli --version
      # You should see as output: "colosseumcli X.X.X"
      root@cont:$ colosseumcli --help
      # You should see as output a list of all colosseumcli commands.

9. Snapshot the container for future use.

   .. code-block:: bash

      root@cont:$ colosseumcli snapshot <snapshot-name> # Note: cannot have underscore characters.
