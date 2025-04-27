USRP FPGA USB JTAG Flashing
==========================

**Created:** 2020-03-31T14:59:15-04:00  
**Updated:** 2020-03-31T14:59:15-04:00  

**Tags:** flash, flashing, USRP, FPGA, USB, JTAG, FD_V2_537243 Import

Content
-------

This page details how to flash a USRP FPGA image from an LXD container over USB JTAG. Note that this is the only option for programming a USRP FPGA within Colosseum. At the beginning of each SRN allocation, the stock FPGA image for the default version of UHD will be flashed to the attached USRP.

Assumptions
---------

- A stock Ettus or custom FPGA bitfile is available e.g. usrp_x310_fpga_HGS.bit
- The target USRP is attached to the machine via a USB JTAG cable
- All SRN USRPs will be attached via USB and Ethernet. Only USB will be available to users for the purpose of changing the USRP FPGA image.

JTAG Programming
--------------

A JTAG programming utility will be necessary to load FPGA images on USRPs within Colosseum. While users are free to use the JTAG programming tool of their choice, this guide will describe how to flash the FPGA using **xc3sprog**.

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

USB Devices in LXC Containers
---------------------------

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

    lxc config device add CONTAINER usb unix-char path=/dev/bus/usb/BUS/DEVICE

Here is an example call and output:

.. code-block:: bash

    sc2-user@sc2-srn-014:~$ lxc config device add b-fresh usb unix-char path=/dev/bus/usb/001/003
    
    Device usb added to b-fresh

After running this command, running lsusb in the container should show the same output as on the host machine and the container should have access to the JTAG device.
