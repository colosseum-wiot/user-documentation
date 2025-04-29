Transferring the Base LXC Image from the NAS
========================================

With access to the SSH Gateway and File Proxy server, it is possible to access the base container images and copy them from Colosseum to your local machine.

Prerequisites
------------

Users should have already:

- Uploaded their SSH public key to their account following the instructions in `Uploaded SSH Public Keys <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253402-upload-ssh-public-keys>`_.
- Configured their ssh config following the instructions in `SSH Proxy Setup <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253369-ssh-proxy-setup>`_.
- Be able to access the File Proxy server within the Colosseum following the instructions in `Accessing Colosseum Resources <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253362-accessing-colosseum-resources>`_.

Procedure
--------

1. SSH into the File Proxy server in order to verify the path and file name of the base image you wish to transfer. See `Accessing Colosseum Resources <https://colosseumneu.freshdesk.com/support/solutions/articles/61000253362-accessing-colosseum-resources>`_ for more detail on how to access the File Proxy.

   .. code-block:: bash

       ~$ ssh file-proxy
       Password:
       user@file-proxy:~$

2. Check the contents of the /share/nas/common/ directory. This is where the common base container images are stored. There should be one image indicating there is no cuda and one indicating that there is cuda (this one will have NVIDIA CUDA package installed). The numbers in the image name specify the version of Ubuntu that image corresponds to. For example, base-1604-nocuda.tar.gz is an Ubuntu 16.04 image. It is recommended to use the image with the latest version number. Make note of the filename (including the .tar.gz ending).

   .. code-block:: bash

       user@file-proxy:~$ ls -l /share/nas/common/
       total 9429444
       -rwxr-xr-x 1 armory-user sc2-group 898543811 Feb 27 23:52 base-1604-nocuda.tar.gz
       -rwxr-xr-x 1 armory-user sc2-group 7820838925 Feb 28 01:01 base-1604-cuda.tar.gz

3. Open a new terminal window from your local terminal. Transfer the desired image using its filename and path on the file-proxy server to a folder on your local machine using rsync or scp (see :doc:`File Upload by rsync and scp <file_upload_scp_rsync>`). Rysnc is recommended for large file transfers.

   .. code-block:: bash

       ~$ rsync -vP -e ssh user@file-proxy:/share/nas/common/base-1604-cuda.tar.gz /home/localuser/myresources/

4. You can verify that the file transfer completed successfully by following the instructions to :doc:`Verify Integrity of File Transfers <verifying_integrity>`.