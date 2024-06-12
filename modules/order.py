import csv
from datetime import datetime
from modules.cart import view_cart, total
from modules.bill import generate_bill
from modules.utils import save_user_to_csv

def generate_unique_order_id():
    starting = "ABCDE"
    with open("data/orders.csv") as fp:
        reader = csv.reader(fp)
        rows = list(reader)
        length = len(rows)
        end = length + 7498
    return starting + str(end)

def save_order(order_id, order_status, cart, payment_mode, user, total):
    with open("data/orders.csv", "a") as fp:
        writer = csv.writer(fp)
        writer.writerow([user.name, user.emailId, order_id, order_status, cart, total, payment_mode])

def confirm_order(cart, user):
    print("Help us with some information to complete your order: ")
    if len(cart) == 0:
        print("Cart is empty")
        return
    while True:    
        choice = input("Please select payment mode('A'-->online, 'B' --> offline, Q --> go back): ").upper()
        if choice == 'A':   
            upi_id = input("Please enter your UPI-ID: ")
            print("Please complete your payment through the notification sent to your payment app")
            print("Please wait.....")
            print("Verifying............")
            print("Payment successful! Your order is on the way")
            order_id = generate_unique_order_id()
            order_status = "placed"
            payment_mode = "online"
            total_payment = total(cart)
            now = datetime.now()
            current_date = now.strftime("%d/%m/%Y %H:%M:%S")
            generate_bill(order_id,cart, user, current_date)
            save_order(order_id, order_status, cart, payment_mode, user, total_payment)
            cart.clear()
            return
        elif choice == 'B':
            print("Please keep cash ready to handover while getting your order delivered")
            order_id = generate_unique_order_id()
            order_status = "placed"
            payment_mode = "offline"
            total_payment = total(cart)
            now = datetime.now()
            current_date = now.strftime("%d/%m/%Y %H:%M:%S")
            generate_bill(order_id,cart, user, current_date)
            save_order(order_id, order_status, cart, payment_mode, user, total_payment)
            cart.clear()
            return
        elif choice == 'Q':
            return
        else:
            print("Invalid choice. Please try again.")

def view_order_history(current_user):
    with open("./data/orders.csv", "r") as fp:
        reader = csv.reader(fp)
        
        header = "Your Order History!"
        separator = "-" * 123
        print(f"\n{' ' * ((123 - len(header)) // 2)}{header}\n")
        
        # Print table header
        print(f"{' ' * 3}| {'Order ID':<15} | {'Order Status':<15} | {'Items':<47} | {'Total Amount':<15} | {'Payment Mode':<15} |")
        print(f"{' ' * 3}{separator}")
        
        for row in reader:
            if row[1] == current_user.emailId:
                order_id = row[2]
                order_status = row[3]
                items = eval(row[4])  # Convert tuple representation of list to actual list
                total_amount = row[5]
                payment_mode = row[6]
                
                # Print order details
                print(f"{' ' * 3}| {order_id:<15} | {order_status:<15} | ", end="")
                
                # Print items
                for idx, (pizza, size, price, qty) in enumerate(items):
                    item_str = f"{pizza} ({size}) x {qty} - Rs {price}"
                    if idx == 0:
                        print(f"{item_str:<45}", end="")
                    else:
                        print("\n   |", f"{' ' * 17} {' ' * 15} | {item_str:<45}", end="")
                
                # Print total amount and payment mode
                print(f"{' ' * 3}| {total_amount:<15} | {payment_mode:<15} |")
                print(f"{' ' * 3}{separator}")
                
    
def save_order_to_csv(rows):
    with open("./data/orders.csv", "w", newline='') as fp:
        writer = csv.writer(fp)
        writer.writerows(rows)

def cancel_order(user):
    if(user == None):
        print("Please login or create new account")
        return
    view_order_history(user)
    order_id = input("Enter order_id: ")
    
    # Read the current orders
    with open("./data/orders.csv", "r") as fp:
        reader = csv.reader(fp)
        orders = list(reader)
    
    # Find and update the order
    order_found = False
    for row in orders:
        if row[2] == order_id:
            row[3] = "Cancelled"
            order_found = True
            print("Order cancelled successfully")
            if row[5] == 'online':
                print("We are working on your refund. You will get your refund in the original payment method you used")
    
    if order_found:
        save_order_to_csv(orders)
    else:
        print("Order ID not found")