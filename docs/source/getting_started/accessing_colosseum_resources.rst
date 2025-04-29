Accessing Colosseum Resources
==========================

In the current Colosseum, the SSH Gateway is the entry point for users into the Colosseum for LXC container storage and SRN access.

.. note::
   Access to Colosseum is only available through secure user VPN tunnel into the Colosseum environment for Tenants (Clients) connectivity. Please see :doc:`Cisco AnyConnect Remote VPN Access <cisco_anyconnect_remote_vpn_access>` for more information.

Accessing the SSH Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~

Users will access the SSH gateway with the SSH public keys that they have created and uploaded to their accounts on the user wiki. Following the instructions on the process to :doc:`Upload SSH Public Keys </wiki/upload_ssh_keys>`, users should be ready to access the SSH gateway. This can be done through the ssh command on the terminal, providing your username in place of ``user``:

.. code-block:: bash

   ~$ ssh user@gw.colosseum.net
   user@gw:~$

.. note::
   Users have a home directory available on the SSH Gateway with a 25 MB storage limit. The SSH Gateway is intended only to be a point of access to other Colosseum resources. See instructions on how to use an :doc:`SSH Proxy Setup </wiki/ssh_proxy_setup>`.

.. note::
   The steps discussed here are for unix-based systems, such as Linux or Mac OSX. For Windows users there are multiple Windows ssh clients. A list of some popular ones can be found `here <https://en.wikipedia.org/wiki/Comparison_of_SSH_clients>`_.

Accessing the File Proxy Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When logged into the SSH gateway, users should be able to manually connect to available Colosseum resources, such as the File Proxy or any SRNs available to the user team. For example, once logged into the SSH gateway, a user can log into the File Proxy using the following command:

.. code-block:: bash

   user@gw:~$ ssh file-proxy
   Password:
   user@file-proxy:/$

.. note::
   Users have a home directory available on the File Proxy with a 25 MB storage limit. The File Proxy is intended only to provide user access to their team's network storage folders. When :doc:`uploading an LXC container </wiki/upload_lxc_container>`, users should be sure to have an :doc:`SSH proxy setup </wiki/ssh_proxy_setup>` and **transfer all files directly to their team's network storage folders**.

When prompted by SSH, enter your Colosseum user password, which will provide access to the File Proxy server, which will have the network storage for the team mounted at ``/share/nas/team-name/``.

.. code-block:: bash

   user@file-proxy:/$ ls /share/nas/team-name/
   images   other

Your team's directory has execute permissions for your group only, and as such can not be traversed by other users. This means that users outside of your group will not be able to read, write, or execute any files in this directory regardless of the file's unique permissions.

Preferred Method: SSH Gateway as a Proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instructions are available to get the :doc:`SSH proxy setup </wiki/ssh_proxy_setup>`.

A user can access the resources beyond the gateway using an ssh proxy configuration following the :doc:`SSH proxy setup </wiki/ssh_proxy_setup>`. This will allow the user to automatically connect through the ssh gateway to the resources on the Colosseum.

With the ssh config file in place, it is possible to access Colosseum resources using a single ssh command from the user's local machine. Under this configuration file, the user's ssh client will first log in to the SSH gateway using the private/public SSH keys, then log into the Colosseum resource (here, the File Proxy server) using the username specified in the config file with their LDAP credentials. As an example:

.. code-block:: bash

   ~$ ssh file-proxy
   Password:
   user@file-proxy:~$

This configuration will also work for secure copy (scp), secure FTP (sftp), and rsync over ssh. For more detailed information, see the article on how to :doc:`upload an LXC container </wiki/upload_lxc_container>`. As an example, to transfer a file to the user team storage via the File Proxy server, scp can be used:

.. code-block:: bash

   ~$ scp my_local_file file-proxy:/share/nas/team-name/other/
   Password:
   my_local_file                        100%   17MB   1.4MB/s   00:12
   ~$

See also: :doc:`Cisco AnyConnect Remote VPN Access <cisco_anyconnect_remote_vpn_access>`
