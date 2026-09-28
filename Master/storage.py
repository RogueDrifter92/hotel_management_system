#module 6 = storage

def save_file_bill(invoice):
    file = open("checkout_records.txt", "a")
    file.write(
        f"customer: {invoice['cust_name']}  room: {invoice['room_no']} ({invoice['room_type']}) days: {invoice['days']} room cost: rs.{invoice['room_total']} food cost: rs.{invoice['food_total']} grandtotal: rs{invoice['grand_total']:.2f} "        
    )
    file.close()
    print("invoice save to checkout records")
    