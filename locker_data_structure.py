# Locker System
# This program uses a nested dictionary data structure to store and manage locker details.


# Step 1: Empty data structure
lockers = {}


# Step 2: Add hardcoded test data
lockers["L01"] = {
    "occupied": True,
    "mobile": "0500000001",
    "passcode": "SR07",
    "time": 5
}

lockers["L02"] = {
    "occupied": False,
    "mobile": None,
    "passcode": None,
    "time": 0
}

lockers["L03"] = {
    "occupied": True,
    "mobile": "0500000002",
    "passcode": "Abc123",
    "time": 12
}

lockers["L04"] = {
    "occupied": True,
    "mobile": "0500000003",
    "passcode": "Mylock4",
    "time": 2
}

lockers["L05"] = {
    "occupied": False,
    "mobile": None,
    "passcode": None,
    "time": 0
}


# Operation 1 - Display all lockers

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " LOCKER DETAILS ".center(60) + "|")
print("+" + "═" * 60 + "+")

for locker_id, locker_data in lockers.items():
    print(f"\nLocker ID   : {locker_id}")
    print(f"Occupied    : {locker_data.get('occupied')}")
    print(f"Mobile      : {locker_data.get('mobile')}")
    print(f"Passcode    : {locker_data.get('passcode')}")
    print(f"Time        : {locker_data.get('time')} hours")
    print("_" * 62)


# Operation 2 - Find occupied lockers

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " OCCUPIED LOCKERS ".center(60) + "|")
print("+" + "═" * 60 + "+")

for locker_id, locker_data in lockers.items():
    if locker_data.get("occupied"):
        print(f"\nLocker ID   : {locker_id}")
        print(f"Mobile      : {locker_data.get('mobile')}")
        print(f"Passcode    : {locker_data.get('passcode')}")
        print(f"Time        : {locker_data.get('time')} hours")
        print("_" * 62)


# Operation 3 - Find available/empty lockers

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " AVAILABLE LOCKERS ".center(60) + "|")
print("+" + "═" * 60 + "+")

for locker_id, locker_data in lockers.items():
    if not locker_data.get("occupied"):
        print(f"\nLocker ID : {locker_id}")
        print(f"Occupied  : {locker_data.get('occupied')}")
        print("_" * 62)


# Operation 4 - Allocate an empty locker

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " CHANGE A LOCKER FROM EMPTY TO OCCUPIED ".center(60) + "|")
print("+" + "═" * 60 + "+")

print("\nCurrent Locker Details:")

print("\nLocker ID : L02")
print(f"Occupied  : {lockers['L02']['occupied']}")
print(f"Mobile    : {lockers['L02']['mobile']}")
print(f"Passcode  : {lockers['L02']['passcode']}")
print(f"Time      : {lockers['L02']['time']} hours")
print("_" * 62)

lockers["L02"]["occupied"] = True
lockers["L02"]["mobile"] = "0500000004"
lockers["L02"]["passcode"] = "B45C"
lockers["L02"]["time"] = 1

print("\nUpdated Locker Details:")

print("\nLocker ID : L02")
print(f"Occupied  : {lockers['L02']['occupied']}")
print(f"Mobile    : {lockers['L02']['mobile']}")
print(f"Passcode  : {lockers['L02']['passcode']}")
print(f"Time      : {lockers['L02']['time']} hours")
print("_" * 62)


# Operation 5 - Free an occupied locker

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " CLEAR LOCKER AFTER RETRIEVAL ".center(60) + "|")
print("+" + "═" * 60 + "+")

print("\nCurrent Locker Details:")

print("\nLocker ID : L03")
print(f"Occupied  : {lockers['L03']['occupied']}")
print(f"Mobile    : {lockers['L03']['mobile']}")
print(f"Passcode  : {lockers['L03']['passcode']}")
print(f"Time      : {lockers['L03']['time']} hours")
print("_" * 62)

lockers["L03"]["occupied"] = False
lockers["L03"]["mobile"] = None
lockers["L03"]["passcode"] = None
lockers["L03"]["time"] = 0

print("\nUpdated Locker Details:")

print("\nLocker ID : L03")
print(f"Occupied  : {lockers['L03']['occupied']}")
print(f"Mobile    : {lockers['L03']['mobile']}")
print(f"Passcode  : {lockers['L03']['passcode']}")
print(f"Time      : {lockers['L03']['time']} hours")
print("_" * 62)


# Operation 6 - Add a new locker

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " ADD A NEW LOCKER ".center(60) + "|")
print("+" + "═" * 60 + "+")

new_id = "L06"

lockers[new_id] = {
    "occupied": True,
    "mobile": "0500000005",
    "passcode": "Loc123",
    "time": 1
}

print("\nLocker added successfully!")

print("\nNEW LOCKER DETAILS:\n")
print(f"Locker ID : {new_id}")
print(f"Occupied  : {lockers[new_id]['occupied']}")
print(f"Mobile    : {lockers[new_id]['mobile']}")
print(f"Passcode  : {lockers[new_id]['passcode']}")
print(f"Time      : {lockers[new_id]['time']} hours")


# Operation 7 - Update locker usage time

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " UPDATE STORAGE TIME ".center(60) + "|")
print("+" + "═" * 60 + "+")

print("\nCurrent Locker Details:")

print("\nLocker ID : L04")
print(f"Time      : {lockers['L04']['time']} hours")
print("_" * 62)

lockers["L04"]["time"] += 3

print("\nUpdated Locker Details:")

print("\nLocker ID : L04")
print(f"Time      : {lockers['L04']['time']} hours")
print("_" * 62)


# Operation 8 - Search for a locker by ID

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " SEARCH LOCKER BY UNIQUE ID ".center(60) + "|")
print("+" + "═" * 60 + "+")

search_id = "L02"

print("\nSearching locker using locker ID:", search_id)

locker_data = lockers.get(search_id)

if locker_data:
    print("\nSearch Result: Matching locker found")

    print(f"\nLocker ID   : {search_id}")
    print(f"Occupied    : {locker_data.get('occupied')}")
    print(f"Mobile      : {locker_data.get('mobile')}")
    print(f"Passcode    : {locker_data.get('passcode')}")
    print(f"Time        : {locker_data.get('time')} hours")

else:
    print("\nSearch Result: Locker not found.")


# Operation 9 - Search for a locker by mobile number

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " SEARCH LOCKER BY MOBILE NUMBER ".center(60) + "|")
print("+" + "═" * 60 + "+")

search_mobile = "0500000001"

print("\nSearching locker using mobile number:", search_mobile)

found = False

for locker_id, locker_data in lockers.items():
    if locker_data.get("mobile") == search_mobile:
        print("\nSearch Result: Matching locker found")

        print(f"\nLocker ID   : {locker_id}")
        print(f"Occupied    : {locker_data.get('occupied')}")
        print(f"Mobile      : {locker_data.get('mobile')}")
        print(f"Passcode    : {locker_data.get('passcode')}")
        print(f"Time        : {locker_data.get('time')} hours")

        found = True
        break

if not found:
    print("\nSearch Completed")
    print("Result: No locker found with this mobile number")


# Operation 10 - Count lockers

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " COUNT TOTAL, OCCUPIED, AND AVAILABLE LOCKERS ".center(60) + "|")
print("+" + "═" * 60 + "+")

total = len(lockers)
occupied = 0

for locker in lockers.values():
    if locker["occupied"]:
        occupied += 1

available = total - occupied

print(f"\nTotal Number of Lockers     : {total}")
print(f"Occupied Number of Lockers  : {occupied}")
print(f"Available Number of Lockers : {available}")


# Operation 11 - Calculate total occupied storage time

print("\n\n" + "+" + "═" * 60 + "+")
print("|" + " TOTAL OCCUPIED STORAGE TIME ".center(60) + "|")
print("+" + "═" * 60 + "+")

total_time = 0

for locker_id, locker_data in lockers.items():
    if locker_data.get("occupied"):
        total_time += locker_data.get("time")

print("\nTotal occupied storage time:", total_time, "hours\n")