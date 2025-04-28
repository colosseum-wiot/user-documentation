New Scenario File Format Requirements
=================================

The latest update of the scenario creation toolchain allows users to create a full-fledged 4-taps channel, although constant in time. The toolchain was updated to support time-varying channels, supporting the nominal coherence time interval used by Colosseum of 1 ms. To simplify the deployment and reduce the amount of storage required for scenario descriptions, the toolchain also supports longer coherence intervals, multiples of 1 ms, over which the channel remains constant.

A Matlab-based tool has been developed to further simplify the scenario definition. Thanks to this, Colosseum now expects to find specific information, multiple configuration files, and parameter structures to create a scenario.

**Limits Requirements**

- The maximum number of nodes that have been tested successfully for a scenario is currently 52.
- The current dynamic range of Colosseum, i.e. the minimum and maximum representable gain value in dB, is between 0 and -43 dB. It is recommended not to go under these values.
- The delay spread supported by Colosseum is 5.12 us, i.e. the tap delay must reside within 0 and 5.11 us.

Matlab File Requirements
---------------------

The structures needed to create a scenario should be provided inside a .mat file following specific formats as explained below. Depending on the availability of information and on the type of channel simulator used, a user can provide only some of the following files (chMatrix, time, coordinates, origin) and the system will use the default values for the others.

Based on the user requirements, a scenario with mobility and a simplified version with no mobility are provided.

Scenario with Mobility
^^^^^^^^^^^^^^^^^^^^^^

**Path Gain Matrix**

- **Structure name**: chMatrix
- **Type**: cell -> cell -> complex 2x4 (delay and iq)
- **Size**: #_nodes X #_nodes X #_timestamps -> #_taps X 2
- **Default values**:

  .. code-block:: matlab

    tap.delay [1*10-9, 0, 0, 0]
    tap.iq [1+0j, 0, 0, 0]

- **Description**: A cell matrix of NxNxT (where N is the number of nodes and T is the total number of timestamps) describing the path gain behavior of each link of all the nodes in the scenario. Each element cell specifies the FIR filter delay and IQ coefficients for the multi-tap channel of a given link between Tx Node (row) and Rx Node (column). At this moment, Colosseum can support up to 4 channel scalar taps per link at a given timestamp. The iq value in dB of each cell should be less or equal to 0, while in complex numbers it should be in the range [1,1]+j[-1,1]. The delay value must be between 0 and 5.11 us.

**Timestamps**

- **Structure name**: time
- **Type**: double
- **Size**: 1 X (#_timestamps)
- **Default values**: [0, 1000]
- **Description: An array of size T consisting of all the timestamp intervals in which the node positions and corresponding path gains values are sampled. The unit is milliseconds. Colosseum allows a coherence time, i.e. the minimum time step, of 1 ms. The pipeline requires that this array should terminate with a multiple of 1000 (i.e. a second integer) in which the last values of coordinates and path gain matrix remain the same. If the provided array does not terminate with a multiple of 1000, the last values of coordinates and path gain matrix will be copied to reach a second integer timestamp.

**Coordinates (Optional)**

- **Structure name**: coordinates
- **Type**: double
- **Size**: #_nodes X 3 X #_timestamps
- **Default values**: [1, 1, 1]
- **Description**: A matrix of length Nx3xT (where N is the number of nodes and T is the total number of timestamps), with each row representing the Cartesian coordinates of the nodes. This structure is optional, and it is just stored in Colosseum as metadata.

**Origin (Optional)**

- **Structure name**: origin
- **Type**: structure
- **Size**: 1x1 structure
- **Default values**:

  .. code-block:: matlab

    origin.long = 41.8902
    origin.lat = 12.4922

- **Description**: A structure containing longitude and latitude coordinates of the origin of the scenario.

Scenario without Mobility (Static)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a static scenario that does not include mobility, a user can provide just a simplified version of the channel matrix and the system will use the default values for all other structures.

**Path Gain Matrix (Simplified)**

- **Structure name**: chMatrix
- **Type**: double
- **Size**: #_nodes X #_nodes
- **Default values**: [0, 0; 0, 0] for 2 nodes
- **Description**: A matrix NxN with N equal to the number of nodes. Each cell represents the path loss in dB of the link between a Tx node (row) and a Rx node (column). This value has to be less or equal to 0.

In this simplified case, only 1 tap with an FIR filter delay value of 1 ns will be used.

How to Request a Scenario
----------------------

To request a new scenario, please provide the following information:

- Desired name of the scenario
- Center frequency of operation
- Total number of nodes
- A ``.mat`` file with the user-defined structures

**References**

- D. Villa, M. Tehrani-Moayyed, P. Johari, S. Basagni, T. Melodia, "CaST: A Toolchain for Creating and Characterizing Realistic Wireless Network Emulation Scenarios", Proc. of the 16th ACM Workshop on Wireless Network Testbeds, Experimental evaluation & CHaracterization (WiNTECH 2022), Sydney, Australia, October 2022. [`pdf <https://ece.northeastern.edu/wineslab/papers/villa2022wintech.pdf>`_][`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2022wintech.txt>`_]

- D. Villa, M. Tehrani-Moayyed, C. Robinson,  L. Bonati, P. Johari, M. Polese, S. Basagni, T. Melodia, "Colosseum as a Digital Twin: Bridging Real-World Experimentation and Wireless Network Emulation," arXiv:2303.17063 [cs.NI], pp. 1-15, March 2023. [`pdf <https://arxiv.org/pdf/2303.17063>`_][`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/villa2024dt.txt>`_]

- L. Bonati, P. Johari, M. Polese, S. D'Oro, S. Mohanti, M. Tehrani-Moayyed, D. Villa, S. Shrivastava, C. Tassie, K. Yoder, A. Bagga, P. Patel, V. Petkov, M. Seltser, F. Restuccia, A. Gosain, K.R. Chowdhury, S. Basagni, T. Melodia, "Colosseum: Large-Scale Wireless Experimentation Through Hardware-in-the-Loop Network Emulation," Proc. of IEEE Intl. Symp. on Dynamic Spectrum Access Networks (DySPAN), Virtual Conference, December 2021. [`pdf <https://ece.northeastern.edu/wineslab/papers/bonati2021colosseum.pdf>`_] [`bibtex <https://ece.northeastern.edu/wineslab/wines_bibtex/bonati2021colosseum.txt>`_]
