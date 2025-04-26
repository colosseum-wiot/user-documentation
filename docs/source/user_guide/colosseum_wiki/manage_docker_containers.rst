Manage Docker Containers
========================

:Created: 2022-07-20T11:21:51-04:00
:Updated: 2022-07-20T11:21:51-04:00

:Tags: Docker, Container, upload, manage

Users can manage their Docker containers on the Experiments website from its `Images page <https://experiments.colosseum.net/images>`_. Users must upload their Docker containers to the Colosseum Docker Registry to be able to use them in a GPU reservation. Each team has access to a team-specific sub-registry on the Colosseum Docker Registry server. From this page, a user is able to perform the following operations:

* Push a new image from the NAS to the Colosseum Docker Registry ready to be used.
* Commit an active reservation container into an image and save it into the Colosseum Docker Registry.
* Export an image from the Colosseum Docker Registry to the NAS.
* Delete an image from the Colosseum Docker Registry.

Prerequisites
------------

In order to access the File Proxy server, users must have already :doc:`Uploaded SSH Public Keys <upload_ssh_public_keys>`.  

**The user MUST have their ssh client configured per the** :doc:`SSH Proxy Setup <ssh_proxy_setup>` **instructions.**

Docker Image Requirements
-----------------------

In order to correctly use a Docker Image in the Colosseum environment, the following requirements should be addressed and satisfied:

* OpenSSH-Server needs to be installed (See Troubleshooting for more information).
* An additional user, besides the root user, needs to be created and configured to be able to ssh into the container, or the root user needs to be explicitly set (See Troubleshooting for more information).
* Users can also start the Docker image creation from tested Dockerfiles in Colosseum by leveraging the following repository: `<https://github.com/colosseum-wiot/colosseum-dockerfiles>`_.

Push a new image
--------------

In this subsection, users are able to push a new image from the NAS to the Colosseum Docker Registry. In this way, the pushed image can be selected and used during a reservation.

Users are encouraged to verify that the container operates appropriately before uploading to the Colosseum. At minimum the container must be accessible via **SSH** to be used during an interactive session. Therefore, openssh-server needs to be installed correctly (see troubleshooting for more information).

Users should use the Docker Save command to export the image that needs to be pushed. The name of the image should be in the following format: "your-name.tar.gz".

In order to push a new image, a user should follow these steps:

1. Copy the image to be uploaded in the Network Attached Storage (NAS) in the user's team directory "push-images". The image can be exported `using docker save on your local machine. <https://docs.docker.com/engine/reference/commandline/save/>`_ A user can use scp or rsync to upload the image by following the instruction in :doc:`File Upload by scp and rsync <file_upload_by_scp_and_rsync>`. Verify that the image has been successfully copied and that it has the proper permissions set to '755', as shown in the troubleshooting section at the of this guide. As an example, with *scp* the command should be similar to this:

   .. code-block:: bash

      ~$ scp <image-name>.tar.gz @file-proxy:/share/nas/<teamname>/push-images/

2. Go to the `experiments images tab <https://experiments.colosseum.net/images>`_, and select the image that needs to be pushed from the drop-down menu. If the image is not present, try to refresh the page.

3. Choose a name and a tag for the image to be pushed into the Colosseum Docker Registry. The correct format of the name should be: image-name:tag. If no tag is specified, the image will be uploaded with the "latest" tag. Allowed special characters are "_-".

4. Press the button "Push" to start the pushing process from the NAS to the Colosseum Docker Registry.

5. If the image is pushed correctly, a successful green message will appear, and the .tar.gz file in the NAS will be deleted.

If the push image encounters an error, a red message will tell the user the issue. If the user is not able to resolve the error, please, open a new ticket on FreshDesk with the red message displayed.

Commit an image
-------------

With this feature, a user can save the current status of a running Docker container of an active reservation by committing a new image into the Colosseum Docker Registry. The committed image can then be used in a new GPU reservation, or exported in the NAS with the Export feature explained below.

This feature is similar to the colosseumcli snapshot used to save an LXC container, as shown in :doc:`Save an Image Snapshot using ColosseumCLI <save_an_image_snapshot_using_colosseumcli>`. If a user wants to save both the Docker and LXC containers, he should perform the saving operations separately, i.e. by using the Commit feature for Docker, and the colosseumcli snapshot for LXC.

In order to commit a Docker image, a user should perform these steps:

1. Select the active reservation to commit from the drop-down menu. The menu will show all current active GPU reservations of their team in the format: "<reservation name> - id: <id>".

2. Choose a name and a tag for the image to be committed into the Colosseum Docker Registry. The correct format of the name should be: image-name:tag. If no tag is specified, the image will be uploaded with the "latest" tag. Allowed special characters are "_-".

3. Press the button "Commit" to start the committing process.

4. A successful green message will be displayed when the committing process has been terminated. The image should now be ready to be used in a new reservation or to be exported in the NAS.

If the commit image encounters an error, a red message will tell the user the issue. If the user is not able to resolve the error, please, open a new ticket on FreshDesk with the red message displayed.

Export an image
-------------

In this subsection, a user is able to export an image from the Colosseum Docker Registry to the NAS team folder in the 'exported-images' directory in an archive file. In this way, a user can copy the image from the Colosseum environment to their own computer. From the NAS, a user is able to copy the archived image to their own device by using for example scp or rsync.

In order to export an image, a user should follow the following instructions:

1. Select the image to export from the drop-down menu. The menu will show all images in the registry for the user's team, together with the common ones.

2. Choose a name for the exported image to be saved in the NAS.

3. Press the button "Export" to start the exporting process. The image will be exported in a tar archive with the format name: "<image-name>.tar.gz". A successful green message will notify the user that the process has been completed correctly.

4. (Optional) Copy the docker .tar.gz archive image to your device. This step is optional, and allows the user to copy the image to their device by using, for example, *scp* or *rsync*. The image is located in the 'exported-images' directory in the user's team folder. As an example, with *scp* the command should be similar to this:

   .. code-block:: bash

      ~$ scp <username>@file-proxy:/share/nas/<teamname>/exported-images/<image-name>.tar.gz <local-path>

Delete an image
-------------

With this feature, a user can delete an image from the Colosseum Docker Registry. A user can only delete the images of their own team. The deletion of the image is **permanent** and cannot be reverted.

In order to delete an image, a user should perform these steps:

1. Select the image to delete from the drop-down menu. The menu will show all images in the registry for the user's team.

2. Press the button "Delete" to start the deletion process. A successful green message will notify the user that the process is completed.

Once deleted, an image cannot be recovered, and cannot be used in any reservation or exported in any case.

Troubleshooting
-------------

Install openssh
~~~~~~~~~~~~~

For a container to be accessible in ssh during a reservation, openssh needs to be installed. When a container starts, the entrypoint command that will be run is: entrypoint = ["/usr/sbin/sshd", "-D"].

Openssh can be installed by running the following commands:

.. code-block:: bash

   ~$ sudo apt-get install openssh-server
   ~$ ssh-keygen -A
   ~$ mkdir -p /run/sshd

Create a new user or set ssh via root
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to ssh into the reservation, at least one additional user, besides the root user, needs to be created and configured which will be used to log in into the reservation, or, alternatively, Alternatively, the root user needs to be explicitily set to allow ssh via it. This because, by default, *openssh-server* does not allow ssh authentications with the root user. 

An additional user can be created with the following commands:

.. code-block:: bash

   ~$ useradd -m -s /bin/bash new-user
   ~$ usermode -aG sudo new-user
   ~$ passwd new-user

The first command create the user; the second grants the user admin privileges; the third sets the password for the new user.

To allow ssh via the root user, the following line can be used:

.. code-block:: bash

   ~$ sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

Uploading an LXC Container to the Colosseum File Proxy Server
-----------------------------------------------------------

The Colosseum reservation system checks a specific directory in each team's network attached storage space for containers to use in reservations. Containers must be uploaded to ``/share/nas/<teamname>/images/`` to be available to the team when making a reservation.

Users may use one of the following tools to upload their container. 

Rsync
~~~~~

The rsync utility provides a means to synchronize folder content between a local and remote host. The rsync utility inspects the content in each folder, identifies the differences in that content, and reconciles those differences by transferring the file differences. Using rsync requires a more command operation configuration, but the utility is a bit more flexible than scp and users may find it useful. Additionally, with proper configuration, rsync will allow the user to resume incomplete or partial transfers.

See the following instructions on how to use rsync: :doc:`File Upload by scp and rsync <file_upload_by_scp_and_rsync>` 

.. note::
   rsync has the capability to remove files on either the remote or local folder as part of the reconciliation operation. If users are unfamiliar with rsync, it is recommended that they test its use on local folders which do not contain critical data. Colosseum Administrators may not be able to recover data accidentally lost.

Secure Copy (SCP)
~~~~~~~~~~~~~~~

Secure copy is a version of the unix copy (cp) command that uses the SSH protocol to transfer files between remote machines. The scp utility provides a simple means to transfer one or many files between machines, leveraging the security provided by SSH. However, if the transfer is interrupted, progress is not saved, and the transfer must be started over from the beginning.

See the following instructions on how to use SCP: :doc:`File Upload by scp and rsync <file_upload_by_scp_and_rsync>`.

.. note::
   If needed, users can check the integrity of their file transfer after completion. See the following instructions: :doc:`Verifying Integrity of File Transfers <verifying_integrity_of_file_transfers>`.

Verifying Image Name
~~~~~~~~~~~~~~~~~

An image name should be less than 30 characters long, and should only container the following special characters: "-" and "_".

If the image is not showing on the drop-down menu, please double-check the name and refresh the website page.

Verifying Container Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After uploading your container to your team's network storage, from the File Proxy, be sure that file permissions are appropriately set for container import. Permissions should be set to '755' to allow the system controller to properly import and load the container.

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