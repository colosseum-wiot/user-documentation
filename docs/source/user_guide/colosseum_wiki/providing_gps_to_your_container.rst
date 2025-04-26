Providing GPS to your Container
============================

:Created: 2020-03-31T14:59:18-04:00
:Updated: 2020-03-31T14:59:18-04:00

:Tags: GPS, FD_V2_537243 Import

Purpose
-------

A Container uses the gpsd libraries to provide itself with a "real-time" mock GPS data feed. To start the GPS data feed in Interactive Mode, use the Colosseum CLI (see 'help gps'). In Batch/Scrimmage Mode, the GPS data feed is automatically started when the Container receives the 'start' signal from the Colosseum.

Prerequisites
------------

To enable GPS capability into your Container, you must do the following:

* Install gpsd version 3.16 or higher.
* Install colosseumcli version 2.2 or higher.

Install gpsd (from source)
~~~~~~~~~~~~~~~~~~~~~~~~~

The gpsd versions on Ubuntu 14.04.x and 16.04.x apt repositories are too old. Therefore, if your Container is on Ubuntu 14.04.x or 16.04.x, you will need to install gpsd from source.

.. code-block:: bash

   sudo apt-get install scons
   git clone https://git.savannah.nongnu.org/git/gpsd.git
   cd gpsd
   scons
   scons check
   sudo scons udev-install

Install/Update Colosseum CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`ColosseumCLI <colosseum_cli>`

Interactive Mode
--------------

During Interactive Mode, you must manually invoke the GPS feed by using the Colosseum CLI. The key CLI commands are: gps start, gps info, and gps stop.

gps start <rfid> <nodeid>
~~~~~~~~~~~~~~~~~~~~~~~

Every GPS feed is tied to a unique input file specified by the RF scenario ID and the RF node ID. For example, if you want to enable the GPS feed for RF scenario ID 1764 (Close Encounters) for Node 8 (Team Green), then you would run 'colosseumcli gps start 1764 8'.

To figure out available RF scenario IDs and their respective RF node ID mappings, see :doc:`Scenarios <scenarios_summary_list>`.

gps info
~~~~~~~

This command simply reports back the ``<rfid>`` and ``<nodeid>`` GPS scenario currently running.

gps stop
~~~~~~

This command stops the GPS scenario currently running.

Quick Check to Verify GPS Feed
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After starting a GPS scenario (via gps start), you can use the cgps utility to see a real-time feed of GPS data. Run 'cgps 127.0.0.1:6000'

If the GPS feed is present, then cgps will display something similar to the output below:

.. code-block:: none

   ┌───────────────────────────────────────────┐┌─────────────────────────────────┐
   │    Time:       n/a                        ││PRN:   Elev:  Azim:  SNR:  Used: │
   │    Latitude:    38.90367499 N             ││   1    01    001    01      N   │
   │    Longitude:   77.00001166 W             ││                                 │
   │    Altitude:   5.682 ft                   ││                                 │
   │    Speed:      n/a                        ││                                 │
   │    Heading:    n/a                        ││                                 │
   │    Climb:      n/a                        ││                                 │
   │    Status:     3D FIX (25 secs)           ││                                 │
   │    Longitude Err:   n/a                   ││                                 │
   │    Latitude Err:    n/a                   ││                                 │
   │    Altitude Err:    +/- 226 ft            ││                                 │
   │    Course Err:      n/a                   ││                                 │
   │    Speed Err:       n/a                   ││                                 │
   │    Time offset:     n/a                   ││                                 │
   │    Grid Square:     FM18lv                ││                                 │
   └───────────────────────────────────────────┘└─────────────────────────────────┘
   {"class":"TPV","device":"/dev/pts/13","mode":3,"lat":38.903668333,"lon":-76.999988333,"alt":0.760,"epv":69.000}
   {"class":"SKY","device":"/dev/pts/13","vdop":3.00,"hdop":3.00,"pdop":3.00,"satellites":[{"PRN":1,"el":1,"az":1,"ss":1,"used":false}]}
   {"class":"SKY","device":"/dev/pts/13","vdop":3.00,"hdop":3.00,"pdop":3.00,"satellites":[{"PRN":1,"el":1,"az":1,"ss":1,"used":false}]}
   {"class":"TPV","device":"/dev/pts/13","mode":3,"lat":38.903663333,"lon":-76.999996667,"alt":3.762,"epv":69.000}
   {"class":"SKY","device":"/dev/pts/13","vdop":3.00,"hdop":3.00,"pdop":3.00,"satellites":[{"PRN":1,"el":1,"az":1,"ss":1,"used":false}]}
   {"class":"SKY","device":"/dev/pts/13","vdop":3.00,"hdop":3.00,"pdop":3.00,"satellites":[{"PRN":1,"el":1,"az":1,"ss":1,"used":false}]}
   {"class":"TPV","device":"/dev/pts/13","mode":3,"lat":38.903636667,"lon":-76.999998333,"alt":0.929,"epv":69.000}
   {"class":"SKY","device":"/dev/pts/13","vdop":3.00,"hdop":3.00,"pdop":3.00,"satellites":[{"PRN":1,"el":1,"az":1,"ss":1,"used":false}]}
   {"class":"SKY","device":"/dev/pts/13","vdop":3.00,"hdop":3.00,"pdop":3.00,"satellites":[{"PRN":1,"el":1,"az":1,"ss":1,"used":false}]}
   {"class":"TPV","device":"/dev/pts/13","mode":3,"lat":38.903675000,"lon":-77.000011667,"alt":1.732,"epv":69.000}

The top portion shows current GPS latitude, longitude, and altitude. And the bottom shows a scrolling-view of the current gpsd JSON-formatted output strings. Some things to note:

* {TPV: lat, lon, and alt} are "fuzzy" coordinates. Meaning the reported coordinates have position error.
* {SKY: vdop, hdop, and pdop} specifies the 95% confidence interval of the position error for longitude, latitude, and altitude; respectively.

.. note::
   The DOP fields in the SKY message is **NOT** your traditional DOP metrics. The Scenario Developers have "overloaded" these DOP fields to store the the 95% confidence interval instead.   

GPS API
------

cgps is a quick utility to visually see the current GPS feed. But in order to use the GPS feed in your programs, you should use the gpsd client-side API. http://www.catb.org/gpsd/client-howto.html The API comes in C, C++, and Python flavors.

Essentially, if the user wants to use the GPS feed while their radio code is running, they would use the gpsd client API to poll 127.0.0.1 port 6000 for incoming TPV and SKY JSON messages. The user will then parse the TPV message for lat/lon/alt and parse the SKY message for vdop/hdop/pdop (reminder: reported dop is not actual dop numbers, but are the 95% confidence interval error). 

.. note::
   For the GPS Python API, we recommend using https://pypi.python.org/pypi/gps3.

Batch/Scrimmage Mode
------------------

During Batch/Scrimmage mode, the GPS feed is automatically started when the Colosseum sends the start signal. The Colosseum automatically maps a node's GPS feed by using the RF scenario ID ("RFScenario") and RF node ID ("RFNode_ID") specified in the batch configuration file.