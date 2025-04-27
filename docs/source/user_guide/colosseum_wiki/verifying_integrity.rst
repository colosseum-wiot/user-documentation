Verifying Integrity of File Transfers
=================================

**Created:** 2020-03-31T14:59:17-04:00  
**Updated:** 2020-03-31T14:59:17-04:00  

**Tags:** file transfer, integrity, verify, verification, FD_V2_537243 Import

Content
-------

Most unix-based systems provide several command-line utilities for computing hashes of files. These hashes can be used to verify file integrity by calculating the hash value before and after the file transfer.

Some commonly-available hash function utilities on unix-based systems:

- md5sum (or md5 on Mac OSX)
- shasum
- sha256sum (or shasum -a 256 on Mac OSX)

Any of these options should suffice for a basic file integrity check.

These commands all share a common syntax:

On the user's local machine, compute the hash:

.. code-block:: bash

    ~$ shasum my_container.lxc
    f1925f822c5ae7b6df5bc8354a2d8534c64fbcd1  my_container.lxc

Compute the hash of the uploaded file:

.. code-block:: bash

    user@file-proxy:~$ shasum my_container.lxc
    f1925f822c5ae7b6df5bc8354a2d8534c64fbcd1  my_container.lxc

References
---------

See the man pages of each command for more information:

.. code-block:: bash

    man md5sum (or man md5 on Mac OSX)
    man shasum
    man sha256sum
