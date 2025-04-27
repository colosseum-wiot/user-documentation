Logging into an SRN
================

When a team's reservation becomes available, the selected container will be loaded onto all SRNs included in the reservation. Users may then log into their team's containers running on the SRN through SSH. With the :doc:`SSH proxy setup <ssh_proxy_setup>` in place, users can use ssh directly from their local machine to access their containers. Otherwise, users will need to first ssh to the SSH gateway (:doc:`Accessing Colosseum Resources <accessing_colosseum_resources>`) and then ssh to the user account within their container.

The base containers provided in the Colosseum have two accounts, root and srn-user. Both accounts have a default password of "ChangeMe". Upon login, users will be prompted to change the password. **Users should log in to both accounts to ensure that passwords are changed.** After the passwords are changed, use the ColosseumCLI to 'snapshot' a new container image. The next time a reservation is made, use the new container image which will have your new passwords set.

The root account is a typical root user for the container. In the base container, **the srn-user account is the only account with access to the team network storage folder** found at ``/share``. 

From inside a container, root user as a member of srn-user group cannot access ``/share/``. There are three workarounds:

1. In your container, switch to srn-user (via su srn-user) and you'll be able to access the ``/share/`` folder.
2. Do your development directly on the container and then use the ColosseumCLI to 'snapshot' the container when you're done.
3. Use a utility like scp to move files to-and-from the the file-proxy server (NAS access) and gateway (Container access).

The hostname convention is ``<teamname>-<srn#>`` (example: myteamname-001). At your scheduled reservation time, SSH into your SRN(s) at teamname-srn#. Hostnames can be found by using cat ``/etc/hosts`` on the SSH gateway. In this example, a user may receive a reservation response that indicates that SRN 1 will be available with their container:

.. code-block:: bash

   ~$ ssh teamname-001
   Password:
   root@the-winning-team-container-v1-srn-001:~#

If users are using a non-root user in their containers and wish to ssh using that account, it should be specified either on the command line or specified within the ssh config file as mentioned in the :doc:`SSH Proxy Setup <ssh_proxy_setup>`. For example, if the user is ``sdruser``, the user would connect to their container by:

.. code-block:: bash

   ~$ ssh sdruser@teamname-001
   Password:
   sdruser@the-winning-team-container-v1-srn-001:~#

Time Zone Change
--------------

To change the time zone to your local time zone use:

.. code-block:: bash

   export TZ=/usr/share/zoneinfo/Country/City

New York Time Zone Example:

.. code-block:: bash

   export TZ=/usr/share/zoneinfo/America/New_York