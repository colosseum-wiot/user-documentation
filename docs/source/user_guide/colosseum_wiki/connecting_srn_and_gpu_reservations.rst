Connecting SRN and GPU Reservations
=================================

:Created: 2023-05-11T16:52:20-04:00
:Updated: 2023-05-11T16:52:20-04:00

:Tags: GPUs, LXC, Docker

This guide helps Colosseum users to allow communication between an SRN reservation (LXC container) and a GPU reservation (Docker container).

Prerequisites
------------

Perform a reservation comprising at least 1 SRN and 1 GPU.

Connecting SRN and GPU
---------------------

To allow communication between an SRN node (LXC container) and a GPU node (Docker container), a user needs to manually add the proper route to allow communication between the two containers.

SRN Node
~~~~~~~

The SRN node needs a default gateway to allow the traffic to reach the Docker container of the GPU reservation. The can0 interface is used to route the traffic out from the LXC container toward the Docker one.

The can0 interface information can be seen by running the ifconfig command, which will result in an output similar to the following:

.. code-block:: bash

   # ifconfig can0
   can0      Link encap:Ethernet  HWaddr 00:16:3e:4e:05:68
             inet addr:172.18.1.101  Bcast:172.18.1.255  Mask:255.255.255.0
             inet6 addr: fe80::216:3eff:fe4e:568/64 Scope:Link
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:112 errors:0 dropped:0 overruns:0 frame:0
             TX packets:73 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:11571 (11.5 KB)  TX bytes:9743 (9.7 KB)

The third part of the inet address (**172.18.1.101**) is linked to the team-name and usually assigned dynamically, e.g., in this case 1, while the last part is specific to the used SRN, e.g., in this case, 101.

To allow the traffic toward the GPU reservation, the default gateway route needs to be added. The ip of the gateway to add is taken from the can0 inet addr by using .1 as the last part of the address. The command would have a structure as follows:

.. code-block:: bash

   # route add default gw 172.18.<team>.1

For example, since in this case the considered team is 1, the IP would be 172.18.1.1.

To check if the route has been added correctly, the following command and a similar output should be displayed:

.. code-block:: bash

   # ip r
   default via 172.18.1.1 dev can0

At this point, the GPU reservation should be reachable. A ping test can be performed to validate the connection to the proper GPU server. Due to the current lack of DNS resolution, the IP of the GPU server should be retrieved based on the GPU nodes assigned as follows:

* From DGX 1 to DGX 8: **10.100.13.153**
* From DGX 9 to DGX 16: **10.100.13.154**
* From LMN 1 to LMN 6: **10.100.13.152**

For example, if the GPU node reserved is DGX 4, the ping should be done as follows:

.. code-block:: bash

   # ping 10.100.13.153
   PING 10.100.13.153 (10.100.13.153) 56(84) bytes of data.
   64 bytes from 10.100.13.153: icmp_seq=1 ttl=59 time=0.104 ms
   64 bytes from 10.100.13.153: icmp_seq=2 ttl=59 time=0.057 ms
   64 bytes from 10.100.13.153: icmp_seq=3 ttl=59 time=0.075 ms

Finally, the reachability of the GPU reservation can be tested by leveraging the netcat command which allows specifying both an IP address and a port. The port of the reservation can be retrieved on the experiment website (see :doc:`Logging into a GPU <logging_into_a_gpu>`). For example, if the reservation port is 25743, a successful test would be similar to the following:

.. code-block:: bash

   # nc -v 10.100.13.153 25743
   Connection to 10.100.13.153 25743 port [tcp/*] succeeded!
   SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5

This proves that the communication from SRN (LXC) to GPU (Docker) has been established correctly.

GPU Node
~~~~~~~

The GPU reservation should be already all set to communicate with the SRN nodes through the can0 LXC interface.

This can be tested by using the netcat command towards, for example, port 22. The IP of the can0 interface should be retrieved from the SRN node via the ifconfig command, as shown in the previous steps.

For example, if the SRN ip is 172.18.1.101, the test would be similar to the following:

.. code-block:: bash

   # nc -v 172.18.1.101 22
   Connection to 172.18.1.101 22 port [tcp/*] succeeded!
   SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.6

This proves that the communication from GPU (Docker) to SRN (LXC) works correctly.