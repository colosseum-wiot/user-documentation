Setting up and using a local SRN
=============================

**Created:** 2020-03-31T14:59:12-04:00  
**Updated:** 2020-03-31T14:59:12-04:00  

**Tags:** local, local SRN, FD_V2_537243 Import

Content
-------

How to configure a user's development host to be similar to an SRN:
-------------------------------------------------------------------

1. Install Ubuntu 16.04.6 LTS on the system.
2. Install LXD:

   .. code-block:: bash

       sudo apt-get install lxd
   
   (Simply accept defaults)

3. Logout/login (This is just so your user is added to lxd group. This can be achieved by other means)

4. The base container uses NVIDIA CUDA version 8.0.44. Download and follow the installation directions.

   Note: Only do this if you have NVIDIA GPA and plan on exercising it.
   
   Note: Users may install a more updated version, however, these versions have not been tested within the Colosseum and are not officially supported.
   
   https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda-repo-ubuntu1404-8-0-local_8.0.44-1_amd64-deb
   
   Choose the options:
   
   Linux:x86_84:Ubuntu:14.04:deb(local)
   
   Download the Deb
   
   .. code-block:: bash
   
       sudo dpkg -i cuda-repo-ubuntu1404-8-0-local_8.0.44-1_amd64.deb
       sudo apt-get update
       sudo apt-get install cuda

Once you have your local SRN setup, here are some useful LXC commands to use. For more information on how to use LXC/LXD use this tutorial (https://www.stgraber.org/2016/03/11/lxd-2-0-blog-post-series-012/)

Importing an image:
------------------

.. code-block:: bash

    lxc image import baseContainerImage.tar.gz --alias AliasName

Starting a container:
-------------------

.. code-block:: bash

    lxc init local:AliasName ContainerName
    lxc start ContainerName

Deleting a container:
-------------------

.. code-block:: bash

    lxc stop ContainerName
    lxc delete ContainerName

Exporting an image:
-----------------

.. code-block:: bash

    lxc stop ContainerName
    lxc publish ContainerName --alias NewAliasName
    lxc image export NewAliasName ./NewContainerImage.tar.gz

Editing the Containers configuration:
-----------------------------------

Option 1:

.. code-block:: bash

    lxc stop ContainerName
    lxc config edit ContainerName
    # Modify using nano editor
    # Save 
    lxc start ContainerName

Option 2:

.. code-block:: bash

    lxc stop ContainerName
    lxc config show ContainerName > container.yaml
    # Modify the container.yaml using the editor of your choice
    cat container.yaml | lxc config edit ContainerName
    # After the yaml is created only this command is required between the lxc stop and start
    lxc start ContainerName

Enable internet access from within your container:
------------------------------------------------

If your LXD installation is configured correctly, you should automatically have internet connectivity in your container (as long as your Ubuntu host has an internet connection). If you are having trouble with connectivity from your container, please follow the following steps:

1. Please ensure you have an internet connection on your Ubuntu host.
2. Run the following command on the host machine:

   .. code-block:: bash
   
       sudo dpkg-reconfigure -p medium lxd
   
   You will be prompted to answer a few questions about creating an LXD bridge interface and enabling IP addressing for the interface. Please ensure you enable IPv4 addressing (choosing all the default answers will enable IPv4 addressing).

3. After the above steps are complete, you will need to initialize and start a fresh container from your imported image (please see steps under 'Starting a container' above).
4. This new container and any containers initialized subsequently will have internet connectivity by default.

Mount a host directory to the Container
--------------------------------------

Edit the lxc configuration. Add the following lines nested under the "devices:" key

.. code-block:: yaml

    devices:
        logs:
            path: /data   #path on the container
            source: /path/on/host
            type: disk

Add a physical interface to the Container - This is advised for a lower latency connection to the USRP
----------------------------------------------------------------------------------------------------

Edit the lxc configuration. Add the following lines nested under the "devices:" key

.. code-block:: yaml

    devices:
        usrp1:
            name: usrp1
            nictype: physical
            parent: p4p1
            type: nic

**Note:** Colosseum automatically sets up the USRP physical interface when an image is loaded on SRNs during a reservation.

Add NVIDIA devices to the Container
---------------------------------

Edit the lxc configuration. Add the following lines nested under the "devices:" key

.. code-block:: yaml

    devices:
        nvidia-uvm:
            path: /dev/nvidia-uvm
            type: unix-char
        nvidia0:
            path: /dev/nvidia0
            type: unix-char
        nvidiactl:
            path: /dev/nvidiactl
            type: unix-char

Additional Configuration (which may already be present in your container config):
-------------------------------------------------------------------------------

Add a bridged interface to the Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the lxc profile configuration. Add the following lines nested under the "devices:" key

.. code-block:: yaml

    devices:
        eth0:
            mtu: "9000"
            name: eth0
            nictype: bridged
            parent: lxdbr0
            type: nic