Using an SRN Reservation
=====================

**Created:** 2020-03-31T14:59:19-04:00  
**Updated:** 2020-03-31T14:59:19-04:00  

**Tags:** reservation, SSH, accessing, FD_V2_537243 Import

Content
-------

Accessing the SRN
---------------

Once a team's reservation becomes available, users on that team will be able to log into their reserved SRNs running the container specified in the reservation request.

Logging on to an SRN
~~~~~~~~~~~~~~~~~~

A user can log into the SRNs specified in the reservation response only through the SSH gateway. Users must have `Uploaded SSH Public Keys <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253402-upload-ssh-public-keys>`_ to the website and are recommended to have a `SSH Proxy Setup <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253369-ssh-proxy-setup>`_.

See the instruction for `Logging into an SRN <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253366-logging-into-and-srn>`_.

Accessing Network Storage from an SRN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users will have access to their team network storage folder on all of their allocated containers from the /share directory. **Note**: this path is different from the path on the File Proxy server.

**Users must be logged into their container using the srn-user account to access the /share folder.**

To see the contents of your team network storage folder, run:

.. code-block:: bash

    srn-user@the-winning-team-container-v1-srn-001:~# ls /share
    images/   other/

Exercising SRN Capabilities
-------------------------

Using SRN Hardware
~~~~~~~~~~~~~~~~

Users should consult the `Colosseum Development Guide <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253403-colosseum-development-guide>`_ for information on how to access the hardware available from the containers on the SRNs.

ColosseumCLI for Practice Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SRNs now support a command line interface within the container which will allow users to request and configure resources during a practice-mode reservation. If users are using an older base container or an outdated ColosseumCLI, follow the instructions for `Installing or Updating ColosseumCLI <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253397-colosseum-cli>`_.

The ColosseumCLI supports the following capabilities:

- Practice Scenarios: `Scenarios <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253456-scenarios-summary-list>`_
- MCHEM Scenario Configuration: `Colosseum CLI <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253397-colosseum-cli>`_
- GPS Emulation into Container: At this time, GPS is not yet fully integrated. See the instructions for how to `Provide GPS to your Container <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253384-providing-gps-to-your-container>`_ for examples of how this feature will be integrated into the container.

RadioAPI for Batch Mode
~~~~~~~~~~~~~~~~~~~~

In batch mode operation, users will need to conform to the Radio Command and Control (C2) API. This mode of operation is not yet supported within the Colosseum, but users are provided a description of this API to help plan for how to develop their Batch Mode containers in the `Colosseum Development Guide <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253403-colosseum-development-guide>`_.

Traffic Generation
~~~~~~~~~~~~~~~

At this time, traffic generation is not supported. Examples are provided in the `Colosseum Development Guide <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253403-colosseum-development-guide>`_ for how to integrate a traffic interface within your radio applications.

Prior to Session Tear-Down
------------------------

At the end of a reservation, the user's containers are removed from the SRNs. The current state of the container is not automatically saved, so all changes made and files or data created will be lost.

Save Image Snapshot
~~~~~~~~~~~~~~~~

Users can save the state of their image through the `Colosseum CLI <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253397-colosseum-cli>`_. This will allow the user to save a new image file to the images directory on the user's team network storage.

See the instructions to `Save an Image Snapshot <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253381-save-an-image-snapshot-using-colosseumcli>`_.

Copy files to Network Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can copy files to their attached network storage directories, which are mounted within the containers at /share/nas/team-name/. Users should allow enough time before the end of their reservation for any file copy operations to complete.
