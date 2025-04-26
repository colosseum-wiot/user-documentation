GPUs of an SRN
============

:Created: 2020-03-31T14:59:34-04:00
:Updated: 2020-03-31T14:59:34-04:00

:Tags: GPU, cuda, nvidia, GPUs, FD_V2_537243 Import

Prerequisites
------------

This guide covers interaction with the GPUs of a single SRN with the default base container image. Any customization to the container image by the user may change the instructions provided here.

GPU Permissions
--------------

As of release v2.2.3, users now have permissions to modify GPU settings using nvidia-smi and to profile code with nvprof. For information on using these utilities, please see the Nvidia CUDA documentation.

Verifying the CUDA Environment
----------------------------

By default, the NVIDIA CUDA software repository is installed on the CUDA-enabled base image as described in the CUDA Quick Start Guide. This base image also has the appropriate environment variables configured in the ~/.bashrc file of the root directory. To verify the variables are set correctly, run:

.. code-block:: bash

   root@team-image-srn:~# echo $PATH | grep cuda
   /usr/local/**cuda**-8.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
   
   root@team-image-srn:~# echo $LD_LIBRARY_PATH | grep cuda
   /usr/local/**cuda**-8.0/lib64

If neither command returns output, this likely means that the environment variables are not being properly set in the .bashrc file. Open the .bashrc file using vi or your favorite text editor:

.. code-block:: bash

   vi ~/.bashrc

Add the following lines to the end of the file:

.. code-block:: bash

   export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}} 
   export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64  ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

Reload your .bashrc file in your current terminal:

.. code-block:: bash

   root@team-image-srn:~# source ~/.bashrc

These changes will take effect for each subsequent terminal session.

Running the NVIDIA CUDA Examples
------------------------------

By default, the CUDA Examples provided by NVIDIA are not installed. To install them to your home directory, run:

.. code-block:: bash

   root@team-image-srn:~# cuda-install-samples ~/

To test the CUDA build environment, you can build and run an example by:

.. code-block:: bash

   root@team-image-srn:~# cd NVIDIA_CUDA-8.0_Samples/0_Simple/matrixMul/
   root@team-image-srn:~/NVIDIA_CUDA-8.0_Samples/0_Simple/matrixMul/# make
   root@team-image-srn:~/NVIDIA_CUDA-8.0_Samples/0_Simple/matrixMul/# ./matrixMul
   [Matrix Multiply Using CUDA] - Starting...
   GPU Device 0: "Tesla K40m" with compute capability 3.5
   
   MatrixA(320,320), MatrixB(640,320)
   Computing result using CUDA Kernel...
   done
   Performance= 346.97 GFlop/s, Time= 0.378 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
   
   Checking computed result for correctness: Result = PASS
   
   NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
   root@team-image-srn:~/NVIDIA_CUDA-8.0_Samples/0_Simple/matrixMul/# 

Similar output to the terminal indicates that the example code successfully compiled and executed.

NVIDIA CUDA Development
---------------------

For more information on software development using CUDA, see the References section below.

References
---------

NVIDIA CUDA Quick Start Guide: `<https://developer.nvidia.com/compute/cuda/8.0/Prod2/docs/sidebar/CUDA_Quick_Start_Guide-pdf>`_

See Section 4.1.5.1 for instructions for the Debian Installer in Ubuntu.

NVIDIA CUDA Toolkit Developer Information: `<https://developer.nvidia.com/cuda-toolkit>`_