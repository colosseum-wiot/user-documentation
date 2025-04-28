Common Issues & Frequently Asked Questions (FAQ)
===========================================

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
