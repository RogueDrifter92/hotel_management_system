#module 5 = billing

tax_rate = 0.18 # 18 % gst

def generate_checkout_bill(room_no, room_info, stay_info, cust_info):
    days = stay_info["days"]
    price_per_night = room_info["price"]
    room_total = price_per_night * days

    # calculation of total resturant bill
    food_total = 0
    for order in stay_info["food_orders"]:
        food_total = food_total + order["total"]

    subtotal = room_total + food_total
    tax = subtotal * tax_rate
    grand_total = subtotal + tax

    invoice = {
        "cust_name": cust_info["name"],
        "cust_phone": cust_info["phone"],
        "room_no" : room_no,"room_type": room_info["type"],"days": days,
        "rate": price_per_night,"food_orders": stay_info["food_orders"],"tax": tax,"room_total": room_total,"food_total": food_total,
        "grand_total": grand_total
    }
    return invoice

def print_receipt(invoice):
    print(" ")
    print("checkout")
    print(" ")
    print(f"customer name : {invoice['cust_name']}")
    print(f"phone number : {invoice["cust_phone"]}")
    print(f"room number : {invoice["room_no"]}")
    print(f"duration : {invoice["days"]}")
    print(f"room charges : rs. {invoice['room_total']}")

    print(" ")
    print("resturant orders")
    if len(invoice["food_orders"]) >0:
        for order in invoice['food_orders']:
            print(f"{order['name']} * {order['qty']} = rs.{order['total']:.2f}")
        print(f"food total :rs. {invoice['food_total']:.2f}")
    else:
        print(" no orders recived")

    print(" ")
    print(f"grand total : rs.{invoice["grand_total"]:.2f}")
    print(" ")