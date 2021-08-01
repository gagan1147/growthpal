# GrowthPal Assignment

Created the Scheduler for Multiple People

The main task is to detect any time collisions if scheduling a new meeting.
 
# For Command Line 
Used JSON file-based system for data persistency.

If the file contains any past schedule it first loads the file and creates the schedule.

To run 
python3 main.py

# For API
To run 

python3 manage.py runserver

Used Django as a Backend for creating the APIs

To Schedule meetings with multiple people

Send POST request to 127.0.0.1:8000/api_create_meetings

with the following json data

example data = {
    "person":["p1","p2","p3"],
    "date":5082021,
    "start":1030,
    "end":1100,
    "roomID":"r1"
}

for Multiple Scheduling 

Send POST request to 127.0.0.1:8000/api_json

with the following json data

example data = {
  "user": {
    "p0": {
      "5082021": [
        {
          "start": 1030,
          "end": 1200,
          "roomID": "r1"
        }
      ]
    },
    "p1": {
      "5082021": [
        {
          "start": 1030,
          "end": 1200,
          "roomID": "r1"
        }
      ],
      "6082021": [
        {
          "start": 1725,
          "end": 1800,
          "roomID": "r5"
        }
      ]
    },
    "p2": {
      "5082021": [
        {
          "start": 1030,
          "end": 1200,
          "roomID": "r1"
        }
      ],
      "6082021": [
        {
          "start": 1725,
          "end": 1800,
          "roomID": "r5"
        }
      ]
    }
  }
}

# To Know About Meeting After sending the above post request

open on browser

http://127.0.0.1:8000/show_meetings

