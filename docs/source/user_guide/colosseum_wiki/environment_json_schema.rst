Environment JSON Schema
=====================

:Created: 2020-03-31T14:59:41-04:00
:Updated: 2020-03-31T14:59:41-04:00

:Tags: environment json, FD_V2_537243 Import

.. code-block:: json

   {
     "$schema": "http://json-schema.org/draft-04/schema#",
     "title": "environment schema",
     "type": "array",
     "items": {
       "type": "object",
       "properties": {
         "environment": {
           "type": "array",
           "items": {
             "type": "object",
             "properties": {
               "collab_network_type": {
                 "type": "string"
               },
               "incumbent_protection": {
                 "type": "array",
                 "items": {
                   "type": "object",
                   "properties": {
                     "center_frequency": {
                       "type": "integer"
                     },
                     "rf_bandwidth": {
                       "type": "integer"
                     }
                   }
                 }
               },
               "scenario_center_frequency": {
                 "type": "integer"
               },
               "scenario_rf_bandwidth": {
                 "type": "integer"
               }
             },
             "required": [
               "collab_network_type",
               "scenario_center_frequency",
               "scenario_rf_bandwidth"
             ]
           },
           "maxItems": 1
         },
         "stage_number": {
           "type": "integer"
         },
         "timestamp": {
           "type": "number"
         }
       },
       "required": [
         "environment",
         "stage_number",
         "timestamp"
       ]
     }
   }