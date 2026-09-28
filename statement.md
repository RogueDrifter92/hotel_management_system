Project Statement : Hotel Management System

1. Why Build This? (the problem)

watching how a receptionist handles thinks at a small resort during a busy weekend shows just how chaotic it can get. smaller places especially eco resorts with stays like tents or bamboo huts tend to depend on notebooks and scattered messages or spreadsheets. it seems like that setup works for them most days. but when it gets really busy that part gets a bit messy. i am not totally sure how they manage all the details without missing something.

manual setup breaks down quickly:
- a guest orders snakes or dinner to their cottage, but the kitchen staff did not handle the order recipit properly and lost it due to which resort will face loss unknowingly.
- to avoid in convinse in accendental double booking and also maintain a proper higine in the rooms and alert the housekeeping staff.
- to avoid calculation mistakes during checkout

i built this project to built a leight weight program for the day-to-day task

2. What the project sets out to do
- the project is ment to keep the customer data organized with essential detail related to customer like name, contact, city, and ID.
- for tracking room status in real time with out any mistakes.
- it also trakes the food ordered by the guests and and then add the bill of food with the room bill.
- during the check out it automaticaly generated bill with a total breakdown to avoid inconvinance to the guest.
- after every check out the details of guest is stored.

3. scope: what it does(and what it leaves for later)

whats handled right now
- guest profile: fast onboarding using simple unique id.
- distinct stays : built in pricing for various accommodations(non ac/ac tents, treehouses, bamboo houses, and suits).
- kitchen orders loop : muilti item food ordering linked directly to occupied rooms.
- accurate invoice : actomatically frees up the room immediately after checkout.
- room cleaning: automatically alerts the house keeping team to make the room ready for the next customer

what i want to do in future
- i will also update the program in which i will add discount as per the user.
- i will also add a status for graphs in which it will tell us the profit and loss in the buisness

4. who is this for?
- front desk staff & caretakers: who needs a convinent terminal for the check on someone in sending food to a room, and generate an invoice in seconds.
- resort owners who want assurance that every cup of tea , meal and night stayed gets accounted for accurately whitout buying heavy enterprise software.
- students & reviewes : anyone intrested in seeing how basic data structures and clean modular architecture in python solve real world operational problems.

5. core rules & logic
to keep operations reliable , the application follows a few strict rules:
- a guest must be registered with a customer id before they can check in.
- an occuoied room cannot be booked again until the current occupant checks out.
- food orders can only be dispatched to rooms that are actually occupied.
- checkout math followa a clear, predictable formula:
                            subtotal = room total + food total

                            tax(GST 18%)= subtotal * 0.18

                            grand total = subtotal + tax

- once checkout is processed, the room immediately returns to availabe status so recepition knews it can be reassined right away.