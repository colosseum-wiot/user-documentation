Cisco AnyConnect Remote VPN Access
================================

The Colosseum now offers secure user VPN tunnel into the Colosseum environment for Tenants (Clients) connectivity.

To obtain remote VPN access, you must obtain LDAP user credentials from the Colosseum Sponsor before seeking access to VPN (this is the username and password provided to you when you registered your team/accounts). Once your account has been provisioned and in good standing, follow the steps outlined below to download Cisco AnyConnect VPN client for Windows/Mac or Linux OS and establish remote VPN connectivity to the environment.

1. Open your preferred browser and visit the Colosseum VPN page (you should have received the address of this page via email when your account was created).
2. Specify your LDAP username/password to login to the Cisco VPN Portal.

.. figure:: /_static/resources/getting_started/vpn/vpn_prompt.png
   :width: 300px
   :alt: VPN Prompt
   :align: center

3. Download Cisco AnyConnect Secure Mobility Client and install it on your computer on the next page.

.. figure:: /_static/resources/getting_started/vpn/vpn_download.png
   :width: 600px
   :alt: VPN Download Page
   :align: center

4. At the bottom right corner of the page, expand on **Instructions** button for a 10 Step-by-Step procedure to install the software package on your desktop.

5. Once you have successfully installed the Cisco AnyConnect Secure Mobility Client, it is ready for use.

.. note::
   On Ubuntu systems, you might need to install the ``canberra-gtk-module``:
   
   .. code-block:: bash
   
      sudo apt-get install libcanberra-gtk-module

6. Specify Colosseum VPN URL to connect (you should have received this address via email when your account was created).
7. You will be prompted to enter your LDAP credentials (your Colosseum username and password).
8. The VPN status page should show an established VPN tunnel to the Colosseum environment.
9. Now you can access the Colosseum Experiments website as you normally would, and SSH into the Colosseum Resources and the SRN Containers for your reservation.

Command Line Alternative for Linux Users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an alternative to the GUI client, Linux users can connect using openconnect with the command line:

.. code-block:: bash

   openconnect <colosseum-vpn-address> --useragent=AnyConnect --user=<your-colosseum-username>

If you decide to use the command line, please make sure that the VPN route is not the default route in the system and is not in conflict with other links (e.g., WiFi or ethernet connection).

If you lose internet connection with the VPN, you can try to restart the WiFi connection on your machine. To access the SRN servers you should also set up the route:

.. code-block:: bash

   sudo ip route add 10.100.11.53 dev tun0 scope link

And add ``10.100.11.53`` as the first nameserver entry in the ``/etc/resolv.conf`` file.
