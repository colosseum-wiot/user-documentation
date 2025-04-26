==========================
Frequently Asked Questions
==========================

Hardware and Computation Capabilities
------------------------------------

**Q: Is it possible to run/install packages using the internet?**

A: It is possible to set up appropriate proxies and you can access the wide internet, but it is currently restricted. We encourage users to install software on their local system due to reasons including using Colosseum resources primarily for experiments and not being limited by Colosseum reservation time.

**Q: How much storage is available for each team on the NAS server?**

A: There are quotas for each team, it can be specified according to your needs. At the moment the quota is 50 gigabytes per team.

**Q: Are the SRNs synchronized at the RF TX port to build the MIMO model using multiple SRNs?**

A: Yes, they are synchronized through Octoclocks (clock/PPS signal).

**Q: For the mMIMO case, what is the maximum number of time and phase coherent antennas/radios?**

A: The current maximum is 32 SDRs.

**Q: I assume you can build a MIMO channel model using multiple SRNs, especially for more than 2 layers, is this right?**

A: Yes, you can build a MIMO system using different SRNs.

**Q: Is there any guideline regarding the maximum sample rate that can be supported by the host (assuming default FPGA images at USRPs)?**

A: Each USRP has an independent host/server, so your only bottleneck is the speed of the single host. Also see: `Ettus X310 Kit <https://www.ettus.com/all-products/x310-kit/>`_.

**Q: What are the available bandwidth sub bands? Is it possible to make use of 5G bands 3.4Ghz and 3.5Ghz? Are 30GHz available too?**

A: Any frequency supported by UBX daughterboards can be used for your experiment.

**Q: Do users have full access to UHD settings in each USRP?**

A: Yes, you can basically flash the FPGA, but access is only through JTAG and power cycling is not permitted.

**Q: Can we physically access the SDRs to perform some real measurements?**

A: Users have full access to the SDR software and the host server. At this time users do not have "physical" access to the SDR.

**Q: Can we account for the "true" hardware impairments of the RF front-end or is this a baseband-in-the-loop simulation?**

A: Yes, the signal transmitted travels through a physical radio's pipeline which allows for true hardware impairments. Everything is Colosseum is "real", so you can emulate from traffic to waveform, including all the real-world imperfections you get in a real system.

**Q: What are the constraints of each SDR? E.g., what is the number of Tx/Rx antennas per supported per node? What is the range of operating frequency/bandwidth? Are there any constraints on the frequency range?**

A: Each SDR is an X310, with 2 daughterboards. So all the constraints are the same as the X310. See `Ettus X310 Kit <https://www.ettus.com/all-products/x310-kit/>`_.

**Q: What is the clock/sample rate in the FPGA channel emulator?**

A: MCHEM samples at 200 MS/s, see `X300/X310 Documentation <https://kb.ettus.com/X300/X310>`_.

RF Emulation Scenarios and Capabilities
--------------------------------------

**Q: Can channel emulation happen in the RF or it happens in the "baseband" and will be fed back into RF?**

A: Channel emulation happens in baseband.

**Q: Is it possible to simulate phased array antennas for directional mmWave research?**

A: Technically it is possible to simulate phased array antennas but not at mmWave.

**Q: How many taps can be specified for the channel model?**

A: It is 512 taps for each link. You can emulate up to 256x256 channels. You can specify taps for each individual link.

**Q: Does the 4-tap filter emulator incorporate both the delay due to path loss and any small-scale fading?**

A: The 4 taps are complex numbers and can be used to model any channel effect (path-loss, fading, multi-path, etc…). Each path delay is accounted for. Small-scale fading can be emulated according to your specific scenario (for example, with a ray tracer).

**Q: Is Wi-Fi unicast working (i.e., ACKs return in time?)**

A: You can always use the channel as a feedback to get the IDs. No base container has this capability currently, but users can implement it in their own codes.

**Q: How are the channel models for the 5G wireless environments modeled (in Rome, Boston, etc.)? Are they based on actual measurements/mathematical models/raytracing, etc?**

A: They are dependent on the scenarios. There are scenarios in development based on ray tracing and it is certainly possible to be able to be based on actual measurements/mathematical models.

**Q: Does Colosseum support hybrid terrestrial-satellite communication?**

A: It does support hybrid aerial communications. The delay that can be modeled by Colosseum is limited to what you would see in a scenario with 1 km of distance. As of now, satellite communication is not supported by Colosseum but maybe possible in the future.

**Q: Can users design their own scenarios?**

A: As of now, users are only provided set scenarios and are not able to design their own scenarios. We are open to working with users to create a scenario if the existing scenarios do not satisfy the users' needs.

**Q: Can users create their own custom protocol stack? (from APP to PHY)**

A: Yes, users have freedom to create a fully customized protocol stack.

**Q: What is the end to end (TX process to RX process) delay?**

A: Colosseum generates a real wireless signal over the SDR which is passed through a wire and the wire's propagation delay in near real time. It is as fast a radio can process an RF signal and as fast as the propagation can happen. We account for waveform propagation delay as well.

**Q: Are the SDRs connected 1-to-1 or is there a multi-path component in RF analog also?**

A: The SDRs are connected to the channel emulator physically. The channel matrix that we enter at the emulator takes into account multiple signals. On the receiver side, the receiver takes in the intended transmission and transmission interference from the rest of the other transmitters which adds to the complexity capabilities of Colosseum 4-tap model.

**Q: How realistic is it to only have 4 non-zero taps?**

A: We had to make a compromise between feasibility/cost and fidelity. Colosseum supports up to 512 taps per link. 4 taps is a good compromise between complexity and accuracy. This is something we inherited from DARPA/APL. In most cases the system so far has been used with path loss and propagation delay only (no multi path). We are developing a pipeline to approximate propagation profiles generated with ray tracers with a sparse 512-tap filter with 4 nonzero taps. Feedback from the community is very much appreciated. Introducing additional taps will require substantial changes in the channel emulator. Basically, it is the FPGA space needed to emulate the entire 256x256 mesh.

**Q: What about having 4 non-zero taps at the mmWave level?**

A: mmWave will be a new, redesigned quadrant with longer channels and only 16x16 mesh.

**Q: How fast are the taps updated?**

A: Scenarios are generated with 1 second resolution, then interpolation occurs, and resolution is one millisecond. So, for every millisecond we update the channel information.

**Q: The channel taps can be changed, but is the number of taps fixed?**

A: The number of taps is always fixed but they change every 1 ms. Scenarios can be made where the channel will update at various speeds or to be fixed.

**Q: Is it possible to reduce the total number of taps from 512 to something like 64-80 while each tap can be populated?**

A: Only 4 taps can be non-zero. The 4 taps are generated according to your RF scenario and are completely customizable. They are stored inside Colosseum and are automatically retrieved and processed whenever you launch a reservation. We are working on releasing a general tool that can generate the 4 taps given coordinates of nodes and the location of the region where they are placed. To enter these taps implies making a new scenario. This feature is not available to general users as of now as a directly accessible capability but we can work with individual teams on scenario building if the existing scenarios do not satisfy the users' needs.

Colosseum Containers
------------------

**Q: What is the process for using specific packages for custom experiments?**

A: A custom LXC container must be created and all packages and changes must be made on your local machine and then saved to the image and uploaded to the experiment's reservation website.

**Q: Would the container management framework support something like Kubernetes or Kubevirt?**

A: Not right now, but we are planning on supporting them.

**Q: Can users have a snapshot of the image within the container using the Colosseum CLI?**

A: Yes, and it will be saved in the images folder of your team directory.

**Q: Do the containers have access to the internet? Or do I have to download the container to install software?**

A: By default, containers do not have access to the internet. The best practice to install new software is by downloading the base image on your computer and modify it as you wish, and then upload it back to Colosseum.

**Q: What is usually included in the container exactly? Everything running on SRN?**

A: A container includes your own code to process the incoming traffic. The base containers come with the UHD drivers, Colosseum CLI, and all other requirements needed to connect to the USRPs, the MCHEM, and other components of the system.

**Q: Has there been benchmarking done to compare the potential overhead of running code in container instead of native machine? Any implications on types of experiments supportable?**

A: LXC containers give you bare metal access to hardware. So, the overhead should be negligible. The code is running locally on the SRN host. Each SRN has its own blade server.

Legacy Scenarios Support, PAWR Integration and Future Upgrades
------------------------------------------------------------

**Q: Are you going to resurrect the mandated outcomes and collaboration channel from the SC2 competition?**

A: For the time being, we are not working on resurrecting the mandated outcomes. The feature is archived at the moments as the current focus is not for competition-based experiments.

**Q: To what extent can Colosseum currently serve as a stepping-stone to in-field experimentation on the existing PAWR platforms?**

A: We have onboarded a large set of lead users including participants from the DARPA SC2 competition and other lead user communities with prior experience with Colosseum which include some NSF researchers. These teams developed the containers ansible tool chains to extend the containers that we use for Colosseum and that can be used for existing PAWR platforms. While the process is still being optimized, there is capability for instantiating the Colosseum LXC containers on the PAWR compute fabric that will allow them to connect to the SDRs that are available for PAWR.

**Q: Are there any in-field PAWR scenarios currently modeled in Colosseum?**

A: Colosseum has 2 scenarios from the PAWR platform that were based on measurement campaigns that would be run statically and remotely by the Northeastern team to develop. Recently, the PAWR team itself has run a measurement campaign and we will be releasing to the public, the data set at multiple frequencies. These frequencies (CBRS and 2.5) are currently being annotated and will be released to the community.
