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
            return
        elif choice == 'Q':
            return
        else:
            print("Invalid choice. Please try again.")