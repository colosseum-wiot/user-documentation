Common Issues
=============

This page documents known issues and bugs in the Colosseum system, along with their current status and available workarounds.

Batch Jobs Taking Long Time to Run
--------------------------------

During times of high Colosseum usage, users experience a very long wait time. This happens because more users than usual are queueing and running batch jobs, and any new batches will experience a longer-than-usual wait time in order to wait for their turn.

Our best advice is to not procrastinate and attempt to get all your testing done in the last week before an event.

Also, the reservation system has a "holdback" of 10 SRNs for a given type of reservation. For example, if there are nothing but batch jobs running at the moment, then each Quad will always holdback 10 SRNs (thereby only allowing 22 SRNs for batch usage). This was a measure to prevent batch jobs from completely monopolizing the Colosseum -- thereby preventing interactive jobs from starting; and vice-versa.

Batch Job Failures
---------------

Make sure all files in your batch folder have properly formatted JSON. Review wiki articles to ensure your JSON is formatted correctly. Also we recommend using a JSON validator like https://jsonlint.com/

Reservation/Interactive Session Failures
------------------------------------

After uploading your container image onto the NAS, always compare its signature (ex., md5sum) with the original. Currently the Colosseum lacks notification capability about bad container images. If your reservation refuses to work, this could be a likely culprit.

In some rare cases, the USRP in your SRN suddenly disappears without warning (uhd_find_devices and uhd_usrp_probe returns nothing). This is a known UHD driver issue. Fortunately, the USRP can be recovered from within your container via JTAG reflash.

Do not execute 'colosseumcli rf stop' and 'start' commands immediately back to back (e.g., 'rf stop' then 'rf start' within 1 second). Give it >15 seconds, and the probability of anomalous behavior is significantly reduced.

Do not execute 'colosseumcli tg stop' and 'start' commands immediately back to back (e.g., 'tg stop' then '! tg start' within 1 second). Give it >120 seconds, and the probability of anomalous behavior is significantly reduced.

Website slow or down
----------------

We're working to optimize the website but in the meantime there are a few things you can do to help yourself and others have a better experience.

- Close any un-used browser tab that access the website. The reservation and batch pages poll the system for the reservation table and put a constant load on the system.
- When not in use, close down any SSH sessions to file-proxy. file-proxy is a single machine shared by all users. So please be a good citizen of Colosseum when utilizing that system.
- Make sure all files in your batch folder have properly formatted JSON. This folder is parsed when loading the batch job web page and mal-formed files increases the load on the website.

Permission denied when trying to access/ssh Colosseum resources
-----------------------------------------------------------

This may occur when your public and private SSH keys have incorrect permissions. Try the following commands in your local terminal to fix the permissions for the public and private keys:

.. code-block:: bash

   chmod 600 ~/.ssh/id_rsa
   chmod 644 ~/.ssh/id_rsa.pub

Users may also need to add the private key to the SSH agent by the following command:

.. code-block:: bash

   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_rsa

Not Getting MGEN Traffic / ColosseumCLI tg Error 500 and 409
------------------------------------------------------------

In interactive sessions competitors may have trouble starting or stopping tgen/tr0 traffic, specifically:

.. code-block:: bash

   root@teamname-srnX:~/name# colosseumcli tg info
   +-------------+--------+
   | Field       | Value  |
   +-------------+--------+
   | Scenario id | 12692  |
   | Status      | ACTIVE |
   
   root@teamname-srnX:~/name# colosseumcli tg stop
   Traffic Stop Failed Code: 500
   
   root@teamname-srnX:~/name# colosseumcli tg start 12692
   Colosseum failed to start traffic scenario: 12692
   HTTP POST Failed: 409

"tg info" status shows "ACTIVE", but...
- when you try "tg stop", you get a 500 Error code.
- when you try "tg start", you get a 409 Error code.

This is often caused by issuing "tg stop" and "tg start" commands within seconds apart. To prevent this from happening, we strongly urge you wait 30 seconds in-between "tg stop" and "tg start" calls.

This can also happen if you issue multiple "tg start" commands back-to-back by accident.

**Workaround**: Unfortunately, this reservation's traffic system is now unusable and there is no way of resetting it. Please contact the Help Desk with your reservation ID and they will refund the tokens for the unused portion of the reservation.

Creating snapshots with the same name of an existing image can cause an SRN error
---------------------------------------------------------------------------------

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
----------------------------------------------------------------------------------

The Massive Channel Emulator uses direct-conversion RF frontends, which at this time are uncalibrated and are subject to DC offset, IQ imbalance, and LO leakage. Because of this, competitors can expect to see some interference at the scenario center frequency. We are actively looking at mitigating this interference, both through calibration and by changing practice scenario operating frequencies.

Update: MCHEM USRP calibration is complete (introduced in Rel 1.7.1).

For optimal USRP operation, it is strongly recommended to use LO offset tuning.

From inside a container, root user as a member of srn-user group cannot access /share/
--------------------------------------------------------------------------------------

There are three workarounds:

- In your container, switch to srn-user (via su srn-user) and you'll be able to access the /share/ folder.
- Do your development directly on the container and then use the ColosseumCLI to 'snapshot' the container when you're done.
- Use a utility like scp to move files to-and-from the the file-proxy (NAS access) and gateway (Container access).

tr0 interface attached to containers with NOARP set
---------------------------------------------------

Interactive mode workaround:

.. code-block:: bash

   ifconfig tr0 arp

Batch mode workaround:

- make sure above call is made in initialization

Reservation marked as "future"
------------------------------

This typically happens in one of two ways:

- when a user's local clock is off by a few minutes

  - solution: make sure local clock is accurate

- or a user fills in reservation starting as soon as possible and then delays hitting the "reserve" button a few minutes

  - submit reservation request quickly or make a reservation that starts a few minutes later
  - we're working on a solution to disable "reserve" button for this scenario

Sometimes a reservation will stay in 'Future' state forever.

Make sure your computer's clock is within +/- 1 minute of Colosseum time (see time under Reservations tab when on experiments.colosseum.net/). Even though your reservation request meets the "5 minute check" during time of reservation, if the time discrepancy between your clock and Colosseum clock is large enough, the "5 minute check" actually fails behind the scenes.

Pending Batch Jobs disappear after approximately 5 minutes
----------------------------------------------------------

A pending batch job will stay pending for about 5 minutes. If there are not enough SRNs by the time the 5 minutes is up, the batch job will automatically get removed from the queue. When the Colosseum is heavily utilized, SRN fulfillment becomes harder, and therefore this bug becomes more prevalent.

The workaround is to keep requeueing your batch job until it finally gets through. Definitely not ideal, but that's the only way for now during busy times.

