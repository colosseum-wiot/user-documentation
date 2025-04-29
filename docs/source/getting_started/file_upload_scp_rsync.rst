File Upload by scp and rsync
==========================

By scp
------

The secure copy (scp) utility is useful for transferring small files between a user's local environment and the Colosseum network storage. For large files, users are encouraged to use rsync.

Prerequisites
~~~~~~~~~~~~

These instructions require that the user has modified their SSH config file per the `SSH Proxy Setup </getting_started/ssh_proxy_setup>` instructions. This will allow the user to transfer files directly to the network storage directory from their local environment.

The user should also have verified the path of their team folder and that it is accessible on the File Proxy by the instructions for `Accessing Colosseum Resources </getting_started/accessing_colosseum_resources>`.

Using scp
~~~~~~~~~

The scp utility can be used to transfer files either to a remote directory or from a remote directory. The format of the scp command is very similar to the cp command:

.. code-block:: bash

    ~$ scp <from-location> <to-location>

When specifying a remote directory as either the from-location or to-location, that directory must be prefixed with the host name and the username used to log into that host. In this example, a file is being transferred from the current directory on a local machine to the 'other' folder on the network storage for a user's team:

.. code-block:: bash

    ~$ scp ./best_radio_code.c username@file-proxy:/share/nas/the-winning-team/other/

Also, similar to cp, multiple files may be transferred using single directories may be specified instead of individual files the wildcard character (*) may be used to select multiple matching files

Required File Permissions for Containers on the NAS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Don't forget to update the file permissions for new containers on the NAS as described at the bottom of `Upload an LXC Container </container_mgmt/upload_lxc_container>`

References
~~~~~~~~~~

See the man page for scp for a full description of its operation and options:

.. code-block:: bash

    man scp

By rsync
--------

As part of the development and deployment process, users will need to transfer very large files over the Internet to their file storage directories on the Colosseum NAS. In order to efficiently transfer files onto the NAS, users are encouraged to make use of the rsync utility, which can be found on most UNIX-based systems. Rsync allows a user to transfer files between a local host and a remote host efficiently by only transferring changes to the files between the hosts.

In the case of very large file transfers, such as LXC containers, any loss of connection between the user local host and the Colosseum remote host may terminate the file transfer. Rsync provides a command line option, -P, to preserve the partial file and resume the transfer when the command is re-run.

Prerequisites
~~~~~~~~~~~~

These instructions require that the user has modified their SSH config file per the `SSH Proxy Setup </getting_started/ssh_proxy_setup>` instructions. This will allow the user to transfer files directly to the network storage directory from their local environment.

The user should also have verified the path of their team folder and that it is accessible on the File Proxy by the instructions for `Accessing Colosseum Resources </getting_started/accessing_colosseum_resources>`.

Example Usage
~~~~~~~~~~~~

In both of the examples presented here, the -P command line argument is used to indicate to rsync that partial files should be preserved in the event of a failure. This will allow rsync to resume the file transfer.

Single File Transfer
^^^^^^^^^^^^^^^^^^^

In this example, a user has a single file (e.g., an LXC container) that they wish to transfer to a remote directory path on the Colosseum NAS.

.. code-block:: bash

    rsync -vP -e ssh /local/path/mycontainer.tar.gz username@file-proxy:/share/nas/the-winning-team/resources/

In this example, the components of the command line are:

* ``-v``: run rsync in verbose mode
* ``-P``: shortcut argument for ``--partial`` and ``--progress``, which indicate:

    * ``--partial``: partial file transfers should be retained
    * ``--progress``: display file transfer progress on the command line

* ``-e ssh``: use ssh as the remote shell
* /local/path/mycontainer.tar.gz: the local path and file to transfer
* username: the user's username on the Colosseum
* file-proxy: the hostname of the File Proxy server, or the fully-qualified domain name or IP address of the remote server which is the destination of the upload
* /share/nas/the-winning-team/resources/: the path on the remote system to where the local directory will be transferred -- in this case, the images directory

If this transfer fails due to an interrupted connection, simply rerun the same command until the transfer completes.

Recursive Directory Transfer
^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, a user has a local directory with large files that they wish to transfer to a remote directory on the Colosseum NAS.

.. code-block:: bash

    rsync -avP -e ssh /local/path/ username@file-proxy:/share/nas/the-winning-team/resources/

In this example, the components of the command line are:

* ``-a``: use archive settings, which includes recursion and preserves almost everything (see rsync man page for details)
* ``-v``: run rsync in verbose mode
* ``-P``: shortcut argument for ``--partial`` and ``--progress``, which indicate:

    * ``--partial``: partial file transfers should be retained
    * ``--progress``: display file transfer progress on the command line

* ``-e ssh``: use ssh as the remote shell
* /local/path/: the local directory to be transferred and mirrored to the remote host
* username: the user's username on the Colosseum
* file-proxy: the hostname of the File Proxy server, or the fully-qualified domain name or IP address of the remote server which is the destination of the upload
* /share/nas/the-winning-team/resources/: the path on the remote system to where the local directory will be transferred -- in this case, the images directory

If this transfer fails due to an interrupted connection, simply rerun the same command until the transfer completes.

Required File Permissions for Containers on the NAS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Don't forget to update the file permissions for new containers on the NAS as described at the bottom of `Upload an LXC Container </getting_started/upload_lxc_container>`

References
~~~~~~~~~~

For full documentation on rsync including operation details and command line options, please see either the man page for rsync or the rsync web page at `https://rsync.samba.org <https://rsync.samba.org/>`_.
