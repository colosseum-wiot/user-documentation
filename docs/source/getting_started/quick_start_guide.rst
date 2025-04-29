Quick Start Guide
===============

If this is your first time using Colosseum, it is recommended that you complete the following steps to fully configure your account and familiarize yourself with Colosseum.

.. note::
   Access to Colosseum is only available through secure user VPN tunnel into the Colosseum environment for Tenants (Clients) connectivity. Please see :doc:`Cisco AnyConnect Remote VPN Access </getting_started/cisco_anyconnect_remote_vpn_access>` for more information.

1. Login to the Reservation Website at https://experiments.colosseum.net/login, using the account information you received. This username and password will be used for accessing your account from the website as well as logging in to the Colosseum File Proxy.

2. Create an SSH key-pair using command line tools and upload the public key by clicking on the "Accounts" tab on the website, following the instructions to :doc:`Upload SSH Public Keys </getting_started/upload_ssh_keys>`. This SSH key will only be used to provide access to the Colosseum SSH Gateway, which is the network entry point for Colosseum.

3. Configure your SSH client and test accessing the SSH gateway using command line tools to ensure your SSH keys are working, following the instructions in :doc:`SSH Proxy Setup </getting_started/ssh_proxy_setup>`. This configuration will make it easier for you access Colosseum resources, including SRNs and network storage.

   * The SSH Gateway is located at ``gw.colosseum.net``
   * The File Proxy Server (used to access your network storage when not logged in to an SRN) is located at ``file-proxy`` (from behind the SSH gateway)
   * The SRNs are located at ``teamname-srn###`` from behind the SSH gateway, where ``srn###`` is the SRN number, always expressed in 3-digit format, ex: 001, 043, 104


Workflow of running an experiment in Colosseum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``TODO fix URLs below``

1. Download a copy of the base container from the network storage on the File Proxy server, following the instructions for :doc:`Transferring the Base LXC Image from the NAS </container_mgmt/transferring_base_lxc_image>`.

2. Modify the container offline from the Colosseum and prepare it to upload back to the Colosseum, following the instructions to :doc:`Prepare a New Container for Upload </container_mgmt/prepare_a_new_lxc_container_for_upload>`.

3. If you are working with an older container, you should follow the instructions to install or update ColosseumCLI in a container on :doc:`ColosseumCLI </radio_api_traffic/colosseum_cli>`

4. Upload a container onto your team's shared storage using SCP, rsync, or SFTP following the instructions to :doc:`Upload an LXC Container </container_mgmt/upload_lxc_container>`. You can access your team's network storage through the File Proxy server, following the instructions for :doc:`Accessing Colosseum Resources </getting_started/accessing_colosseum_resources>`. On the File Proxy, your network storage is available at ``/share/nas/<team>/``. Containers must be uploaded to ``/share/nas/<team>/images`` to be selectable during the reservation process.

5. Make a reservation for multiple nodes by clicking on the "Reservations/View SRN Schedule" tab on the website, following the instructions for :doc:`Making a Reservation (Interactive and Batch Mode) </reservations/making_a_reservation_interactive_and_batch_mode>`. By making a reservation, you are spending an amount of your team's reservation tokens proportional to the total SRN time you are requesting.

6. Once you've successfully made a reservation you will receive a confirmation pop-up notice. Users should reference the Colosseum website at https://experiments.colosseum.net for the most up-to-date information on their reservations.

7. At your scheduled time, SSH into your SRN(s) at ``teamname-srn###`` where ``srn###`` is the SRN number. Follow the instructions to :doc:`Logging into an SRN </getting_started/logging_into_an_srn>`.

8. Configure a scenario within the Massive Channel Emulator (MCHEM) following the instructions for scenario control through :doc:`Colosseum CLI </radio_api_traffic/colosseum_cli>`. This will configure an RF channel between SRNs in your reservation.

9. Run your tests

   .. warning::
      It is your responsibility to be aware of the reservation ending time. No data within the container is saved automatically, so be sure to save data to network storage if needed.

Colosseum Overview
~~~~~~~~~~~~~~~~

See the :doc:`Release Notes </news_announcements/index>` list for more insight into the current state of Colosseum. A description of all the Colosseum subsystems is available at: :doc:`Colosseum Architecture </architecture/colosseum_architecture>`.

There are three primary types of resources that users can access in the Colosseum:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 10 10

   * - Resource
     - Availability
     - Authentication Method
     - Storage
     - Access From
     - Access To
   * - SSH Gateway
     - Persistent
     - By SSH Key
     - Home directory with limited storage
     - Internet
     - | File Proxy
       | SRN Containers 
   * - File Proxy
     - Persistent
     - Colosseum Account Password
     - | Home directory with limited storage
       | User team network storage 
     - SSH Gateway
     - | Network Storage
       | SRN Containers
   * - SRN Containers
     - When reserved
     - Container Password
     - | Container userspace (non-persistent)
       | User team network storage 
     - SSH Gateway
     - Network Storage
