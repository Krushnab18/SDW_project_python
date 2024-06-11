import csv
from datetime import datetime
from modules.cart import view_cart
from modules.bill import generate_bill

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
            total_payment = sum(price for _, _, price in cart)
            now = datetime.now()
            current_date = now.strftime("%d/%m/%Y %H:%M:%S")
            generate_bill(cart, total_payment, current_date)
            save_order(order_id, order_status, cart, payment_mode, user, total_payment)
            cart.clear()
            return
        elif choice == 'B':
            print("Please keep cash ready to handover while getting your order delivered")
            order_id = generate_unique_order_id()
            order_status = "placed"
            payment_mode = "offline"
            total_payment = sum(price for _, _, price in cart)
            now = datetime.now()
            current_date = now.strftime("%d/%m/%Y %H:%M:%S")
            generate_bill(cart, total_payment, current_date)
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
        
        print("\n", " " * 40, "Your Order History!\n")
        print(" " * 5, f"| {'order_id':<15} | {'order_status':<15} | {'items':<44} | {'total amount':<15} | {'payment mode':<15} |")
        print(" " * 5, "-" * 121)
        
        for row in reader:
            if row[1] == current_user.emailId:
                order_id = row[2]
                order_status = row[3]
                items = eval(row[4])  # Convert string representation of list to actual list
                total_amount = row[5]
                payment_mode = row[6]
                
                # Print order details
                print(" " * 5, f"| {order_id:<15} | {order_status:<15} | ", end="")
                
                # Print items
                for idx, (pizza, size, price) in enumerate(items):
                    if idx == 0:
                        print(f"{pizza} ({size}) - Rs {price}", end="")
                    else:
                        print(f"\n{'':<23}   {'':<15} | {pizza} ({size}) - Rs {price}", end="")
                
                # Print total amount and payment mode
                print(" "*18,f"| {total_amount:<15} | {payment_mode:<15} |")
                print(" " * 5, "-" * 121)