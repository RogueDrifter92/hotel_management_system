Resort & Hotel Management System:

A clean , module terminal-based hotel manegement system built in python. this project simulates essential front-desk and room - service operations for a resort - from guest registration and room allocations to restaurent room service, billing calculations (including GST), and persistent checkout logging.

Project Overview:

Managing hotel operations involves coordinating several moving parts simlutaneously tracking occupied rooms, registering guists, handlling resturant orders changed to rooms, and computing accurate invoice at check out

i have created several modules in order to divide the task for specific operations while perfoming different tasks the different modules are customers, room inventories, booking, restsurant menu, billing calculations. it is a friendly and straight forward frameworks.

Features:
- guest registrations are done in customers.py with details of guest like name, id, phone number,aadhaar number, city.
- the rooms related data is taken by the rooms.py module and this module is also used for displaying the avability and types of rooms availabe for the customers
- for assining rooms to the customer we have booking.py module to track the active status record of a room at that instants.
- for in rooom servise and resturant service i have created restaurant.py module this module displays the menu when called and also generates the bill which is then added to the total bill.
- for removing human error in the calculation of the bill i have created billing.py module.
- for the storage of checkedout customers i have created storage.py module which stores the data in checkout_records.txt so that to maintaine a proper history of customer check in and out.

Technologies & tools used
- language used is python3.14
- i have used 6 various modules for perfoming task and completing the project
- for the check out history i have used .txt file for maintaing records
- virsion control: Git & Git Hub

Steps to Install & Run Project:

- make sure to install python3.8 or higher in your computer
-- Installation
  1. clone or download the repository or download the .py files into a single local diractory.
  2. this no need of installing any extra external packages.
-- Running the application
  - type in your terminal python main.py

Instructions for Testing:

1. Register a customer:
- select the option 1 from the main menu
- enter the details and create a unique id
- you will be able to see the newly registered customer by selecting the 2 option in the main menu.

2. Type of room and avalability of the room:
- select option 3 in the main menu for checking the avibility of rooms
- select 4 option in the main menu for the check in of the customer
        - enter the guest id
        - enter the room no which the customer wants
        -enter the duartion of the stay
- after the check in you can select 3 option to check the ststus of the room

3. for resturant & resturant services in room:
- select option 5 to place orders
- enter the room number of the guest
- chose the serial no of the food and the mention the quantity of the food
- enter 0 to exit from resturen order services

4. check out & billing:
- select option 6 to begin check out
- enter the room no
- the bill will be generated and it will also display room total, food total, and grand total with applied GST
- then the room is availabe for the next customer
- the customer check out details will be saved in the checkout_records.txt file

5. Exit
- select the option 0 from the main menu for coming out of the program.