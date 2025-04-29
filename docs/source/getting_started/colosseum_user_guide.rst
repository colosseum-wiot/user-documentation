Colosseum User Guide
==================

If this is your first time accessing the Colosseum, see the :doc:`Quick Start Guide <quick_start_guide>`.

This article presents a listing of resources for users on how to use various components of the Colosseum as they are currently deployed in the :doc:`Colosseum Architecture </architecture/colosseum_architecture>`.

There are three primary resources that users can access in the Colosseum:

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

Using the Colosseum
~~~~~~~~~~~~~~~~~~

Uploading SSH Public Keys
------------------------

Access to Colosseum resources is provided primarily through SSH. Colosseum makes use of private/public keys to control user access. These key pairs are created by users on their local machines and the public key is uploaded to the Colosseum User Website. Follow these instructions to :doc:`Upload SSH Public Keys </getting_started/upload_ssh_keys>`.

.. note::
   The security of this authentication method is based entirely on the secrecy of the private key file. Users are expected to take measures to protect the contents of this file from disclosure.

Accessing Colosseum Resources
---------------------------

Users can access their reserved SRN containers and the File Proxy server through the SSH gateway. See the instructions for :doc:`Accessing Colosseum Resources <accessing_colosseum_resources>`.

Working with the Base LXC Container
---------------------------------

* Download the base container from the Network Storage: :doc:`Transferring the Base LXC Image from the NAS </container_mgmt/transferring_base_lxc_image>`
* Work with the base container offline and :doc:`Prepare a New Container for Upload </container_mgmt/prepare_a_new_lxc_container_for_upload>`

Uploading an LXC Container
-------------------------

LXC containers developed by users must be uploaded to their team's network storage directory prior to making a reservation through the User Website. See instructions on how to :doc:`Upload an LXC Container </container_mgmt/upload_lxc_container>` through the SSH Gateway.

Making an SRN Reservation
-----------------------

Users use the User Website to reserve SRNs within the Colosseum using a Token System. User teams are allocated a certain amount of tokens, which are used to reserve SRNs. Users select containers for each reserved SRN. See instructions for :doc:`Making a Reservation (Interactive and Batch Mode) </reservations/making_a_reservation_interactive_and_batch_mode>`.

Accessing the SRN
---------------

Once a team's reservation becomes available, users on that team will be able to log into their reserved SRNs running the container specified in the reservation request.

Logging on to an SRN
^^^^^^^^^^^^^^^^^^

A user can log into the SRNs specified in the reservation response only through the SSH gateway. Users must have :doc:`Uploaded SSH Public Keys </getting_started/upload_ssh_keys>` to the website and are recommended to have a :doc:`SSH Proxy Setup </getting_started/ssh_proxy_setup>`.

See the instruction for :doc:`Logging on to an SRN </getting_started/logging_into_an_srn>`.

Accessing Network Storage from an SRN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users will have access to their team network storage folder on all of their allocated containers from the ``/share`` directory. **Note**: this path is different from the path on the File Proxy server.

**Users must be logged into their container using the srn-user account to access the /share folder.**

To see the contents of your team network storage folder, run:

.. code-block:: bash

   sdruser@the-winning-team-container-v1-srn-001:~# ls /share
   resources/   other/

Exercising SRN Capabilities
-------------------------

Using SRN Hardware
^^^^^^^^^^^^^^^

Users should consult the :doc:`Colosseum Development Guide </architecture/colosseum_development_guide>` for information on how to access the hardware available from the containers on the SRNs.

ColosseumCLI for Practice Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

SRNs now support a command line interface within the container which will allow users to request and configure resources during a practice-mode reservation. If users are using an older base container or an outdated ColosseumCLI, follow the instructions for :doc:`Installing or Updating ColosseumCLI </radio_api_traffic/colosseum_cli>`. For information on the syntax, see the :doc:`ColosseumCLI </radio_api_traffic/colosseum_cli>` page.

The ColosseumCLI supports the following capabilities:

* Practice scenarios: :doc:`Scenarios Summary Page </scenarios/index>`
* MCHEM Scenario Configuration: :doc:`Colosseum CLI </radio_api_traffic/colosseum_cli>`

RadioAPI for Batch Mode
^^^^^^^^^^^^^^^^^^^^

In batch mode operation, users will need to conform to the Radio Command and Control (C2) API. This mode of operation is not yet supported within the Colosseum, but users are provided a description of this API to help plan for how to develop their Batch Mode containers in the :doc:`Colosseum Development Guide </architecture/colosseum_development_guide>`.

Traffic Generation
^^^^^^^^^^^^^^^

The Colosseum includes a traffic generation system that provides traffic to the user radio design through the traffic network interface. It is up to the users to direct traffic arriving on the traffic interface (tr0) to their radio interface.

For a more detailed description of the traffic system, see :doc:`Traffic Generation </radio_api_traffic/traffic_generation>`.

Prior to Session Tear-Down
------------------------

At the end of a reservation, the user's containers are removed from the SRNs. The current state of the container is not automatically saved, so all changes made and files or data created will be lost.

Save Image Snapshot
^^^^^^^^^^^^^^^^^

Users can save the state of their image through the :doc:`Colosseum CLI </radio_api_traffic/colosseum_cli>`. This will allow the user to save a new image file to the images directory on the user's team network storage.

See the instructions to :doc:`Save an Image Snapshot Using Colosseum CLI </radio_api_traffic/save_image_snapshot>`.

Copy files to Network Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^

Users can copy files to their attached network storage directories, which are mounted within the containers at ``/share/nas/<teamname>/``. Users should allow enough time before the end of their reservation for any file copy operations to complete.

During both batch and interactive reservations, users will have access to a logging directory within a container which will be automatically copied to their teams' shared directories. Any files written to this directory, along with traffic logs and collaboration server logs, will be copied at the end of a reservation.

This page provides information on how to make use of logging as well as the structure of those directories.

Using SRN Container Log Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During a reservation, each SRN will have a folder mounted within the container at ``/logs/``. During a reservation, users can use this directory as a location for any files they automatically want to be saved at the end of a reservation. Users may find this feature useful in a number of ways, particularly during batch mode reservations.

.. note::
   **The /logs/ directory has a limit of 25 GB on each SRN**, but users should keep in mind that their **team's network storage directories cannot exceed 500 GB**. If the 500 GB limit is exceeded while the /logs directory copy is in progress, it will fail.

Accessing SRN Logs After a Reservation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After a reservation is complete, users can access their logs through the File Proxy server. Users can find their logs in their team's shared drive root directory:

``/share/nas/<teamname>/RESERVATION-<id>/``

Within that folder, users can find the following subfolders:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Subfolder/File
     - Description
   * - ``__CollabServer_SRN_YYYYMMDD-HHMMSS.log``
     - | Collaboration Server Log File
       | One per reservation
   * - ``__srn_colbr_YYYYMMDD-HHMMSS.log``
     - | Collaboration Gateway PCAP File
       | One per gateway per reservation
   * - ``--srn-<id>/``
     - | Folder with contents of /logs/ for each SRN in the reservation
       | One per SRN
   * - ``traffic_logs/``
     - Folder with MGEN logs from the traffic scenario that was executed during the reservation.
