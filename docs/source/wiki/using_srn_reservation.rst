Using an SRN Reservation
=====================

Accessing the SRN
---------------

Once a team's reservation becomes available, users on that team will be able to log into their reserved SRNs running the container specified in the reservation request.

Logging on to an SRN
~~~~~~~~~~~~~~~~~~

A user can log into the SRNs specified in the reservation response only through the SSH gateway. Users must have :doc:`Uploaded SSH Public Keys <upload_ssh_keys>` to the website and are recommended to have a :doc:`SSH Proxy Setup <ssh_proxy_setup>`.

See the instruction for :doc:`Logging into an SRN <logging_into_an_srn>`.

Accessing Network Storage from an SRN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users will have access to their team network storage folder on all of their allocated containers from the /share directory. **Note**: this path is different from the path on the File Proxy server.

.. note::

    Users must be logged into their container using the srn-user account to access the /share folder.

To see the contents of your team network storage folder, run:

.. code-block:: bash

    srn-user@the-winning-team-container-v1-srn-001:~# ls /share
    resources/   other/

Exercising SRN Capabilities
-------------------------

Using SRN Hardware
~~~~~~~~~~~~~~~~

Users should consult the :doc:`Colosseum Development Guide <colosseum_development_guide>` for information on how to access the hardware available from the containers on the SRNs.

ColosseumCLI for Practice Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SRNs now support a command line interface within the container which will allow users to request and configure resources during a practice-mode reservation. If users are using an older base container or an outdated ColosseumCLI, follow the instructions for :doc:`Installing or Updating ColosseumCLI <colosseum_cli>`.

The ColosseumCLI supports the following capabilities:

- Practice Scenarios: :doc:`Scenarios <../../scenarios/index>`
- MCHEM Scenario Configuration: :doc:`Colosseum CLI <colosseum_cli>`

RadioAPI for Batch Mode
~~~~~~~~~~~~~~~~~~~~

In batch mode operation, users will need to conform to the Radio Command and Control (C2) API. This mode of operation is not yet supported within the Colosseum, but users are provided a description of this API to help plan for how to develop their Batch Mode containers in the :doc:`Colosseum Development Guide <colosseum_development_guide>`.

Traffic Generation
~~~~~~~~~~~~~~~

At this time, traffic generation is not supported. Examples are provided in the :doc:`Colosseum Development Guide <colosseum_development_guide>` for how to integrate a traffic interface within your radio applications.

Prior to Session Tear-Down
------------------------

At the end of a reservation, the user's containers are removed from the SRNs. The current state of the container is not automatically saved, so all changes made and files or data created will be lost.

Save Image Snapshot
~~~~~~~~~~~~~~~~

Users can save the state of their image through the :doc:`Colosseum CLI <colosseum_cli>`. This will allow the user to save a new image file to the images directory on the user's team network storage.

See the instructions to :doc:`Save an Image Snapshot <save_image_snapshot>`.

Copy files to Network Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can copy files to their attached network storage directories, which are mounted within the containers at /share/nas/team-name/. Users should allow enough time before the end of their reservation for any file copy operations to complete.
