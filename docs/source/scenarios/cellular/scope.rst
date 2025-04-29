SCOPE Scenarios
===============

These are a set of RF cellular scenarios to use with the Colosseum wireless network emulator. Scenarios have been designed in three different urban setups:

1. Rome, Italy
2. Boston, MA, US
3. Salt Lake City, UT, US (POWDER scenario)

For the Rome and Boston scenarios, the locations of the base station reflect real cell tower deployments taken from the OpenCelliD database. For the POWDER scenario, locations mirror the coordinates of the rooftop base stations deployed in the POWDER testbed in Salt Lake City.

Different versions of the above scenarios have been created for different numbers of base stations and users, different distances from the base stations users are deployed, and different mobility speeds of the users. 

Available distances between users and base stations:

- **Close**: users are deployed within 20 m from the base stations
- **Medium**: users are deployed within 50 m from the base stations
- **Far**: users are deployed within 100 m from the base stations

Available user mobility speeds:

- **Static**: users do not move for the whole duration of the scenario
- **Moderate**: users move at 3 m/s
- **Fast**: users move at 5 m/s

.. note::
  These scenarios cluster nodes in groups of 5. This means that nodes 1-5 are emulated to be closer to each other than they are to the other nodes of the scenario. The same holds for the remaining nodes, i.e., nodes 6-10, 11-15, 16-20, 21-25, 26-30, 31-35, 36-40, 41-45, and 46-50.

Rome Scenarios
--------------

The Rome scenario captures the dynamics of the city center of Rome, Italy. A total of 50 nodes are involved: 10 BSs and 40 UEs (4 UEs assigned to each BS randomly scattered around it). This is one of the densest scenarios in Colosseum and covers an area of 0.5 km².

.. figure:: /_static/resources/scenarios/cellular/rome.jpg
   :width: 300px
   :alt: Rome Cellular Scenario
   :align: center

**Node Pattern**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Node in Colosseum
     - Node in the Scenario
   * - Node 1
     - BS 1
   * - Node 2
     - UE 1 assigned to BS 1
   * - Node 3
     - UE 2 assigned to BS 1
   * - Node 4
     - UE 3 assigned to BS 1
   * - Node 5
     - UE 4 assigned to BS 1
   * - Node 6
     - BS 2
   * - Node 7
     - UE 5 assigned to BS 2
   * - ...
     - ...
   * - Node 46
     - BS 10
   * - Node 47
     - UE 37 assigned to BS 10
   * - Node 48
     - UE 38 assigned to BS 10
   * - Node 49
     - UE 39 assigned to BS 10
   * - Node 50
     - UE 40 assigned to BS 10

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 1017 (close static), 1018 (close moderate), 1028 (close fast), 1035 (medium static), 1019 (far static)
   * - Duration
     - 600 s, cyclable
   * - RF Description
     - Single tap; large scale
   * - Traffic ID
     - 10170, 10180, 10190, 10280, 10350
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 50
   * - Number of Base Station Nodes
     - 10
   * - Number of Users per Base Station
     - 4

Boston Scenarios
----------------

The Boston scenario captures the dynamics of downtown Boston, U.S. A total of 50 nodes are involved: 10 BSs and 40 users. This scenario covers an area of 0.95 km².

.. figure:: /_static/resources/scenarios/cellular/boston.jpeg
   :width: 300px
   :alt: Boston Cellular Scenario
   :align: center

The sequence of the nodes in the scenario follows the same pattern as the Rome scenarios shown above.

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 1031 (close static), 1033 (close moderate), 1034 (close fast), 1036 (medium static), 1024 (far static)
   * - Duration
     - 600 s, cyclable
   * - RF Description
     - Single tap; large scale
   * - Traffic ID
     - 10310, 10330, 10340, 10360, 10240
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 50
   * - Number of Base Station Nodes
     - 10
   * - Number of Users per Base Station
     - 4

POWDER Scenarios
----------------

The POWDER scenario mirrors the setup of the rooftop BSs deployed in the POWDER platform in Salt Lake City, U.S. A total of 40 nodes are involved: 8 BSs and 32 UEs. This scenario is the sparsest with an area of 3.6 km².

.. figure:: /_static/resources/scenarios/cellular/powder.jpg
   :width: 300px
   :alt: POWDER Testbed Cellular Scenario
   :align: center

The sequence of the nodes in the scenario follows the same pattern as the Rome scenarios shown above, but stops at node 40.

**Scenario Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - RF ID
     - 1025 (close static), 1026 (close moderate), 1030 (close fast), 1041 (medium static), 1027 (far static)
   * - Duration
     - 600 s, cyclable
   * - RF Description
     - Single tap; large scale
   * - Traffic ID
     - 10250, 10260, 10300, 10410, 10270
   * - Traffic Description
     - Bodycam
   * - Center Frequency
     - 1000.0 MHz
   * - Number of Nodes
     - 40
   * - Number of Base Station Nodes
     - 8
   * - Number of Users per Base Station
     - 4

**References**

- L. Bonati, S. D'Oro, S. Basagni, and T. Melodia, "SCOPE: An Open and Softwarized Prototyping Platform for NextG Systems," in Proceedings of ACM MobiSys, June 2021. [`pdf <https://ece.northeastern.edu/wineslab/papers/bonati2021scope.pdf>`_] [`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/bonati2021scope.txt>`_]

- POWDER Deployment. 2021. https://www.powderwireless.net/area.
