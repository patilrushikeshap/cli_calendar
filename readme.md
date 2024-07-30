# CLI Calendar System

This project is a command-line interface (CLI) calendar system that allows you to schedule and manage meetings. It includes features to detect collisions when scheduling meetings, handle multiple participants, and allocate meeting rooms.

## Features

- Schedule a meeting with a specified day, time, room, and participants.
- Detect collisions if a meeting is scheduled at the same time as another meeting in the same room or with the same participants.
- List all scheduled meetings.

## Requirements

- Python 3.x
- Virtual environment (`venv`)
- `SQLAlchemy` package

## Project Structure

cli_calendar/
│
├── venv/
│ ├── Scripts/
│ ├── Lib/
│ ├── ...
│
├── calendar_system.py
├── requirements.txt
└── README.md


- **venv/**: Virtual environment directory containing dependencies and Python binaries.
- **calendar_system.py**: Main script with database model, scheduling functions, and CLI logic.
- **requirements.txt**: File listing project dependencies.
- **README.md**: Project overview and setup instructions.

## Setup

### 1. Clone the Repository

Clone the repository to your local machine.

### 2. Create and Activate Virtual Environment

Navigate to the project directory and create a virtual environment:

- **python -m venv venv**
- **venv\Scripts\activate**  # For Windows

### 3. Install Dependencies
Install the required dependencies listed in requirements.txt:

- **pip install -r requirements.txt**

### 4. Running the Application
    Schedule a Meeting

    To schedule a meeting, use the schedule command with the following arguments:

    day: The day of the meeting in YYYY-MM-DD format.
    start_time: The start time of the meeting in HH:MM format.
    end_time: The end time of the meeting in HH:MM format.
    room: The meeting room.
    participants: Comma-separated list of participants.

- For example:- **python calendar_system.py schedule 2024-07-30 09:00 10:00 "Room 101" "Rushi, Pranav"**

    List All Meetings

    To list all scheduled meetings, use the list command:
-   **python calendar_system.py list**



###### Code Explanation ######
```sh

calendar_system.py


## Imports and Setup ##

SQLAlchemy: Used for database operations.
datetime: Used for date and time operations.

## Database Model ##

It defines the Meeting class representing a meeting record in the database with fields for day, start_time, end_time, room, and participants

### Database Initialization ##

Creates an SQLite database meetings.db and initializes a session to interact with the database.

## Scheduling Function ##

Scheduling functions converts input strings to datetime objects and 
Checks for time collisions with existing meetings also 
Schedules the meeting if no collisions are found.

## Listing Function ##

Retrieves all meetings from the database.

## Command-Line Interface 

Handles command-line arguments to schedule and list meetings.


PROJECT OUTPUT PICTURE WITH MULTIPLE USECASES ATTACHED IN THE SAME WORKING FOLDER (IMAGE.png)

#######################################################################################################################################
                                                    THANK YOU     
