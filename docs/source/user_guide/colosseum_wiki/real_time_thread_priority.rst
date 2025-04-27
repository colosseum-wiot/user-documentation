Real Time Thread Priority
=======================

**Created:** 2020-03-31T14:59:34-04:00  
**Updated:** 2020-03-31T14:59:34-04:00  

**Tags:** real time priority, rtprio, FD_V2_537243 Import

Content
-------

Real time priority scheduling is now enabled in the SRN containers. There are two key changes that users should be aware of:

- Real time will only work for processes run as a child process of the init daemon within the container or from an SSH session. Users should note that RadioAPI scripts such as start.sh will not be able to spawn child processes with real time priority.
- Two CPU cores are now held in reserve for the SRN host system, so containers will have access to the remaining 46 CPU cores.

Below are some examples for working with real time priority within your container:

- To run something with real time priority:

.. code-block:: bash

    chrt 50 echo "RTPRIO works"

- To print rtprio limits:

.. code-block:: bash

    prlimit -r

Expected output:

.. code-block:: bash

    RESOURCE DESCRIPTION SOFT HARD UNITS
    RTPRIO max real-time priority 99 99

- To set the priority of a running process:

.. code-block:: bash

    chrt -p <priority> <pid>

- To check the priority of a running process:

.. code-block:: bash

    chrt -p <pid>

For more information on running processes with real time priority, see the Linux man pages for chrt and prlimit.
