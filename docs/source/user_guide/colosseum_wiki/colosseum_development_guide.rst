Colosseum Development Guide
=========================

:Created: 2020-03-31T14:59:24-04:00
:Updated: 2020-03-31T14:59:24-04:00

:Tags: development guide, hardware, specifications, nvidia, ettus, USRP, API, configuration, password, software, SRN, FD_V2_537243 Import

Overview
--------

This document provides resources to guide the user in developing software to successfully interact with the hardware on the SRN and the interfaces required by Colosseum. Specific documentation and guides for developing software for those resources is beyond the scope of this guide, and the reader is referred to the references listed at the end of this document for more information.

APIs
----

:doc:`Radio Command and Control (C2) API <radio_command_and_control_c2_api>` describes the Command and Control API that user containers must support for Batch Mode, Scrimmages, and Events

:doc:`Collaboration Protocol Specification <collaboration_protocol_specification>` describes the information exchange to be used collaboratively by CIRNs as well as the procedures for providing updates to the Collaboration Protocol.

SRN Configuration
---------------

For users seeking to replicate the SRN configuration locally, see the instructions for :doc:`Setting up and using a local SRN <setting_up_and_using_a_local_srn>`.

SRN Base Container Software Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Base Container Software List
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Software
     - Version
     - Notes
   * - Ubuntu
     - Ubuntu 16.04.3 LTS (Xenial)
     - 
   * - Linux Kernel
     - 4.4.0-109-generic
     - 
   * - Nvidia Driver
     - 387.26
     - 
   * - CUDA
     - 9.1.85-1_amd64
     - | https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda-repo-ubuntu1604-9-1-local_9.1.85-1_amd64
       | https://developer.nvidia.com/compute/cuda/9.1/Prod/patches/1/cuda-repo-ubuntu1604-9-1-local-cublas-performance-update-1_1.0-1_amd64
   * - GNURadio
     - 3.7.10
     - git clone --recursive --branch v3.7.10 https://github.com/gnuradio/gnuradio.git
   * - UHD
     - 3.9.5
     - git clone --branch release_003_009_005 https://github.com/EttusResearch/uhd.git
   * - ColosseumCLI
     - 2.2.3
     - 
   * - gpsd
     - 3.17
     - git clone --branch release-3.17 https://git.savannah.gnu.org/git/gpsd.git

Base Container Default Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One time root password for both machines is ChangeMe. Users can change their Colosseum passwords when logged into either the SSH Gateway or the File Proxy using the unix passwd utility. This will change your Colosseum account password which is used both on the Colosseum website and to access the File Proxy server within the Colosseum. Currently, password changes through the user website are not supported.

Prerequisites
~~~~~~~~~~~

Users must first :doc:`Upload their SSH Public Keys <upload_ssh_public_keys>`.

Users should have configured their SSH client following :doc:`SSH Proxy Setup <ssh_proxy_setup>`.

Users must know their current password.

Password Change Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Users should ssh into the SSH gateway from their local machine using:

.. code-block:: bash

   ~$ ssh gw.sc2colosseum.com
   user@gw:~/$

Then, type passwd at the command line to begin the password change. Enter your current Colosseum password, then enter your new password twice:

.. code-block:: bash

   user@gw:~/$ passwd
   Enter login(LDAP) password: 
   New password: 
   Re-enter new password:

If the password change is successful, the user will see the following response:

.. code-block:: bash

   LDAP password information changed for user
   passwd: password updated successfully

See the man page for passwd:

.. code-block:: bash

   man passwd

ColosseumCLI
~~~~~~~~~~~

The base containers have the ColosseumCLI pre-installed. To install ColosseumCLI in a different container, see instructions for Installing or Updating ColosseumCLI into a container: :doc:`ColosseumCLI <colosseum_cli>`

SRN Hardware Resources
--------------------

This section details how users can access the attached SDR, GPU, and memory from within the LXC container development environment.

Standard Radio Node (SRN) provides a platform for software defined radio and machine learning applications

SRN Host Hardware Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SRN has 3 key hardware components:

* Dell R730 Server
* Ettus X310 USRP Software Defined Radio 
* NVIDIA K40 GP-GPU 

Hardware
^^^^^^^

Dell PowerEdge R730 Server (210-ACXU) PE R730/xd Motherboard MLK (329-BCZK)

**Processors**

* Intel Xeon E5-2650 v4 2.2GHz,30M Cache,9.60GT/s QPI,Turbo,HT,12C/24T (105W) Max Mem 2400MHz (338-BJDV)
* Intel Xeon E5-2650 v4 2.2GHz,30M Cache,9.60GT/s QPI,Turbo,HT,12C/24T (105W) Max Mem 2400MHz (338-BJDW)

**Graphics Processing Unit**

* NVIDIA Tesla K40M GPU (490-BBSQ) 
* R730 GPU Installation Kit (490-BCDP)

**Memory**

* 128GB [16GB RDIMM, 2400MT/s, Dual Rank, x8 Data Width (370-ACNX) x8 2400MT/s RDIMMs (370-ACPH)] 
* Performance Optimized (370-AAIP)

**Hard Drives**

* Chassis with up to 8, 3.5" Hard Drives, Software RAID (350-BBEM)
* Bezel (350-BBEJ) 
* 1TB 7.2K RPM SATA 6Gbps 3.5in Hot-plug Hard Drive,13G (400-AEEZ) 2x

**Networking Adapters**

* R730/xd PCIe Riser 2, Center (330-BBCO)
* R730 PCIe Riser 3, Left (330-BBCQ)
* R730 PCIe Rise 1 Filler Blank, Right (374-BBHS)
* Qlogic 57810 Dual Port 10Gb Base-T Network Adapter (540-BBBD)
* Qlogic 57800 2x10Gb BT + 2x1Gb BT Network Daughterboard (540-BBBZ)
* iDRAC8 Enterprise, integrated Dell Remote Access Controller, Enterprise (385-BBHO)
* 10GbE SFP+ Network Card
* https://www.ettus.com/product/details/10GIGE-KIT

**USRP Base Unit**

* Ettus X310 https://www.ettus.com/product/details/X310-KIT

**USRP Bandwidth**

* 100Mhz Total / 80Mhz usable

**USRP FPGA Resources**

* XILINX Kintex 7 – 410T 
* Logic Cells: 406K 
* Memory: 28,620 Kb 
* Multipliers: 1540 
* Clock Rate: 200Mhz 
* Streaming Bandwidth per Channel (16-bit): 200MS/s

**USRP Daughterboard**

UBX 160LP:
Modified Ettus UBX 160 for reduced power output and increased RX/TX isolation. UBX-160LP is the same as the latest revision of the standard UBX-160 board, except that the NBB-400 and PHA-1+ amplifiers have been removed. You can see where these amplifiers are in the standard design on page 1 of the schematic, in blocks labeled TXBANDSEL and TXPA. The receive chain for the LP variant is unchanged from the stock UBX-160 board.

links to the amplifiers that have been removed for the LP variant: 
* https://www.minicircuits.com/pdfs/PHA-1+.pdf
* http://www.rfmd.com/store/downloads/dl/file/id/29224/nbb_400_data_sheet.pdf

**USRP Networking**

* 10G ethernet

**USRP Reference**

* Internal 10 MHz https://www.ettus.com/content/files/X300_X310_Spec_Sheet.pdf

Ettus USRP X310 SDR
~~~~~~~~~~~~~~~~~

The USRP attached to each SRN is connected by a 10Gbps Ethernet interface which is used for control and data transfer to and from the USRP. In the baseline configuration within the SRN, the USRP is controlled by UHD over the Ethernet interface (see References for more details on using UHD with the USRP X310). Within the Base LXC container, the USRP Ethernet interface is mapped as usrp0 and can be reached from the SRN at the default IP of 192.168.40.2.

See :doc:`USRPs <usrps>` for information on interacting with the USRP X310. For additional information on using the USRPs or the UHD driver, see the information listed below in the References section.

:doc:`Radio Command and Control (C2) API <radio_command_and_control_c2_api>`

At this time we do not intend to connect the SRN USRPs to an external precision 10MHz reference or 1PPS.

**DO NOT USE THE uhd_image_loader UTILITY PROVIDED IN UHD TO FLASH THE FPGA.**

**SEE DIRECTIONS IN** :doc:`USRPs <usrps>`

NVIDIA GPU
~~~~~~~~~

Each SRN contains NVIDIA GPU resources which may be used by the users within their radio application, should they choose to do so. The specifics of developing software to leverage NVIDIA GPUs are beyond the scope of this document, and the reader is referred to the References section below. Within the Base LXC Container, the following GPU devices are mapped and available as:

* /dev/nvidia0
* /dev/nvidia-uvm
* /dev/nvidiactl

See :doc:`GPUs <gpus_of_an_srn>` for more information on interacting with the NVIDIA GPU. For additional information on using or the NVIDIA GPU or CUDA, see the information listed below in the References section.

On-Board Memory
~~~~~~~~~~~~~

Each SRN is outfitted with on-board RAM, which the user may use as needed. Of course, portions of the available RAM will be used to run the SRN host operating system and user LXC container, but the remainder may be used to run supporting software, radio applications, or mapped to a RAM disk local to the SRN. A RAM disk may be useful to support fast file read/write operations during radio application execution. By default, there are no RAM disks configured in the Base LXC container, but users may allocate memory as desired to create RAM disks.

To mount a RAM disk, first create a directory at a desired location (in this example, /media/ramdisk), if one does not already exist. Note that folder permissions may require sudo privileges to create a folder, which is the case in this example.

.. code-block:: bash

   sudo mkdir /media/ramdisk

If needed, change the owner and permissions of the directory to allow non-sudo access to the mounted disk.

.. code-block:: bash

   sudo chown user:user /media/ramdisk
   sudo chmod +rw /media/ramdisk

Then, mount a tmpfs disk (in this example, the disk size is 1 GB) to that location.

.. code-block:: bash

   sudo mount -t tmpfs -o size=1024M tmpfs /media/ramdisk

This is a temporary storage drive. Users should take measures to save data (or the entire ramdisk) prior to SRN deallocation should they need to maintain any data.

GPS
~~~

Each SRN provides a simulated GPS feed into the container which will be used to provide navigation data to radio applications during scenarios. The final GPS system is still under development, but some instructions along with examples are available for :doc:`Providing GPS to your Container <providing_gps_to_your_container>`.

Note that the simulated GPS feed does not support precision timing.

Traffic Generation
~~~~~~~~~~~~~~~~

Should users want to test traffic input to their radio designs prior to when the Colosseum traffic generation system is online, they may use networking tools available within the container to generate basic IP traffic. For some recommendations on how to test network connectivity into your application, see :doc:`Traffic Generation <traffic_generation>`.

References
---------

Presented here are several references that may be useful information to users. This list is not intended to be comprehensive; users are allowed to make use of hardware as they see fit, as long as that use falls within the rules and scope of the SC2 event.

For information on developing software for the USRP X310, see the "Additional Resources" at: https://www.ettus.com/product/details/X310-KIT

For information on developing software for the NVIDA GPU, see: https://developer.nvidia.com/cuda-toolkit

OFDM Reference Design: http://dsp.rice.edu/resources/links

Other Resources