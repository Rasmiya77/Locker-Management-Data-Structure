# Python Locker Data Structure

## Overview

This project demonstrates how a **nested dictionary** can be used in Python to store and manage locker information.

The program manages locker IDs, occupancy status, mobile numbers, passcodes, and storage time. It also demonstrates different operations for searching, updating, adding, and counting lockers.

This is an **academic project** developed as part of the **Introduction to Programming** module.

## Technologies & Tools

* Python
* PyCharm

## Concepts Demonstrated

* Nested Dictionaries
* For Loops
* Conditional Statements
* Dictionary Operations
* Data Searching and Updating
* Basic Data Processing

## Data Structure

The project uses a **nested dictionary** to store locker information.

Each locker has a unique locker ID, such as `L01`, `L02`, and `L03`.

Each locker stores:

* `occupied` – stores whether the locker is occupied
* `mobile` – stores the mobile number
* `passcode` – stores the locker passcode
* `time` – stores the storage time in hours

Example:

```python
lockers["L01"] = {
    "occupied": True,
    "mobile": "0500000001",
    "passcode": "SR07",
    "time": 5
}
```

## Operations Demonstrated

The program demonstrates several practical operations, including:

1. Displaying locker information
2. Finding occupied lockers
3. Finding available lockers
4. Changing an available locker to occupied
5. Clearing an occupied locker
6. Adding a new locker
7. Updating storage time
8. Searching for a locker using its ID
9. Searching for a locker using a mobile number
10. Counting total, occupied, and available lockers
11. Calculating total occupied storage time

## How to Run

1. Download or clone this repository.
2. Make sure Python is installed on your computer.
3. Open `locker_data_structure.py` in any Python-supported development environment.
4. Run the Python file.
5. View the program output in the terminal or console.

## Example Output

The program produces output showing locker details, locker status, search results, updates, and storage-time calculations.

A sample output screenshot is available in the `screenshots` folder.


## What I Learned

Through this project, I practised:

* Creating and using nested dictionaries
* Accessing and updating dictionary values
* Searching data using keys and values
* Using loops to process stored data
* Filtering data using conditions
* Calculating values from stored data

