USRPs
=====

This guide covers interaction with the USRPs with the default base container image. Any customization to the container image by the user may change the instructions provided here.

.. important::

    DO NOT USE THE uhd_image_loader UTILITY PROVIDED IN UHD TO FLASH THE FPGA.

USRP Connectivity
---------------

Users can verify connectivity to the USRP through the 'uhd_find_devices' utility provided by the UHD software on the container:

.. code-block:: bash

    root@apl-test-team-1-base4nocuda-v0-srn31:~# uhd_find_devices
    linux; GNU C++ version 4.8.4; Boost_105400; UHD_003.009.005-0-unknown 
    
    ---------------------------------------------------- UHD Device 0
    --------------------------------------------------
    Device Address:
        type: x300
        addr: 192.168.40.2
        fpga: HGS
        name: 
        serial: 30EC903
        product: X310

UHD Examples
----------

Users may run a variety of test scripts provided by the UHD software to ensure that the USRP is connected and properly looping RF from TX to RX. These scripts are located at /usr/lib/uhd/examples.

USRP FPGA
--------

At the beginning of an SRN allocation, Colosseum flashes a default UHD FPGA image to the SRN USRP.

Please never flash the USRPs over Ethernet (i.e. using the uhd_image_loader utility). There is no method to power cycle the USRPs, so flashing over Ethernet will not change the FPGA image you are running.

For more information on accessing the FPGA (including the only supported flashing procedure), see :doc:`USRP FPGAs <usrp_fpgas>`.
