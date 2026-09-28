#module 2 = customers details

customer_database = {}

# creation of new customer details
def add_new_customer():
    print("--- Register New Customer ---")
    cust_id = input ("Enter unique id for customer: ")

    if cust_id in customer_database:
        print("customer id already exists.")
        return cust_id

    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    addharcard_no = input("enter addhar no: ")
    city = input("enter city: ")

    customer_database[cust_id] ={
        "customer id": cust_id,
        "name": name,
        "phone": phone,
        "addharcard no": addharcard_no,
        "city": city
    }
    print(f"customer '{name}' registation completed secquerly")
    return cust_id

def view_all_customers():
    print("--- registerd customers ---")
    if len(customer_database) == 0:
        print("No customer found")
        return
    for cid, data in customer_database.items():
        print(f"id: {cid}  name: {data['name']}  phone: {data['phone']}  city: {data['city']}")