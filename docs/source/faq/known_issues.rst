Known Issues/Bugs
=============

This page documents known issues and bugs in the Colosseum system, along with their current status and available workarounds.

Current Known Issues
----------------

Not Getting MGEN Traffic / ColosseumCLI tg Error 500 and 409
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In interactive sessions competitors may have trouble starting or stopping tgen/tr0 traffic, specifically:

.. code-block:: bash

   root@teamname--srnX:~/name# colosseumcli tg info
   +-------------+--------+
   | Field       | Value  |
   +-------------+--------+
   | Scenario id | 12692  |
   | Status      | ACTIVE |
   
   root@teamname--srnX:~/name# colosseumcli tg stop
   Traffic Stop Failed Code: 500
   
   root@teamname--srnX:~/name# colosseumcli tg start 12692
   Colosseum failed to start traffic scenario: 12692
   HTTP POST Failed: 409

"tg info" status shows "ACTIVE", but...
- when you try "tg stop", you get a 500 Error code.
- when you try "tg start", you get a 409 Error code.

This is often caused by issuing "tg stop" and "tg start" commands within seconds apart. To prevent this from happening, we strongly urge you wait 30 seconds in-between "tg stop" and "tg start" calls.

This can also happen if you issue multiple "tg start" commands back-to-back by accident.

**Workaround**: Unfortunately, this reservation's traffic system is now unusable and there is no way of resetting it. Please contact the Help Desk with your reservation ID and they will refund the tokens for the unused portion of the reservation.

Creating snapshots with the same name of an existing image can cause an SRN error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a snapshot is made with the same name as an existing image which has read-only group file permissions, the snapshot cannot overwrite the existing image file on the shared drive.

In this example, an attempt to create a snapshot with the name "image2" will fail because it has read-only permissions for the group. This can be fixed by changing the permissions by running "chmod 664 image2.tar.gz" within the team images folder.

.. code-block:: bash

   user@file-proxy:~$ ls -l /share/nas/teamname/resources/
   total 3032938203
   -rw-r--r-- 1 armory-user teamname  902251571 May 14 01:42 image1.tar.gz
   -rw-r--r-- 1 user        teamname 1492723499 Jun 01 15:12 image2.tar.gz

In order to workaround this issue until a patch can be applied:
- Do not create a snapshot using the name of an existing image
- Change the file permissions within the shared drive while logged on to the File Proxy (ex: "chmod 664 image2.tar.gz")

In an RF scenario, there is a large spike at the scenario center frequency (1 GHz)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Massive Channel Emulator uses direct-conversion RF frontends, which at this time are uncalibrated and are subject to DC offset, IQ imbalance, and LO leakage. Because of this, competitors can expect to see some interference at the scenario center frequency. We are actively looking at mitigating this interference, both through calibration and by changing practice scenario operating frequencies.

Update: MCHEM USRP calibration is complete (introduced in Rel 1.7.1).

For optimal USRP operation, it is strongly recommended to use LO offset tuning.

From inside a container, root user as a member of srn-user group cannot access /share/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are three workarounds:

- In your container, switch to srn-user (via su srn-user) and you'll be able to access the /share/ folder.
- Do your development directly on the container and then use the ColosseumCLI to 'snapshot' the container when you're done.
- Use a utility like scp to move files to-and-from the the file-proxy (NAS access) and gateway (Container access).

tr0 interface attached to containers with NOARP set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Interactive mode workaround:

.. code-block:: bash

   ifconfig tr0 arp

Batch mode workaround:

- make sure above call is made in initialization

Reservation marked as "future"
~~~~~~~~~~~~~~~~~~~~~~~~~~

This typically happens in one of two ways:

- when a user's local clock is off by a few minutes

  - solution: make sure local clock is accurate

- or a user fills in reservation starting as soon as possible and then delays hitting the "reserve" button a few minutes

  - submit reservation request quickly or make a reservation that starts a few minutes later
  - we're working on a solution to disable "reserve" button for this scenario

Sometimes a reservation will stay in 'Future' state forever.

Make sure your computer's clock is within +/- 1 minute of Colosseum time (see time under Reservations tab when on experiments.colosseum.net/). Even though your reservation request meets the "5 minute check" during time of reservation, if the time discrepancy between your clock and Colosseum clock is large enough, the "5 minute check" actually fails behind the scenes.

Pending Batch Jobs disappear after approximately 5 minutes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A pending batch job will stay pending for about 5 minutes. If there are not enough SRNs by the time the 5 minutes is up, the batch job will automatically get removed from the queue. When the Colosseum is heavily utilized, SRN fulfillment becomes harder, and therefore this bug becomes more prevalent.

The workaround is to keep requeueing your batch job until it finally gets through. Definitely not ideal, but that's the only way for now during busy times.
