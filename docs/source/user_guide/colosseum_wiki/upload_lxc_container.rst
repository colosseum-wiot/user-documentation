Upload an LXC Container
=====================

**Created:** 2020-03-31T14:59:14-04:00  
**Updated:** 2020-03-31T14:59:14-04:00  

**Tags:** lxc container, upload, LXC, FD_V2_537243 Import

Content
-------

Users must upload their LXC containers to the images subdirectory on their team's network storage to be able to use them in an SRN reservation. Each team has access to a team-specific shared drive mounted on the Colosseum File Proxy server. Users should use an SSH-based transfer method, such as scp or rsync to tranfer their container to the File Proxy server.

Colosseum also requires specific file permissions to be set on each container file. See the "Verifying Container Permissions" section at the bottom of this page for details.

Prerequisites
-----------

In order to access the File Proxy server, users must have already `Uploaded SSH Public Keys <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253402-upload-ssh-public-keys>`_.

*****The user MUST have their ssh client configured per the `SSH Proxy Setup <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253369-ssh-proxy-setup>`_ instructions.*****

Users are encouraged to verify the container operates appropriately before uploading to the Colosseum. At minimum the container must be accessible via SSH to be useful during an interactive session.

Prior to starting an upload, users should publish and export their local container by following the instructions in `Prepare a New Container for Upload <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253428-prepare-a-new-container-for-upload>`_

Uploading an LXC Container to the Colosseum File Proxy Server
-----------------------------------------------------------

The Colosseum reservation system checks a specific directory in each team's network attached storage space for containers to use in reservations. Containers must be uploaded to /share/nas/team-name/images/ to be available to the team when making a reservation.

Users may use one of the following tools to upload their container.

Rsync
~~~~~

The rsync utility provides a means to synchronize folder content between a local and remote host. The rsync utility inspects the content in each folder, identifies the differences in that content, and reconciles those differences by transferring the file differences. Using rsync requires a more command operation configuration, but the utility is a bit more flexible than scp and users may find it useful. Additionally, with proper configuration, rsync will allow the user to resume incomplete or partial transfers.

See the following instructions on how to use rsync: `File Upload by scp and rsync <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253365-file-upload-by-scp-and-rsync>`_

**Note**: rsync has the capability to remove files on either the remote or local folder as part of the reconciliation operation. If users are unfamiliar with rsync, it is recommended that they test its use on local folders which do not contain critical data. Colosseum Administrators may not be able to recover data accidentally lost.

Secure Copy (SCP)
~~~~~~~~~~~~~~~

Secure copy is a version of the unix copy (cp) command that uses the SSH protocol to transfer files between remote machines. The scp utility provides a simple means to transfer one or many files between machines, leveraging the security provided by SSH. However, if the transfer is interrupted, progress is not saved, and the transfer must be started over from the beginning.

See the following instructions on how to use SCP: `File Upload by scp and rsync <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253365-file-upload-by-scp-and-rsync>`_.

**Note:** If needed, users can check the integrity of their file transfer after completion. See the following instructions: `Verifying Integrity of File Transfers <https://colosseumneu.freshdesk.com/en/support/solutions/articles/61000253379-verifying-integrity-of-file-transfers>`_.

Verifying Container Permissions
-----------------------------

After uploading your container to your team's network storage, from the File Proxy, be sure that file permissions are appropriately set for container import. Permissions should be set to '755' to allow the SRN controller to properly import and load the container.

.. code-block:: bash

    ~$ ssh file-proxy
    user@file-proxy:~$ cd /share/nas/team-name/images/
    user@file-proxy:/share/nas/team-name/images/$ ls -l
    -rw------- 1 user        team-name        493476851 May 23 17:45 my-container-v0.tar.gz
    user@file-proxy:/share/nas/team-name/images/$ chmod 755 my-container-v0.tar.gz
    user@file-proxy:/share/nas/team-name/images/$ ls -l
    -rwxr-xr-x 1 user        team-name        493476851 May 23 17:45 my-container-v0.tar.gz

References
---------

See the man pages for scp and rsync for a description of the various options available for these utilities:

.. code-block:: bash

    man scp
    man rsync
