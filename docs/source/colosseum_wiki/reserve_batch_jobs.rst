Reserve Batch Jobs Without Using the Reservation Website
=====================================================

This page provides an overview of manipulating your team's Colosseum reservations without having to use the Colosseum website. A benefit of this approach is it allows a user to script job executions through their own scheduler. For example, automated batch job scheduling-and-execution of jobs during off-peak hours.

The following actions are available:

- Query by Reservation ID
- Query Batch Files List
- Query Completed/Pending/Active Batch List
- Select and Queue a Batch Job
- Delete a Reservation

**IMPORTANT SECURITY NOTE**

- Always use HTTPS. Otherwise, your username and password will be sent over the Internet in cleartext.
- When specifying "-u username", curl will prompt you to enter your password. This has the advantage of hiding your password on the local machine (e.g., your password will not appear in your Terminal's 'history'). If you do not care for this, then you can specify "-u username:password" which will immediately run the curl command without prompting for password.
- All curl commands are restricted for your team only (via LDAP group membership). In other words, a user cannot execute commands for other teams.

Query by Reservation ID
----------------------

View reservation details by reservation ID.

.. code-block:: bash

    curl -k -u username "https://experiments.colosseum.net/api/v1/reservations/ID"

Example
~~~~~~~

.. code-block:: bash

    curl -k -u username "https://experiments.colosseum.net/api/v1/reservations/57291"

Produces the following output...

.. code-block:: json

    [
      {
        "res_status": "Active",
        "start": 1537363800.0,
        "team_name": "apl-test-team-1",
        "name": "dsrc",
        "competitor_id": "yimkj1",
        "nodes": [
          {
            "lxcstatus": "Dead",
            "status": "Ready",
            "srn_id": 1,
            "image": "incumbent-dsrc-v1-1b"
          },
          {
            "lxcstatus": "Dead",
            "status": "Ready",
            "srn_id": 2,
            "image": "incumbent-dsrc-v1-1b"
          }
        ],
        "reservation_type": 1,
        "res_id": "57291",
        "scenario_start_time": 0.0,
        "end": 1537399800.0,
        "duration": 36000.0
      }
    ]

Note: the lxcstatus field is not used, and will always report "Dead".

Query Batch Files List
---------------------

View all available batch jobs. Note: this does not list pending/active batch jobs.

.. code-block:: bash

    curl -k -u username "https://experiments.colosseum.net/api/v1/batch/files/"

Example
~~~~~~~

.. code-block:: bash

    curl -k -u username "https://experiments.colosseum.net/api/v1/batch/files/"

Produces the following output...

.. code-block:: json

    {
      "Batch List": [
        {
          "res_name": "sys-test-test",
          "num_srns": 5,
          "name": "exp-1.json"
        },
        {
          "res_name": "incumbent-passive-2",
          "num_srns": 2,
          "name": "incumbent-passive-2.json"
        },
        {
          "res_name": "incumbent-passive-1-2222",
          "num_srns": 51,
          "name": "incumbent-passive-50-2222.json"
        },
        {
          "res_name": "system-test-128.json",
          "num_srns": 128,
          "name": "system-test-129.json"
        }
      ]
    }

Query Completed/Pending/Active Batch List
----------------------------------------

Get a list of all active, pending, and completed batch jobs within a specified time window.

.. code-block:: bash

    curl -k -u <username> "https://experiments.colosseum.net/api/v1/batch/jobs/?start_time=<start_time_epoch>&stop_time=<stop_time_epoch>"

Note: epoch refers to unix epoch time. To determine unix epoch time, use https://www.epochconverter.com/.

Example
~~~~~~~

.. code-block:: bash

    curl -k -u <username> "https://experiments.colosseum.net/api/v1/batch/jobs/?start_time=1537391100&stop_time=1537883000"

Produces the following output...

.. code-block:: json

    {
      "complete": [
        {
          "expire_time": 999999999.0,
          "token_cost": 0,
          "file_name": "system-test-1033-ram.json",
          "reservation_info": [
            {
              "rf_ready": true,
              "competitor_id": "berhas1",
              "end": 1537392132.15725,
              "traffic_ready": true,
              "scenario_start_time": 1537391972.63792,
              "res_status": "Complete",
              "duration": 960.0,
              "start": 1537391172.15725,
              "team_name": "apl-test-team-1",
              "nodes": [
                {
                  "lxcstatus": "Dead",
                  "status": "Ready",
                  "srn_id": 9,
                  "image": "system-test-ram"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Ready",
                  "srn_id": 8,
                  "image": "system-test-ram"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Ready",
                  "srn_id": 7,
                  "image": "system-test-ram"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Ready",
                  "srn_id": 6,
                  "image": "system-test-ram"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Ready",
                  "srn_id": 5,
                  "image": "system-test-ram"
                }
              ],
              "srn_ready": true,
              "res_id": "57409",
              "name": "system-test-1033-ram.json"
            }
          ],
          "job_status": "complete",
          "priority": 0,
          "num_srns": 5,
          "num_retries": 0,
          "job_id": 33276,
          "enter_queue_time": 1537391144.00156,
          "max_retries": 5,
          "performer_id": "berhas1"
        }
      ],
      "pending": [
        {
          "expire_time": 999999999.0,
          "num_retries": 0,
          "file_name": "system-test-2",
          "job_id": 33285,
          "token_cost": 0,
          "enter_queue_time": 1537394097.05568,
          "job_status": "queued",
          "priority": 0,
          "max_retries": 5,
          "performer_id": "yimkj1"
        }
      ],
      "active": [
        {
          "expire_time": 999999999.0,
          "token_cost": 0,
          "file_name": "system-test-5",
          "reservation_info": [
            {
              "rf_ready": true,
              "competitor_id": "yimkj1",
              "end": 1537394172.09673,
              "traffic_ready": true,
              "scenario_start_time": 1537393472.60586,
              "res_status": "Active",
              "duration": 1500.0,
              "start": 1537392672.09673,
              "team_name": "apl-test-team-1",
              "nodes": [
                {
                  "lxcstatus": "Dead",
                  "status": "Active",
                  "srn_id": 35,
                  "image": "system-test"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Stopping Container",
                  "srn_id": 34,
                  "image": "system-test"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Stopping Container",
                  "srn_id": 33,
                  "image": "system-test"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Active",
                  "srn_id": 27,
                  "image": "system-test"
                },
                {
                  "lxcstatus": "Dead",
                  "status": "Active",
                  "srn_id": 26,
                  "image": "system-test"
                }
              ],
              "srn_ready": true,
              "res_id": "57415",
              "name": "system-test-5"
            }
          ],
          "job_status": "active",
          "priority": 0,
          "num_srns": 5,
          "num_retries": 0,
          "job_id": 33280,
          "enter_queue_time": 1537392585.3102,
          "max_retries": 5,
          "performer_id": "yimkj1"
        }
      ]
    }

Note: the lxcstatus field is not used, and will always report "Dead".

Select and Queue a Batch Job
---------------------------

This command will select, prioritize, and queue a batch job.

.. code-block:: bash

    curl -k -u username -d '{"name":"NAME","filename":"FILENAME","priority":"PRIORITY"}' -H "Content-Type: application/json" -X POST "https://experiments.colosseum.net/api/v1/batch/jobs/"

The API expects three parameters to be passed:

+----------+------------------------------------------------------------------+
| Parameter| Description                                                      |
+==========+==================================================================+
| name     | Required parameter but not currently used. Set this to anything  |
|          | you want.                                                        |
+----------+------------------------------------------------------------------+
| filename | Filename of the batch job to put in the batch queue.             |
+----------+------------------------------------------------------------------+
| priority | Priority of the batch job. "0" is highest priority, "1" is the   |
|          | next priority, and so on.                                        |
+----------+------------------------------------------------------------------+

Example
~~~~~~~

.. code-block:: bash

    curl -k -u username -d '{"name":"system-test-5","filename":"system-test-5","priority":"0"}' -H "Content-Type: application/json" -X POST "https://experiments.colosseum.net/api/v1/batch/jobs/"

If successful, the curl command will not produce any output. Use the "Query by Reservation ID" curl command to get batch status.

If failure, then an error message will be returned. For example, if an invalid filename is entered, then the following error is returned: "Invalid Batch JSON config file with error:FileNotFoundError(2, 'No such file or directory')"

Delete a Reservation
------------------

This command will delete any reservation type both interactive and batch.

.. code-block:: bash

    curl -k -u username -X DELETE "https://experiments.colosseum.net/api/v1/reservations/ID"

Example
~~~~~~~

.. code-block:: bash

    curl -k -u username -X DELETE "https://experiments.colosseum.net/api/v1/reservations/57410"

If successful, the curl command will not produce any output. But users will still receive the email notification about the deleted reservation.

If failure, then an error message will be returned. For example, if an invalid reservation ID is entered, then the following error is returned: "Error Querying Database for Tokens"
