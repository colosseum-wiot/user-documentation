Collaboration Protocol Heatmap
============================

:Created: 2020-03-31T14:59:10-04:00
:Updated: 2020-03-31T14:59:10-04:00

:Tags: heatmap, collaboration protocol, FD_V2_537243 Import

Introduction
-----------

Many users have asked for a way to determine how to best spend their development effort on the Collaboration Protocol. This page attempts to address that request. 

A script is run once an hour that downloads the heatmap_dialect.json file from the heatmap branch on each user's Collaboration Protocol team mirror page. These files are processed and aggregated into a list of message ids, message names, and the teams that have declared they intend to support that message. This page includes the resulting aggregated data set as a JSON formatted fiie as well as a series of plots to give users a better understanding of which messages are most widely supported. These plots are time stamped with the UTC date and time of the last update. If you see a plot that is more than 2 hours old, please notify the Help Desk. Again, please note that the timestamps are in UTC time.  

If you make an update to your heatmap_dialect.json file, but do not see your changes reflected on this page within two hours, please confirm that you can see your updates in the heatmap branch on your team's Gitlab protocol mirror site. If you see the changes there, check the title of the Full Collaboration Protocol Heatmap plot at the bottom of this page. If everything is working properly, it should read: "0 gitlab request errors, 0 files didn't parse." If the number of gitlab errors is nonzero, the automatic update script had problems communicating with gitlab. There is nothing users can do to cause or fix this issue. If, however, the number of files that didn't parse is nonzero, it may be the case that your update as a syntax error preventing the script from parsing your file properly. Please verify that your file is a valid JSON file by running it through a JSON parser and confirming that there are no errors thrown. 

If the title of the Full Collaboration Protocol Heatmap plot shows no errors, you've confirmed that your updates appear in the Gitlab web interface, and you still don't see your updates in the Collaboration protocol heatmap plots after 2 hours, please contact the helpdesk.  

Heatmap Update Process
---------------------

Teams can signal each other about their intent to support various messages by updating their heatmap_dialect.json file and pushing these updates into their **heatmap** branch in their Collaboration Protocol team mirror site. 

The master branch is set as protected to allow any updates to the collaboration protocol to automatically merge in to each team's mirror site without needing to merge changes in manually. This means that teams cannot edit the master branch on their mirror site. However, all teams should have full control over their heatmap branch. Please note that as new messages are added to the Collaboration Protocol, teams will need to merge these new messages into the heatmap branch as this will not be done automatically. 

The following plots show the top level messages, followed by plots for each top level message will all its descendants, and finally one file containing every message in the protocol. 

Raw JSON Data File
-----------------

The following link points to the raw data used to generate the plots on this page.
(see the heatmap_state.json attached below)

Top Level Collaboration Protocol Messages
---------------------------------------

The following plot shows only the top level messages, which are all direct descendants of the main Collaborate message wrapper. 

.. figure:: /_static/images/heatmap/top_level_heatmap.png
   :alt: Top Level Collaboration Protocol Messages
   :align: center

Hello Message Fields
------------------

.. figure:: /_static/images/heatmap/collaborate.hello.png
   :alt: Hello Message Fields
   :align: center

Informational Declaration Message Fields
--------------------------------------

.. figure:: /_static/images/heatmap/collaborate.informational_declaration.png
   :alt: Informational Declaration Message Fields
   :align: center

Informational Query Message Fields
--------------------------------

.. figure:: /_static/images/heatmap/collaborate.informational_query.png
   :alt: Informational Query Message Fields
   :align: center

Query Denied Message Fields
-------------------------

.. figure:: /_static/images/heatmap/collaborate.query_denied.png
   :alt: Query Denied Message Fields
   :align: center

Invalidate My Declaration Message Fields
--------------------------------------

.. figure:: /_static/images/heatmap/collaborate.invalidate_my_declaration.png
   :alt: Invalidate My Declaration Message Fields
   :align: center

Request Message Fields
--------------------

.. figure:: /_static/images/heatmap/collaborate.request.png
   :alt: Request Message Fields
   :align: center

Counter Message Fields
--------------------

.. figure:: /_static/images/heatmap/collaborate.counter.png
   :alt: Counter Message Fields
   :align: center

Agree Message Fields
------------------

.. figure:: /_static/images/heatmap/collaborate.agree.png
   :alt: Agree Message Fields
   :align: center

Claim Message Fields
------------------

.. figure:: /_static/images/heatmap/collaborate.claim.png
   :alt: Claim Message Fields
   :align: center

Confirm Message Fields
--------------------

.. figure:: /_static/images/heatmap/collaborate.confirm.png
   :alt: Confirm Message Fields
   :align: center

Withdraw Message Fields
---------------------

.. figure:: /_static/images/heatmap/collaborate.withdraw.png
   :alt: Withdraw Message Fields
   :align: center

Full Collaboration Protocol Heatmap
---------------------------------

This image contains every message in the protocol in a single plot.

.. figure:: /_static/images/heatmap/full_heatmap.png
   :alt: Full Collaboration Protocol Heatmap
   :align: center