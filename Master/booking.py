#module 3 = booking

import rooms

def check_in(room_no, cust_id, days):
    rooms.rooms_data[room_no]["status"]="occupied"
    rooms.active_stays[room_no]={
        "cust_id": cust_id,
        "days": days,
        "food_orders": []

    }

def release_room(room_no):
    rooms.rooms_data[room_no]["status"]="availbel"
    if room_no in rooms.active_stays:
        del rooms.active_stays[room_no]