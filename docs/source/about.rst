=====================
About Colosseum
=====================

Overview
--------

Colosseum is the world's largest RF emulator designed to support research and development of large-scale, next generation radio network technologies in a repeatable and highly configurable RF environment. It combines 128 Standard Radio Nodes (SRNs) with a Massive digital Channel Emulator (MCHEM) backed by an extensive FPGA routing fabric.

Each SRN provides a platform for Software Defined Radio and Machine Learning applications with two key hardware components:

* A Dell R730 Server with an NVIDIA K40M GPU
* An Ettus Research USRP X310 Software-defined Radio equipped with a XILINX Kintex 7 FPGA

The MCHEM facilitates real-world wireless RF channel emulation between the SRNs and can emulate fading, multipath, etc., for up to 256 x 256 independently customizable channels. This allows for large scale RF testing with up to 256 independent radio nodes each with powerful computational capabilities.

Accessibility and Features
--------------------------

Colosseum is remotely accessible to users and operates 24/7/365. Users can reserve Colosseum resources through a simple web interface. Emulation jobs can be done either:

* Manually in an interactive session during the scheduled time
* As batch jobs that run automatically per user's instructions

As an RF testbed, Colosseum can be utilized to:

* Emulate multiple operational environments including a 1 sq. km open field, a dense urban city, a suburban shopping mall, a desert, or anything in-between
* Emulate in real-time multipath and fading effects with high-fidelity ray-tracing
* Support high-fidelity and large-scale research on waveforms, protocols at all layers, networked applications, jamming and security, MIMO, and beamforming
* Provide full-stack repeatable environment (from RF to application layer)
* Carry out large scale testing, up to 256 radio nodes with 256x256 configurable channels
* Support cellular networks (4G, 5G), IoT, cognitive radio, ad hoc networks, edge computing, and cloud RAN research
* Implement Machine Learning algorithms in different wireless communications techniques such as spectrum sharing, dynamic spectrum access, extraction of signal intelligence and optimized routing, by providing built-in powerful computational resources

Colosseum provides users with preconfigured and ready-to-use LXC containers for basic testing. Users can customize these containers based on their needs to develop and implement their own radio codes. These customized container images can be uploaded to the Colosseum servers, and users may choose to load the default or customized containers onto the SRNs during their reserved session.

How to Sign Up
-------------

If you are interested in becoming a Colosseum user, you can request for a new team and account via this `form <https://docs.google.com/forms/d/e/1FAIpQLScHZ7gNyO4TB8b2xXPnbvPCSzGv22i0NREQ7p2XZyhF-dNQWA/viewform>`_

Colosseum Webinars
-----------------

Colosseum offers introductory webinars covering various aspects of the platform, including:


1. **Introduction to Colosseum** - A high-level overview of the Colosseum architecture and its role in wireless research

2. **Colosseum Use Cases** - Description of key research use cases including WiFi, Cellular/5G, Open RAN, Mesh/Ad Hoc Networks/UAVs, Spectrum Sharing, MIMO/Beamforming, Lora/LPWAN, and AI in wireless
   (`Video <https://www.youtube.com/watch?v=vNKbr19VdWM&list=PLyPwVNte-Wvqovf58LWsfmvWLHQ-dGGQz&index=2>`_)

3. **From Colosseum to PAWR** - Discussion on migrating Colosseum experiments to PAWR platforms
   (`Video <https://www.youtube.com/watch?v=H1xT1fv3nnc&list=PLyPwVNte-Wvqovf58LWsfmvWLHQ-dGGQz&index=3>`_)

4. **Colosseum Scenarios and Traffic** - Deep dive into Colosseum RF and Traffic emulation scenarios
   (`Video <https://www.youtube.com/watch?v=kduNeOxWorw&list=PLyPwVNte-Wvqovf58LWsfmvWLHQ-dGGQz&index=4>`_)

5. **How to use Colosseum: First Time Users** - Live demonstration of running a basic experiment for first-time users
   (`Video <https://www.youtube.com/watch?v=Ct1m9aDQhwc&list=PLyPwVNte-Wvqovf58LWsfmvWLHQ-dGGQz&index=5>`_)

6. **Colosseum File Proxy and Container Creation** - Accessing logs in the file-proxy server and preparing customized LXC containers
   (`Video <https://www.youtube.com/watch?v=HmZlTQ0xL1E&list=PLyPwVNte-Wvqovf58LWsfmvWLHQ-dGGQz&index=6>`_)

7. **Colosseum Events and Community** - Review of current and future plans for Colosseum events and community outreach
   (`Video <https://www.youtube.com/watch?v=Xn1zB3b_rOc&list=PLyPwVNte-Wvqovf58LWsfmvWLHQ-dGGQz&index=7>`_)

Recorded videos and presentation files for each session are available on the Colosseum website.

Frequently Asked Questions
-------------------------

Hardware and Computation Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Q: Is it possible to run/install packages using the internet?**

A: This is currently restricted. We encourage users to install software on their local system due to reasons including using Colosseum resources primarily for experiments and not being limited by Colosseum reservation time.

**Q: How much storage is available for each team on the NAS server?**

A: There are quotas for each team, which can be specified according to your needs. At the moment, the quota is 500 gigabytes per team.

**Q: Are the SRNs synchronized at the RF TX port to build the MIMO model using multiple SRNs?**

A: Yes, they are synchronized through Octoclocks (clock/PPS signal).

**Q: For the mMIMO case, what is the maximum number of time and phase coherent antennas/radios?**

A: The current maximum is 32 SDRs.

**Q: What is the maximum sample rate that can be supported by the host (assuming default FPGA images at USRPs)?**

A: Each USRP has an independent host/server, so your only bottleneck is the speed of the single host.

RF Emulation Scenarios and Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Q: Can channel emulation happen in the RF or it happens in the "baseband" and will be fed back into RF?**

A: Channel emulation happens in baseband.

**Q: Is it possible to simulate phased array antennas for directional mmWave research?**

A: Technically it is possible to simulate phased array antennas but not at mmWave.

Colosseum Containers
~~~~~~~~~~~~~~~~~~~

**Q: What is the process for using specific packages for custom experiments?**

A: A custom LXC container must be created with all packages and changes made on your local machine, then saved to the image and uploaded to the experiment's reservation website.

**Q: Does it support LXC YAML configuration files or similar?**

A: Yes, you can configure the LXC container as you desire.

**Q: Do the containers have access to the internet?**

A: Internet connection is restricted. The best practice to install new software is by downloading the base image on your computer, modifying it as you wish, and then uploading it back to Colosseum.

Scenarios
--------

Colosseum offers a variety of RF scenarios for different research purposes:

LTE and Wi-Fi Coexistence Scenario (50005)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This scenario studies the interference of the WiFi IEEE802.11ac network on the LTE mobile UE with ISM band carrier aggregation in an urban campus scenario. It features:

* A portion of the Northeastern University Boston campus with WiFi coverage
* Two mobile LTE UEs in vehicles passing through the campus area on Huntington avenue
* An LTE base station (eNodeB) mounted on a building wall
* An outdoor WiFi access point mounted on the rooftop of the Ell Hall building
* A combination of Line of Sight (LOS) and Non-Line of Sight (NLOS) communication channel states

Integrated Access and Backhaul (IAB) Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These RF scenarios emulate wireless environments in different densely urban areas around Europe, specifically in:

* Florence, Italy
* Milan, Italy
* Barcelona, Spain
* Luxemburg, Luxemburg

Each scenario deploys around 25 IAB nodes and is intended to test large-scale IAB deployments. The scenarios are available with different variations:

* 28GHz or 3.6GHz modeled frequency
* LoS links only or all kinds of links

Other Available Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~

Colosseum offers a wide range of other scenarios, including:

* Base Test scenarios at 1 GHz
* Cellular scenarios with various channel characteristics in Rome, Boston, and Salt Lake City
* Legacy "Alleys of Austin" scenarios
* Anechoic Chamber scenarios with different boosts and taps
* User-defined scenarios
* Cellular Rural Small scenarios at different frequencies
* Real-field scenarios in Tampa, Florida with mobile nodes
* Arena Digital Twin scenarios
* Outdoor cellular scenarios in Waikiki Beach, Honolulu
* Fixed Pathloss scenarios at various frequencies
* Channel Sounding scenarios

For a complete list of available scenarios, users can check the Scenario Summary List in the Colosseum documentation.
