==============
Colosseum Wiki
==============

Documentation for the Colosseum Radio Frequency (RF) Emulation Testbed.

Contents
========

Architecture and Overview
------------------------

.. toctree::
   :maxdepth: 1
   
   colosseum_architecture
   colosseum_development_guide
   other_resources

Platform Access
-------------

.. toctree::
   :maxdepth: 1
   
   upload_ssh_keys
   ssh_proxy_setup
   logging_into_an_srn
   logging_into_a_gpu
   file_upload_scp_rsync

Reservations
-----------

.. toctree::
   :maxdepth: 1
   
   making_a_reservation_interactive_and_batch_mode
   using_srn_reservation
   connecting_srn_and_gpu_reservations
   reserve_batch_jobs
   batch_mode_format

Command Line Tools
----------------

.. toctree::
   :maxdepth: 1
   
   colosseum_cli
   save_image_snapshot

SRN Specifications and Hardware
-----------------------------

.. toctree::
   :maxdepth: 1
   
   srn_specs
   gpus_of_an_srn
   usrps
   usrp_fpgas
   usrp_fpga_usb_jtag_flashing
   usrp_sample_rate_benchmarks
   optimizing_srn_usrp_performance
   real_time_thread_priority
   providing_gps_to_your_container

Container Management
------------------

.. toctree::
   :maxdepth: 1
   
   public_image_passwords
   setting_up_local_srn
   prepare_a_new_lxc_container_for_upload
   upload_lxc_container
   transferring_base_lxc_image
   verifying_integrity
   manage_docker_containers

Radio APIs and Traffic
--------------------

.. toctree::
   :maxdepth: 1
   
   radio_command_and_control_c2_api
   traffic_generation
   type_of_service
   collaboration_network
   collaboration_protocol_heatmap

Scenarios and Blueprints
----------------------

.. toctree::
   :maxdepth: 1
   
   scenario_json_file_format
   scenario_looping
   environment_json_schema
   blueprints

News and Announcements
--------------------

.. toctree::
   :maxdepth: 1
   
   colosseum_gpu_nodes_announcement
