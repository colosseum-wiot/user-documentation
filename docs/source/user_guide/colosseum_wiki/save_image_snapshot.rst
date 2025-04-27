Save an Image Snapshot using ColosseumCLI
=======================================

**Created:** 2020-03-31T14:59:17-04:00  
**Updated:** 2020-03-31T14:59:17-04:00  

**Tags:** snapshot, CLI, FD_V2_537243 Import

Content
-------

Users can save the state of their image through the `Colosseum CLI <https://sc2colosseum.freshdesk.com/solution/articles/22000220365-colosseum-cli>`_. This will allow the user to save a new image file to the images directory on the user's team network storage.

To check the existing images, check the network storage folder:

.. code-block:: bash

    root@team-name-srnXXX:~/$ ls /storage/nas/team-name/images/

To save a snapshot, run the following command.

.. code-block:: bash

    root@team-name-srnXXX:~/$ colosseumcli snapshot image-name-here

A successful saved snapshot will return a message similar to the following:

.. code-block:: json

    {"request": {"path": "team-name", "filename": "image-name-here"}, "status": 200}

**Important**: image-name-here has the following restrictions:

- Only letters, numbers, or hyphen ('-') may be used
- The image name must be 32 characters or less 

**Note**: This script may take a while to complete, particularly for large image sizes as it involves transferring the image from the SRN to the network storage drive. It could take up to 5-10 minutes or even longer depending on the size of the image, so users must **budget enough time prior to the end of their reservation** to run this script.

**Note**: This script does not check to see if the given filename already exists. **It will overwrite existing files** without notifying the user.
