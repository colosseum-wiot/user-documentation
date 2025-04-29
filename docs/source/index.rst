===================================
Colosseum Wireless Network Emulator
===================================

Colosseum is the world's largest RF emulator designed to support research and development of large-scale, next generation radio network technologies in a repeatable and highly configurable RF environment. It combines 128 Standard Radio Nodes (SRNs) with a Massive digital Channel Emulator (MCHEM) backed by an extensive FPGA routing fabric.

Hardware Architecture
--------------------

Each SRN provides a platform for Software Defined Radio and Machine Learning applications with two key hardware components:

* A Dell R730 Server with an NVIDIA K40M GPU
* An Ettus Research USRP X310 Software-defined Radio equipped with a XILINX Kintex 7 FPGA

.. figure:: _static/resources/architecture.png
   :width: 600px
   :alt: Colosseum architecture diagram
   :align: center

   Figure 1: Colosseum architecture showing the interconnection between SRNs and MCHEM

The MCHEM facilitates real-world wireless RF channel emulation between the SRNs and can emulate fading, multipath, etc., for up to 256 x 256 independently customizable channels. This allows for large scale RF testing with up to 256 independent radio nodes each with powerful computational capabilities.

Key Capabilities
---------------

As an RF testbed, Colosseum can be utilized to:

* Emulate multiple operational environments including a 1 sq. km open field, a dense urban city, a suburban shopping mall, a desert, or anything in-between
* Emulate in real-time multipath and fading effects with high-fidelity ray-tracing
* Support high-fidelity and large-scale research on waveforms, protocols at all layers, networked applications, jamming and security, MIMO, and beamforming
* Provide full-stack repeatable environment (from RF to application layer)
* Carry out large scale testing, up to 256 radio nodes with 256x256 configurable channels
* Support cellular networks (4G, 5G), IoT, cognitive radio, ad hoc networks, edge computing, and cloud RAN research
* Implement Machine Learning algorithms in different wireless communications techniques


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started/index
   tutorials/index
   scenarios/index
   faq/index
   architecture/index
   reservations/index
   srn/index
   container_mgmt/index
   radio_api_traffic/index
   news_announcements/index

Accessibility
------------

Colosseum is remotely accessible to users and operates 24/7/365. Users can reserve Colosseum resources through a simple web interface. Emulation jobs can be done either:

* Manually in an interactive session during the scheduled time
* As batch jobs that run automatically per user's instructions

Container Environment
-------------------

Colosseum provides users with preconfigured and ready-to-use LXC containers for basic testing. Users can customize these containers based on their needs to develop and implement their own radio codes. These customized container images can be uploaded to the Colosseum servers, and users may choose to load the default or customized containers onto the SRNs during their reserved session.

.. figure:: _static/resources/containers.png
   :width: 500px
   :alt: Colosseum container structure
   :align: center
   
   Figure 1: Overview of the Colosseum container architecture

Key Features
-----------

Research Capabilities
^^^^^^^^^^^^^^^^^^^^

* **RF Emulation**: Realistic RF environments with controllable fading, multipath, and interference effects
* **Reproducibility**: Fully repeatable experiments in consistent RF conditions
* **Scale**: Support for large experimental setups with up to 256 radio nodes
* **Flexibility**: Customizable containers to implement user-specific protocols and algorithms

Supported Technologies
^^^^^^^^^^^^^^^^^^^^

* Cellular technologies (4G, 5G)
* WiFi (802.11ac, 802.11ax)
* IoT protocols
* MIMO and beamforming
* Cognitive radio systems
* Dynamic spectrum access
* Edge computing
* Cloud RAN
* Machine learning for wireless communications

Resource Allocation
^^^^^^^^^^^^^^^^^

Users have access to:

* Powerful computing resources (Dell R730 Servers, NVIDIA GPUs)
* High-quality SDR hardware (Ettus X310)
* Comprehensive RF channel emulation via MCHEM
* Shared network-attached storage for experiment data
* Pre-configured container environments

Quickstart
---------

* :doc:`Learn more about Colosseum <about>`
* :doc:`Explore available features <features>`
* :doc:`Get started with Colosseum <getting_started>`
* :doc:`Browse RF scenarios <scenarios/index>`
* :doc:`Review frequently asked questions <faq>`

.. note::
   If you are interested in becoming a Colosseum user, you can request a new team and account via the `signup form <https://docs.google.com/forms/d/e/1FAIpQLScHZ7gNyO4TB8b2xXPnbvPCSzGv22i0NREQ7p2XZyhF-dNQWA/viewform>`_
