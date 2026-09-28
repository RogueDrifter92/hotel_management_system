# module 1 = Rooms

rooms_data = {
    1001: {"type": "tent Non-AC", "price": 1000, "status": "available"},
    2002: {"type": "tent AC", "price": 2500, "status": "available"},
    3003: {"type": "tree house AC", "price": 4000, "status": "available"},
    4004: {"type": "bambu house AC", "price": 8500, "status": "available"},
    5005: {"type": "presidential suite", "price":10000, "status": "available"}
}

# storage for active room booking
active_stays ={}


def display_rooms():
    print("Available Rooms & Rates")
    print(f"{'Room No'} {'Room Type'} {'Price Per Night'} {'Status'}")
    print(" ")
    for r_no, details in rooms_data.items():
        print(f"{r_no} {details['type']} Rs.{details['price']} {details['status']}")
    print(" ")

def is_free(room_no):
    if room_no in rooms_data:
        return rooms_data[room_no]['status']=="available"
    return False

def is_occupied(room_no):
    if room_no in rooms_data:
        return rooms_data[room_no]['status']=="occupied"
    return False