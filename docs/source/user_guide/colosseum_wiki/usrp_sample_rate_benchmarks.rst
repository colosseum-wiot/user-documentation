USRP Sample Rate Benchmarks
=========================

**Created:** 2020-03-31T14:59:16-04:00  
**Updated:** 2020-03-31T14:59:16-04:00  

**Tags:** benchmarks, benchmark, UHD, USRP, USRPs, FD_V2_537243 Import

Content
-------

This page provides information as to the sample rates users can expect to achieve using the USRPs attached to the Colosseum SRNs.

UHD Benchmarks
------------

These tests were conducted using the UHD benchmark_rate utility. The results should not be taken as conclusive but as representative of actual Colosseum SRN/USRP performance during the limited test time. All testing was conducted using the base5nocuda container on a single production SRN. Thread priority was not enabled. Each test run lasted for 30 seconds and the results are an average of multiple runs with decimals rounded.

+------------+----------------+----------------+---------------------------------------------+
| Channel(s) | TX Rate (Msps) | RX Rate (Msps) | Results                                     |
+============+================+================+=============================================+
| 0          | 0              | 100            | RX samples: 2999977831                      |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 0                               |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 0                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0          | 0              | 200            | RX samples: 5999930413                      |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 0                               |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 0                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0,1        | 0              | 100            | RX samples: 5995516126                      |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 0                               |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 0                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0          | 100            | 0              | RX samples: 0                               |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 3000103768                      |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 0                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0          | 200            | 0              | RX samples: 0                               |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 6000085774                      |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 3                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0,1        | 100            | 0              | RX samples: 0                               |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 6000163624                      |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 8                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0          | 100            | 100            | RX samples: 3000657769                      |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 3000091792                      |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 0                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0          | 200            | 200            | RX samples: 6001315041                      |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 6000069812                      |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 1                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+
| 0,1        | 100            | 100            | RX samples: 6010272962                      |
|            |                |                | Dropped samples: 0                          |
|            |                |                | Overflows: 0                                |
|            |                |                | TX samples: 6000195560                      |
|            |                |                | Sequence errors: 0                          |
|            |                |                | Underflows: 3                               |
|            |                |                | Late commands: 0                            |
|            |                |                | Timeouts: 0                                 |
+------------+----------------+----------------+---------------------------------------------+

While these results should not be taken as conclusive, the SRN/USRP seemed to perform as expected with minimal discontinuities when pushing the boundary of the maximum sample rates. Individual results may vary. These tests were repeated using a basic GNURadio flowgraph with similar results observed.
