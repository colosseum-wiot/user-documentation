Creating Custom Containers
========================

All user experiments in Colosseum are run in LXC containers. This tutorial guides users on creating their own custom containers to run their experiments in Colosseum. The tutorial starts with an overview of the use of LXC containers in Colosseum. It then describes the high-level process of creating a custom container in a user's local environment and the prerequisites for the same. The tutorial then goes into a detailed demo of the steps of creating a custom LXC container from a baseline container, including downloading the baseline container from file-proxy server, importing it into an image in their local LXD environment, initializing a container from the image and an quick example of installing a simple program in the container. The demo then shows the process of creating an image from the custom container, uploading it back to file-proxy server and making a reservation with this custom image. The tutorial also includes some tips that are useful for users during an interactive reservation, including transferring files back and forth between their SRN and file-proxy server, installing Colosseum CLI and taking a snapshot of their container using Colosseum CLI.

Tutorial video:
~~~~~~~~~~~~~~

.. youtube:: 9n8G7CNU190
   :width: 100%
   :height: 315
   :align: center
   :privacy_mode: yes

List of key topics within the video with timestamps:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `00:00 <https://youtu.be/9n8G7CNU190>`_ - Introduction and Outline
* `01:17 <https://youtu.be/9n8G7CNU190?t=77>`_ - Containers in Colosseum
* `03:49 <https://youtu.be/9n8G7CNU190?t=229>`_ - Prerequisites on your local system
* `05:24 <https://youtu.be/9n8G7CNU190?t=324>`_ - Creating a Custom Container: Overview
* `07:28 <https://youtu.be/9n8G7CNU190?t=448>`_ - Demo: Baseline image on file-proxy server
* `08:57 <https://youtu.be/9n8G7CNU190?t=537>`_ - Demo: Transferring base container image to your local machine
* `11:41 <https://youtu.be/9n8G7CNU190?t=701>`_ - Demo: Importing the base image into local LXD environment
* `13:39 <https://youtu.be/9n8G7CNU190?t=819>`_ - Demo: Initializing a container from the imported image
* `15:15 <https://youtu.be/9n8G7CNU190?t=915>`_ - Demo: Starting the container and installing sample program
* `18:02 <https://youtu.be/9n8G7CNU190?t=1082>`_ - Demo: Publishing the custom container into an image
* `19:35 <https://youtu.be/9n8G7CNU190?t=1175>`_ - Demo: Exporting the image into Colosseum-ready tarball
* `20:51 <https://youtu.be/9n8G7CNU190?t=1251>`_ - Demo: Upload the custom image to file-proxy server
* `23:53 <https://youtu.be/9n8G7CNU190?t=1433>`_ - Demo: Making a reservation with the custom image
* `24:26 <https://youtu.be/9n8G7CNU190?t=1466>`_ - Troubleshooting: Internet Access within a container on Local Machine
* `25:39 <https://youtu.be/9n8G7CNU190?t=1539>`_ - Demo: Transferring files between SRN and file-proxy server during an interactive reservation
* `30:38 <https://youtu.be/9n8G7CNU190?t=1838>`_ - Demo: Installing Colosseum CLI
* `36:10 <https://youtu.be/9n8G7CNU190?t=2170>`_ - Demo: Taking a snapshot of your container during an interactive reservation
* `38:20 <https://youtu.be/9n8G7CNU190?t=2301>`_ - Conclusion and helpful links