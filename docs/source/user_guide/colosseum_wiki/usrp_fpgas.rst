USRP FPGAs
==========

.. warning::

    This page might need revision after release of the new colosseumcli

The FPGA within the SRN USRPs are accessible to users for development as part of their radio application. This page provides an overview of how to work with FPGAs.

Cautions & Caveats
----------------

Do not attempt to flash the USRPs over Ethernet (i.e. using the uhd_image_loader utility). There is no method to power cycle the USRPs, so flashing over Ethernet will not change the FPGA image you are running. It is left to the user to develop and load FPGA images to work within this constraint.

If you encounter an error dealing with the EEPROM or find the need to flash the EEPROM, please do not attempt to flash information to the EEPROM and instead create a helpdesk ticket detailing the issue you are experiencing.

If you are working with UHD, there are two options that are recommended to program the FPGA by JTAG:

.. list-table:: JTAG Programming Utilities
   :header-rows: 1
   :widths: 15 40 20 25

   * - Utility
     - Description
     - Preinstalled in Base Container?
     - Recommended UHD Compatibility
   * - xc3sprog
     - Light-weight utility for JTAG programming compatible with UHD installed in the base container
     - No
     - UHD < 3.10
   * - Vivado
     - Design suite from Xilinx with a JTAG programming utility which is compatible with newer versions of UHD
     - No
     - UHD >= 3.10

Default USRP FPGA Image
---------------------

At the beginning of an SRN allocation, Colosseum flashes a default UHD FPGA image to the SRN USRP, overwriting the prior image. In order to flash the FPGA with a new image on SRN USRPs, you will need to use a USB JTAG programmer utility, which is described below. This image is available to users on the File Proxy server at: ``/share/nas/common/usrp_X310_fpga_HGS.bit``

For instructions on how to access the File Proxy and copy files to your team's shared drive, see the instructions for :doc:`Accessing Colosseum Resources <../colosseum_introduction/accessing_colosseum_resources>`.

USRP FPGA Interface
-----------------

Also available is a JTAG connection to the USRP which will allow the users to load the FPGA on board the USRP with a custom BIT file, should they choose to do so. This is an optional procedure for users should they decide to leverage FPGA resources within the USRP in support of their radio application. The USB JTAG device is directly added to the Base LXC Container as a default USB device (with ID: 0403:6010).

Users can verify that USB JTAG device through the us of the "lsusb" Linux utility on the container:

.. code-block:: bash

    sc2-user@sc2-srn-014:~$ lsusb
    Bus 001 Device 003: ID 0403:6010 Future Technology Devices International, Ltd FT2232C Dual USB-UART/FIFO IC

Users can load a custom x310 FPGA image using the "xc3sprog" utility on the container:

.. code-block:: bash

    xc3sprog -c nexys4 -v -p 0 /path/to/fpga/image/.bit

Flashing the USRP FPGA
--------------------

.. important::

    USB JTAG is the only method supported for flashing the USRP FPGA. Users **will not have the capability to power cycle** the FPGA and will need to be mindful of that limitation when developing and integrating with the SRN USRP FPGA.

This page details how to flash a USRP FPGA image from an LXD container over USB JTAG. Note that this is the only option for programming a USRP FPGA within Colosseum. At the beginning of each SRN allocation, the stock FPGA image for the default version of UHD will be flashed to the attached USRP.

Assumptions
~~~~~~~~~

- A stock Ettus or custom FPGA bitfile is available e.g. usrp_x310_fpga_HGS.bit
- The target USRP is attached to the machine via a USB JTAG cable
- All SRN USRPs will be attached via USB and Ethernet. Only USB will be available to users for the purpose of changing the USRP FPGA image.

JTAG Programming With xc3sprog (UHD < 3.10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A JTAG programming utility will be necessary to load FPGA images on USRPs within Colosseum. While users are free to use the JTAG programming tool of their choice, this portion of the guide will describe how to flash the FPGA using **xc3sprog**. Per Ettus Research, there are known compatibility issues with the xc3sprog utility and stock versions of UHD 3.10 and above, which may leave the USRP in a state requiring reboot or additional debug not possible through the user container. Ettus Research recommends the use of the Vivado utility.

Useful xc3sprog links:

- `Homepage <http://xc3sprog.sourceforge.net/>`_
- `Manual page <http://xc3sprog.sourceforge.net/manpage.php>`_

Note: If installing xc3sprog locally, it is recommended to checkout the latest revision from the svn repository and build from source.

Using xc3sprog to program an x310 FPGA is as simple as calling the following command:

.. code-block:: bash

    xc3sprog -c nexys4 -v -p 0 /path/to/fpga/image/.bit

Here is an example call to xc3sprog with corresponding output:

.. code-block:: bash

    root@b-fresh:~# xc3sprog -c nexys4 -v -p 0 ./uhd-images_003.009.005-release/share/uhd/images/usrp_x310_fpga_HGS.bit
    
    XC3SPROG (c) 2004-2011 xc3sprog project $Rev: 785 $ OS: Linux
    
    Free software: If you contribute nothing, expect nothing!
    
    Feedback on success/failure/enhancement requests:
             http://sourceforge.net/mail/?group_id=170565
    
    Check Sourceforge for updates:
             http://sourceforge.net/projects/xc3sprog/develop
    
    Using built-in device list
    
    Using built-in cable list
    
    Cable nexys4 type ftdi VID 0x0403 PID 0x6010 Desc "Digilent USB Device" dbus data e8 enable eb cbus data 00 data 60
    
    Using Libftdi, Using JTAG frequency   6.000 MHz from undivided clock
    
    JTAG chainpos: 0 Device IDCODE = 0x13656093     Desc: XC7K410T
    
    Created from NCD file: x300;UserID=0XFFFFFFFF;COMPRESS=FALSE;Version=2014.4
    
    Target device: 7k410tffg900
    
    Created: 2015/12/21 17:04:27
    
    Bitstream length: 127023328 bits
    
    done. Programming time 21693.8 ms
    
    USB transactions: Write 7773 read 12 retries 7

JTAG Programming With Vivado (UHD >= 3.10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, while users are free to use the JTAG programming tool of their choice, this portion of the guide will describe how to flash the FPGA using **Vivado Lab Edition**, which is about 600 MB in size. This method works for flashing images from UHD 3.10 and newer and requires UHD 3.10 or above to be installed in order to find the necessary scripts referenced below.

The directions below provide a method to install Vivado from the command line.

Useful links:

- `Vivado Download <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html>`_
- `USRP Manual <http://files.ettus.com/manual/page_usrp_x3x0.html>`_ (search for: vivado)

Installing Vivado Lab Edition
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites in LXC container:

- UHD 3.10 or newer installed. These instructions assume a UHD path of /root/uhd/
- Internet access (this can be done without internet access, but some instructions pertaining to downloading items would change)

Installing Vivado:

1. Download **Vivado Lab Edition 2015.4** to your local machine using the link above
   - You will need to create a free Xilinx account
   - Alternate versions of Vivado may work, but these instructions have only been verified with 2015.4

2. Move the downloaded tarball from your local machine into your container

   .. code-block:: bash

       lxc file push Xilinx_Vivado_Lab_Lin_2015.4_1118_1.tar.gz container-name/root/

3. Untar the tarball and move into the new directory

   .. code-block:: bash

       tar -xzvf Xilinx_Vivado_Lab_Lin_2015.4_1118_1.tar.gz
       cd Xilinx_Vivado_Lab_Lin_2015.4_1118_1

4. Run the installation script

   .. code-block:: bash

       ./xsetup -b Install -e "Vivado Lab Edition (Standalone)" --agree XilinxEULA,3rdPartyEULA,WebTalkTerms

5. Navigate to the UHD installation

   .. code-block:: bash

       cd /root/uhd/

6. Checkout the fpga-src module for UHD

   .. code-block:: bash

       git submodule init
       git submodule update

7. From the top level of the UHD installation, navigate to ./fpga-src/usrp3/top/x300/

   .. code-block:: bash

       cd /root/uhd/fpga-src/usrp3/top/x300/

8. Set your paths and generate JTAG executable scripts

   .. code-block:: bash

       source setupenv.sh

   NOTE: you will need to source setupenv.sh every time the container is restarted and when you open a new connection to it, or alternatively, add the line "source /root/uhd/fpga-src/usrp3/top/x300/setupenv.sh" to the end of your ~/.bashrc file, with the appropriate path to the setupenv.sh file.

Now you should be able to call USB JTAG utilities (they should tab-complete)

- viv_jtag_list - list available JTAG targets
- viv_jtag_program - flash specified bitfile to the FPGA

These utilities are part of UHD 3.10 and newer and are wrappers around the Vivado JTAG flashing utility. They may not be available with earlier versions of UHD, but if the scripts are available they may need an earlier version of Vivado.

USB Devices in LXC Containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use JTAG programming to flash USRP FPGAs within containers, the host machine USB device must be passed in to the container. This will be handled when containers are booted on SRNs in Colosseum. The following instructions may be useful for setting up USB forwarding on local test machines.

The first step in forwarding the USB JTAG device to a container is determining the bus and device numbers of the JTAG device. Once the USRP JTAG USB cable is attached, an **lsusb** command will revel all attached USB devices along with their IDs. Here is an example call of lsusb and its output:

.. code-block:: bash

    sc2-user@sc2-srn-014:~$ lsusb
    
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
    Bus 002 Device 002: ID 8087:8002 Intel Corp.
    
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
    Bus 001 Device 004: ID 413c:a001 Dell Computer Corp. Hub
    
    Bus 001 Device 003: ID 0403:6010 Future Technology Devices International, Ltd FT2232C Dual USB-UART/FIFO IC
    
    Bus 001 Device 002: ID 8087:800a Intel Corp.
    
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

In this example, the second from bottom line is our JTAG device:
**Bus 001 Device 003: ID 0403:6010 Future Technology Devices International, Ltd FT2232C Dual USB-UART/FIFO IC**

Of particular interest are the bus and device numbers:
**Bus 001 Device 003**

In order to forward a USB device to an LXC container, the following command is called:

.. code-block:: bash

    lxc config device add <containerName> usb unix-char path=/dev/bus/usb/<busNum>/<deviceNum>

Here is an example call and output:

.. code-block:: bash

    sc2-user@sc2-srn-014:~$ lxc config device add b-fresh usb unix-char path=/dev/bus/usb/001/003
    Device usb added to b-fresh

After running this command, running lsusb in the container should show the same output as on the host machine and the container should have access to the JTAG device.
