# main file

import rooms
import customers
import booking
import restaurant
import billing
import storage

def main():
    while True:
        print(" ")
        print("Hotel Management System")
        print(" ")
        print("1. Register a new customer")
        print("2. view registered customers")
        print("3. room prices")
        print("4. check-in")
        print("5. order food to room")
        print("6. checkout and billing")
        print("0. exit")

        x = int(input("enter process no.(1-6,0(for exit)): "))

        #1 Register a new customer
        if x == 1:
            customers.add_new_customer()
        #2 view registered customers
        elif x == 2:
            customers.view_all_customers()
        #3 room prices
        elif x == 3:
            rooms.display_rooms()
        #4 check-in
        elif x == 4:
            cust_id = input("enter customer id: ")
            if cust_id not in customers.customer_database:
                print("customer not found")
                continue

            rooms.display_rooms()
            room_input = input("enter the room no to book: ")
            if not room_input.isdigit():
                print("please entr a valid room no")
                continue

            room_no = int(room_input)
            if not rooms.is_free(room_no):
                print("room is already occupied")
                continue

            days_input = input("no of days of stay: ")
            if not days_input.isdigit() or int(days_input) <= 0:
                print("no of days of stay should be in positive")
                continue

            days = int(days_input)
            booking.check_in(room_no, cust_id, days)
            cust = customers.customer_database[cust_id]
            print(f"the customer is checked in room no {room_no} for mr/ms. {cust['name']}.")

        #5 order food to room
        elif x == 5:
            room_input = input("enter room no to order food")
            if not room_input.isdigit():
                print("please enter a correct room no")
                continue

            room_no = int(room_input)
            restaurant.order_food_for_room(room_no)

        #6 checkout and billing
        elif x == 6:
            room_input = input("enter room no for check out")
            if not room_input.isdigit():
                print("enter the room no properly")
                continue

            room_no = int(room_input)
            if not rooms.is_occupied(room_no):
                print("room is ready for another booking")
                continue

            stay_info = rooms.active_stays[room_no]
            cust_info = customers.customer_database[stay_info["cust_id"]]
            room_info = rooms.rooms_data[room_no]

            # printing checkout invoice
            invoice = billing.generate_checkout_bill(room_no,room_info,stay_info,cust_info)
            billing.print_receipt(invoice)
            storage.save_file_bill(invoice)

            #free up the room
            booking.release_room(room_no)
            print(f"the room no {room_no} is now availabe for booking")

        #0 exit
        elif x == 0:
            print("thank you for visiting")
            break

        else:
            print("please select from option 1-6 or 0 for exit")

if __name__ == "__main__":
    main()     