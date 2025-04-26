Prepare a New LXC Container for Upload
==================================

:Created: 2020-03-31T14:59:36-04:00
:Updated: 2020-03-31T14:59:36-04:00

:Tags: upload, LXC, FD_V2_537243 Import

Once a user has :doc:`Transferred the Base LXC Image from the NAS <transferring_the_base_lxc_image_from_the_nas>` to their local machine, they can use lxd to run the image, make changes, and export the image for upload to the Colosseum.

Prerequisites
------------

This article assumes that the user has :doc:`Transferred the Base LXC Image from the NAS <transferring_the_base_lxc_image_from_the_nas>` and has the base container stored on their local machine at the path ``/home/localuser/myimages/`` and the filename is ``base-image-name.tar.gz``. Replace these placeholder path and file names as appropriate for your local computer.

The user must also have lxd installed on their local machine and configured appropriately. For a tutorial on this process, users can reference the following article. For additional references on setting up and using the lxd environment, see the References section below.

`<https://insights.ubuntu.com/2016/03/16/lxd-2-0-installing-and-configuring-lxd-212/>`_

Notes
-----

Be sure to follow steps 1 and 2 to ensure that user ids and group ids are appropriately mapped within the container.

Do not export the container as split tarballs. This feature is not supported in the Colosseum. Container filenames must be valid hostnames and therefore should only contain letters, numbers, or dashes ('-'). Container filenames should also be limited to 31 characters.  

Procedure
--------

1. Open the ``/etc/subuid`` file on your local machine with sudo privileges. If not already present, add the following lines to the beginning of the file and save the changes.

   .. code-block:: none

      lxd:100000:65536
      root:100000:65536

2. Make the same change to the ``/etc/subgid`` file if not already made. This will also require sudo privileges.

3. From a terminal window on your local machine, import the container .tar.gz file that you wish to use (do not un-tar this file). Within this command, you can provide an alias for the image that makes it easier to reference.

   .. code-block:: bash

      ~$ lxc image import /home/localuser/myimages/base-image-name.tar.gz --alias base-image-name

4. Verify that the image is available in your lxd image repository. You should see similar output identifying that the image has been imported.

   .. code-block:: bash

      ~$ lxc image list

5. Launch the image using the lxd environment. LXD will assign a random name to this instance of the image. This name is how you will reference the running instance of the image, so replace 'knowing-earwig' as appropriate for your case.

   .. code-block:: bash

      ~$ lxc launch base-image-name
      Creating knowing-earwig
      Starting knowing-earwig
      ~$ 

6. Verify that the image has launched.

   .. code-block:: bash

      ~$ lxc list

7. Enter into the container via a bash shell using the lxc exec command:

   .. code-block:: bash

      ~$ lxc exec knowing-earwig bash
      root@knowing-earwig:~# 

8. Now, modify the image as desired. See the references for more complete documentation of working within LXD.

9. When you are ready to save a copy of your image, exit the bash shell within the container.

   .. code-block:: bash

      root@knowing-earwig:~# exit
      ~$ 

10. Stop the container and verify that the state has changed from 'RUNNING' to 'STOPPED'. This is necessary to safely save the state of your container.

    .. code-block:: bash

       ~$ lxc stop knowing-earwig
       ~$ lxc list

11. Publish the changes of your container to your local image store, using an alias of your choice.

    .. code-block:: bash

       ~$ lxc publish knowing-earwig --alias new-base-image-name
       ~$ 

12. Verify that the published image is in your local lxd image store. You should see an entry for the alias provided in the previous step.

    .. code-block:: bash

       ~$ lxc image list

13. Export the image to the desired path and image name on your local machine.

    .. note::
       Valid filenames consist of **only letters, numbers, and dashes ('-')**. LXD will allow you to save files with invalid filenames which will then fail to run when used on the Colosseum.

    .. note::
       **Do not add .tar.gz** to the filename. This will be added automatically.

    .. note::
       **Do not use split tarballs**. This feature is not supported in the colosseum

    .. code-block:: bash

       ~$ lxc image export new-base-image-name /home/localuser/myimages/my-new-image

14. Verify that a new tarball was added to the expected path.

    .. code-block:: bash

       ~$ ls -l /home/localuser/myimages/
       total 1754848
       -rwxr-xr-x 1 qkw lxd 898475854 Feb 26 17:58 base-image-name.tar.gz
       -rw------- 1 qkw lxd 898477398 Mar  1 11:19 mynewimage.tar.gz

You are now ready to :doc:`Upload an LXC Container <upload_an_lxc_container>`.  

References
---------

The lxd homepage can be found at: `<https://linuxcontainers.org/lxd/>`_.

Also, ubuntu hosts a helpful series of blog posts introducing users to the lxd environment: `<https://insights.ubuntu.com/2016/03/14/the-lxd-2-0-story-prologue/>`_.