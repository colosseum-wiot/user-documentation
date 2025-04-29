Save an Image Snapshot using ColosseumCLI
=======================================

Users can save the state of their image through the :doc:`Colosseum CLI </radio_api_traffic/colosseum_cli>`. This will allow the user to save a new image file to the images directory on the user's team network storage.

To check the existing images, check the network storage folder:

.. code-block:: bash

    root@team-name-srnXXX:~/$ ls /storage/nas/team-name/resources/

To save a snapshot, run the following command.

.. code-block:: bash

    root@team-name-srnXXX:~/$ colosseumcli snapshot image-name-here

A successful saved snapshot will return a message similar to the following:

.. code-block:: json

    {"request": {"path": "team-name", "filename": "image-name-here"}, "status": 200}

.. important::

    ``image-name-here`` has the following restrictions:

    - Only letters, numbers, or hyphen (``-``) may be used
    - The image name must be 32 characters or less 

.. note::

    * This script may take a while to complete, particularly for large image sizes as it involves transferring the image from the SRN to the network storage drive. It could take up to 5-10 minutes or even longer depending on the size of the image, so users must **budget enough time prior to the end of their reservation** to run this script.

    * This script does not check to see if the given filename already exists. **It will overwrite existing files** without notifying the user.
