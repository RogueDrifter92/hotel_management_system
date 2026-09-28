#module 4 = resturant menu and oders

import rooms

menu = {
    1: {"name": "paneer tokka", "price": 220},
    2: {"name": "chicken tikka", "price": 280},
    3: {"name": "dal makhani", "price": 200},
    4: {"name": "butter chicken", "price": 320},
    5: {"name": "tanduri roti", "price": 35},
    6: {"name": "butter naan", "price": 45},
    7: {"name": "cold drinks", "price": 50}
}

def display_menu():
    print("Restaurant Menu")
    print(f"{"code"} {"item name"} {"price (rs)"}")
    print(" ")
    for code, item in menu.items():
        print(f"{code} {item["name"]} Rs. {item["price"]}")
    print(" ")

def order_food_for_room(room_no):
    if not rooms.is_occupied(room_no):
        print(f"room {room_no} is not currently checkedin.")
        return

    display_menu()
    while True:
        choice_input = input("enter food code to order (or 0 to finish): ")
        if not choice_input.isdigit():
            print("please enter a digit from above numbers")
            continue
        choice = int(choice_input)
        if choice == 0:
            break
        if choice not in menu:
            print("invalid serial no.")
            continue
        qty_input = input(f"enter quantity for '{menu[choice]['name']}': ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("quantity must be a positive number")
            continue
        qty = int(qty_input)
        item = menu[choice]
        total_price = item["price"] *qty
        rooms.active_stays[room_no]["food_orders"].append({
            "name": item["name"],
            "qty": qty,
            "total": total_price
        })
        print(f"the bill is added to the rooms total bill")
