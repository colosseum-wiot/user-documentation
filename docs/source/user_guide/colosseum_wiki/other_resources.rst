Other Resources
==============

:Created: 2020-03-31T15:00:15-04:00
:Updated: 2020-03-31T15:00:15-04:00

:Tags: FD_V2_537243 Import

Software Defined Radio Resources
-------------------------------

`GNU Radio <http://gnuradio.org/>`_ is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. 

`Liquid DSP <http://liquidsdr.org/>`_ is a free and open-source signal processing library for software-defined radios written in C. Its purpose is to provide a set of extensible DSP modules that do not rely on external dependencies or cumbersome frameworks.

General Programming Resources
---------------------------

C/C++
~~~~~

`C/C++ online reference <http://en.cppreference.com/>`_ for common classes, examples, etc.

`Boost C++ template library <http://www.boost.org/>`_. Like C++'s Standard Template Library on steroids. Sometimes helpful, sometimes painful.

Python
~~~~~~

`Python online documentation <http://docs.python.org/tutorial/>`_

`NumPy <http://www.numpy.org/>`_ and `SciPy <https://www.scipy.org/>`_ libraries for doing scientific computing in Python.

Xilinx FPGA Programming
~~~~~~~~~~~~~~~~~~~~~

The `Xilinx FPGA <http://www.xilinx.com/support/documentation/data_sheets/ds180_7Series_Overview.pdf>`_ resources on each USRP X310 that are part of the Standard Radio Node are available to users to program. Xilinx provides many different tool chains for programming the XC7K410T FPGA. Perhaps the most comprehensive tool is the `Xilinx Vivado <https://www.xilinx.com/products/design-tools/vivado.html>`_ Design Suite.

Xilinx is offering first come first serve vivado licenses to SC2 teams that may not otherwise have access to this or a similar tool chain. Requests for a Vivado Voucher in support of the DARPA Spectrum Collaboration Challenge Program will require an email to be sent to jasonv@xilinx.com, with the appropriate DARPA contact (sc2@darpa.mil) on copy of the email request. Once DARPA contact validates the requesters' participation in the program, they will send a simple response to jasonv@xilinx.com with one word "approved" or "denied".

Xilinx has a list of IP cores in the Intellectual Property section of their website. This list includes those cores available for purchase and those that are bundled with Xilinx design tools. Xilinx is not planning to provide free licenses for any of those cores not bundled freely with their design tools. 

CUDA
~~~~

`CUDA <https://developer.nvidia.com/cuda-zone>`_ is a parallel computing platform and application programming interface (API) model created by Nvidia. It can be used to leverage the highly parallel architecture of GPUs for computation. `Current Documentation <http://docs.nvidia.com/cuda/#axzz4WKeQceu2>`_ links to the developer documentation for NVIDIA CUDA Toolkit 8.0.44

Machine Learning & AI Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Theano <http://deeplearning.net/software/theano/>`_ is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently.

`Google's TensorFlow <https://www.tensorflow.org/>`_ is an open source software library for numerical computation using data flow graphs.

`Keras <https://keras.io/>`_ is a high-level neural networks library, written in Python and capable of running on top of either `TensorFlow <https://www.tensorflow.org/>`_ or `Theano <http://deeplearning.net/software/theano/>`_.

`OpenAI Gym <https://gym.openai.com/>`_ is a toolkit for developing and comparing reinforcement learning algorithms. It supports teaching agents everything from walking to playing games like Pong or Go.

`scikit-learn <http://scikit-learn.org/stable/>`_ is an opensource machine learning toolbox for Python

Hardware Resources
----------------

USRP Hardware
~~~~~~~~~~~

Each Colosseum Standard Radio Node has an `Ettus Research <https://www.ettus.com/>`_ X310 software defined radio with a custom low power UBX daughter card. The easiest way to procure this exact configuration is to contact Ettus Research directly.

SRN Compute Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Colosseum SRN computer specifications can be found here.

Cloud Resources
-------------

`Amazon Web Services <https://aws.amazon.com/>`_ offers cloud storage and computing. Including GPU AWS instances that are particularly well suited to crunching data for machine learning.

Amazon has a `grants program <https://aws.amazon.com/grants/>`_ for researchers driving innovation with cloud computing.  

`Google Cloud <https://cloud.google.com/>`_ offers cloud computing services as well. Perhaps in the near future this will include machines with the `TPU processor <https://cloudplatform.googleblog.com/2016/05/Google-supercharges-machine-learning-tasks-with-custom-chip.html>`_? 

`Microsoft Azure <https://azure.microsoft.com/>`_ also offers a cloud computing services.