SRN Specs and Capabilities
========================

**Created:** 2020-03-31T14:59:25-04:00  
**Updated:** 2020-03-31T14:59:25-04:00  

**Tags:** specs, specifications, hardware, SRN, ettus, nvidia, FD_V2_537243 Import

Content
-------

SRN Quadrants Capabilities
-------------------------

Colosseum Quadrants and SRNs are customizable and might have some unique capabilities compared to the remaining ones. Following is a table summarizing quadrant capabilities.

+------------+-----------+-----------------------------------------------------+
| Quadrant   | SRNs      | Capabilities Notes                                  |
+============+===========+=====================================================+
| 1          | [1-32]    | Dell PowerEdge R730 host server                     |
|            |           | Octoclock¹                                          |
|            |           | SRN-GPU link²                                       |
|            |           | Ubuntu 20.04 host OS                                |
+------------+-----------+-----------------------------------------------------+
| 2          | [33-64]   | Dell PowerEdge R730 host server                     |
|            |           | Octoclock¹                                          |
|            |           | Ubuntu 20.04 host OS                                |
+------------+-----------+-----------------------------------------------------+
| 3          | [65-96]   | Dell PowerEdge R730 host server                     |
|            |           | Octoclock¹                                          |
|            |           | Ubuntu 20.04 host OS                                |
+------------+-----------+-----------------------------------------------------+
| 4          | [97-128]  | Mix of Dell PowerEdge R750 and Dell PowerEdge R730  |
|            |           | host servers                                        |
|            |           | Ubuntu 20.04 host OS                                |
+------------+-----------+-----------------------------------------------------+

¹Octoclock
~~~~~~~~~~

SRNs with radios connected to an Octoclock clock distributor for synchronization.

²SRN-GPU link
~~~~~~~~~~~~

SRNs that are allowed to establish direct communication between the GPU nodes (check `Connecting SRN and GPU Reservations <https://colosseumneu.freshdesk.com/a/solutions/articles/61000307101>`_).

SRN Hardware
-----------

Colosseum Standard Radio Node (SRN) provides a platform for software-defined radio and machine-learning applications.

The SRN has 3 key hardware components:

- Dell Server
- NVIDIA GPU
- NI/Ettus X310 USRP Software Defined Radio

We are currently in the process of upgrading the software and hardware of the SRNs, starting from Quadrant 4 (Q4) and gradually replacing all the legacy ones. The goal is to leverage more powerful servers (Dell R750 versus the legacy Dell R730) to host two instances of the current software running on the legacy Dell R730 to drive the USRP. This multiplexing effort will allow us to run two legacy reservations on the same server in a transparent way for the users.

In this first stage, we will operate in a hybrid mode, with legacy and new servers working together in Q4, each one hosting one container. We will soon transition to Q4 running only Dell R750, and then gradually decommission all legacy hardware in all quadrants.

Legacy Dell Servers (Q1-Q2-Q3-Half_Q4)
-------------------------------------

Dell R730 Server Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+------------------------------------------------------------------+
| Hardware              | Dell PowerEdge R730 Server (210-ACXU)                            |
|                       | PE R730/xd Motherboard MLK (329-BCZK)                            |
+-----------------------+------------------------------------------------------------------+
| Processors            | Intel Xeon E5-2650 v4 2.2GHz,30M Cache,9.60GT/s QPI,Turbo,HT,12C/|
|                       | 24T (105W) Max Mem 2400MHz (338-BJDV)                            |
|                       |                                                                   |
|                       | Intel Xeon E5-2650 v4 2.2GHz,30M Cache,9.60GT/s QPI,Turbo,HT,12C/|
|                       | 24T (105W) Max Mem 2400MHz (338-BJDW)                            |
+-----------------------+------------------------------------------------------------------+
| Graphics Processing   | `NVIDIA Tesla K40M GPU <http://www.dell.com/en-us/shop/dell-nvid |
| Unit                  | ia-tesla-k40m-gpu-computing-processor/apd/490-bbsr/parts-upgrade |
|                       | s>`_ (490-BBSQ)                                                  |
|                       |                                                                   |
|                       | R730 GPU Installation Kit (490-BCDP)                             |
+-----------------------+------------------------------------------------------------------+
| Memory                | 128GB [16GB RDIMM, 2400MT/s, Dual Rank, x8 Data Width            |
|                       | (370-ACNX) x8 2400MT/s RDIMMs (370-ACPH)]                        |
|                       |                                                                   |
|                       | Performance Optimized (370-AAIP)                                 |
+-----------------------+------------------------------------------------------------------+
| Hard Drives           | Chassis with up to 8, 3.5" Hard Drives, Software RAID (350-BBEM) |
|                       |                                                                   |
|                       | Bezel (350-BBEJ)                                                 |
|                       |                                                                   |
|                       | 1TB 7.2K RPM SATA 6Gbps 3.5in Hot-plug Hard Drive,13G (400-AEEZ) |
|                       | 2x                                                                |
+-----------------------+------------------------------------------------------------------+
| Networking Adapters   | R730/xd PCIe Riser 2, Center (330-BBCO)                          |
|                       |                                                                   |
|                       | R730 PCIe Riser 3, Left (330-BBCQ)                               |
|                       |                                                                   |
|                       | R730 PCIe Rise 1 Filler Blank, Right (374-BBHS)                  |
|                       |                                                                   |
|                       | Qlogic 57810 Dual Port 10Gb Base-T Network Adapter (540-BBBD)    |
|                       |                                                                   |
|                       | Qlogic 57800 2x10Gb BT + 2x1Gb BT Network Daughterboard          |
|                       | (540-BBBZ)                                                        |
|                       |                                                                   |
|                       | iDRAC8 Enterprise, integrated Dell Remote Access Controller,      |
|                       | Enterprise (385-BBHO)                                             |
+-----------------------+------------------------------------------------------------------+

Software Versions
~~~~~~~~~~~~~~~~

+---------------+------------------------+---------------------------------------------------+
| Software      | Version                | Notes                                             |
+===============+========================+===================================================+
| Ubuntu        | Ubuntu 20.04.06 LTS    |                                                   |
|               | (Focal)                |                                                   |
+---------------+------------------------+---------------------------------------------------+
| Linux Kernel  | 5.15.0-101-lowlatency  |                                                   |
+---------------+------------------------+---------------------------------------------------+
| Nvidia Driver | 470                    |                                                   |
+---------------+------------------------+---------------------------------------------------+
| CUDA          | 9.1.85-1_amd64         | https://developer.nvidia.com/compute/cuda/9.1/Pro |
|               |                        | d/local_installers/cuda-repo-ubuntu1604-9-1-local |
|               |                        | _9.1.85-1_amd64                                   |
|               |                        |                                                   |
|               |                        | https://developer.nvidia.com/compute/cuda/9.1/Pro |
|               |                        | d/patches/1/cuda-repo-ubuntu1604-9-1-local-cublas |
|               |                        | -performance-update-1_1.0-1_amd64                 |
+---------------+------------------------+---------------------------------------------------+
| GNURadio      | 3.7.10                 | git clone --recursive --branch v3.7.10            |
|               |                        | https://github.com/gnuradio/gnuradio.git          |
+---------------+------------------------+---------------------------------------------------+
| UHD           | 3.9.5                  | git clone --branch release_003_009_005            |
|               |                        | https://github.com/EttusResearch/uhd.git          |
+---------------+------------------------+---------------------------------------------------+
| ColosseumCLI  | 19.0.0                 |                                                   |
+---------------+------------------------+---------------------------------------------------+
| gpsd          | 3.17                   | git clone --branch release-3.17                   |
|               |                        | https://git.savannah.gnu.org/git/gpsd.git         |
+---------------+------------------------+---------------------------------------------------+

New Dell Servers (Half_Q4)
-------------------------

Dell R750 Server Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+------------------------------------------------------------------+
| Hardware              | Dell PowerEdge R750 Server (210-AYCG)                            |
|                       |                                                                   |
|                       | R750 Motherboard with Broadcom 5720 Dual Port 1Gb On-Board LOM   |
|                       | (329-BFGT)                                                        |
+-----------------------+------------------------------------------------------------------+
| Processors            | 2x Intel Xeon Platinum 8358 2.6G, 32C/64T, 11.2GT/s, 48M Cache,  |
|                       | Turbo, HT (250W) DDR4-3200 (338-CBCH)                            |
+-----------------------+------------------------------------------------------------------+
| Graphics Processing   | NVIDIA Ampere A100, PCIe, 300W, 80GB Passive, Double Wide, Full  |
| Unit                  | Height GPU (490-BHBM)                                            |
|                       |                                                                   |
|                       | GPU Enablement (379-BDSQ)                                        |
+-----------------------+------------------------------------------------------------------+
| Memory                | 32GB RDIMM, 3200MT/s, Dual Rank 16Gb BASE x8 (370-AGDS)          |
|                       |                                                                   |
|                       | 3200MT/s RDIMMs (370-AEVR)                                       |
|                       |                                                                   |
|                       | Performance Optimized (370-AAIP)                                 |
+-----------------------+------------------------------------------------------------------+
| Hard Drives           | 2.5" Chassis with up to 16 SAS/SATA Drives (321-BGEZ)            |
|                       |                                                                   |
|                       | Unconfigured RAID (780-BCDS)                                     |
|                       |                                                                   |
|                       | PowerEdge 2U Standard Bezel (325-BCHU)                           |
|                       |                                                                   |
|                       | 480GB SSD SATA Read Intensive 6Gbps 512 2.5in Hot-plug AG Drive, |
|                       | 1 DWPD (400-AXTV)                                                |
+-----------------------+------------------------------------------------------------------+
| Networking Adapters   | Riser Config 2, Full Length, 4x16, 2x8 slots, DW GPU Capable     |
|                       | (330-BBRW)                                                        |
|                       |                                                                   |
|                       | Broadcom 57414 Dual Port 10/25GbE SFP28, OCP NIC 3.0 (540-BCOC)  |
|                       |                                                                   |
|                       | Broadcom 57508 Dual Port 100GbE QSFP Adapter, PCIe Low Profile   |
|                       | (540-BDEF)                                                        |
|                       |                                                                   |
|                       | iDRAC9, Enterprise 15G (385-BBQV)                                |
+-----------------------+------------------------------------------------------------------+

Software Versions
~~~~~~~~~~~~~~~~

+---------------+------------------------+---------------------------------------------------+
| Software      | Version                | Notes                                             |
+===============+========================+===================================================+
| Ubuntu        | Ubuntu 20.04.06 LTS    |                                                   |
|               | (Focal)                |                                                   |
+---------------+------------------------+---------------------------------------------------+
| Linux Kernel  | 5.15.0-101-lowlatency  |                                                   |
+---------------+------------------------+---------------------------------------------------+
| Nvidia Driver | 535                    |                                                   |
+---------------+------------------------+---------------------------------------------------+
| CUDA          |                        |                                                   |
+---------------+------------------------+---------------------------------------------------+
| GNURadio      |                        |                                                   |
+---------------+------------------------+---------------------------------------------------+
| UHD           |                        |                                                   |
+---------------+------------------------+---------------------------------------------------+
| ColosseumCLI  |                        |                                                   |
+---------------+------------------------+---------------------------------------------------+
| gpsd          |                        |                                                   |
+---------------+------------------------+---------------------------------------------------+

NI/Ettus USRP X310
-----------------

NI/Ettus X310 Network Card
~~~~~~~~~~~~~~~~~~~~~~~~~

10GbE SFP+ Network Interface Card

https://www.ettus.com/product/details/10GIGE-KIT

NI/Ettus X310
~~~~~~~~~~~~

Base Unit
^^^^^^^^^

Ettus X310

https://www.ettus.com/product/details/X310-KIT

+--------------------+-----------------------------------------------+
| Bandwidth          | 100Mhz Total / 80Mhz usable                   |
+--------------------+-----------------------------------------------+
| FPGA Resources     | XILINX Kintex 7 – 410T                        |
|                    |                                               |
|                    | Logic Cells: 406K                             |
|                    |                                               |
|                    | Memory: 28,620 Kb                             |
|                    |                                               |
|                    | Multipliers: 1540                             |
|                    |                                               |
|                    | Clock Rate: 200Mhz                            |
|                    |                                               |
|                    | Streaming Bandwidth per Channel (16-bit): 200MS/s |
+--------------------+-----------------------------------------------+
| Daughterboard      | UBX 160LP: Modified Ettus UBX 160 for reduced power |
|                    | output and increased RX/TX isolation          |
+--------------------+-----------------------------------------------+
| Networking         | 10G ethernet                                  |
+--------------------+-----------------------------------------------+
| Reference Clock    | Internal 10 MHz                               |
|                    |                                               |
|                    | https://www.ettus.com/content/files/X300_X310_Spec_Sheet.pdf |
+--------------------+-----------------------------------------------+
