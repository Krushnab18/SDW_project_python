from modules.menu import get_most_similar_word, display_menu
def view_cart(cart):
    total_amount = total(cart)
    
    print(" " * 38, "This is your cart: \n")
    print(" " * 25, "-" * 68)
    print(" " * 25, f"| {'S.No.':<8} | {'Pizza':<15} | {'Size':<10} | {'Quantity':<10} | {'Price':<10}|")
    print(" " * 25, "-" * 68)
    for idx, (pizza, size, price, qty) in enumerate(cart, start=1):
        print(" " * 25, f"| {idx:<8} | {pizza:<15} | {size:<10} | {qty:<10} | {price:<10}|")
    print(" " * 25, "-" * 68)
    print(" " * 25, "|", " " * 38, f"Total amount  --> Rs {total_amount}  |")
    print(" " * 25, "-" * 68, "\n")

def get_pizza_count():
    while True:
        try:
            count = int(input("Please enter how many pizzas do you want to order: "))
            return count
        except ValueError:
            print("Please enter an integer value only")
        
def get_qty():
    while True:
        try:
            qty = int(input("Enter Quantity of pizza required: "))
            return qty
        except ValueError:
            print("Please enter an integer value only")

def add_to_cart(cart, pizzas):
    display_menu(pizzas)
    count = get_pizza_count()
    idx = 0
    while idx < count:
        pizza_name = input("Enter pizza Name ('Q' to go back): ")
        pizza = get_most_similar_word(pizza_name, pizzas)
        if pizza != None:
            choice = input(f"Did you mean {pizza[0]}? 'Y' or 'N'(q to go back): ").upper()
            if choice == 'Y':
                while True:
                    size = input("Enter required size('S', 'M', 'L'): ").upper()
                    if size in ('S', 'M', 'L'):
                        for x in pizzas:
                            if (x[0] == pizza[0]) and (size in x[1]):
                                cart.append(x)
                                idx += 1
                                break
                        break
                    else:
                        print("Please enter valid size ('S', 'M', 'L')")
                qty = get_qty()
                length = len(cart)
                tup = cart[length - 1]
                new_tup = tup + (qty,)
                cart[length - 1] = new_tup
                print("\nPizza added to your cart!\n")
                
            elif choice == 'Q':
                return
            else:
                print("Please enter correct Pizza name")
        elif pizza == None:
            return
        else:
            print("No similar pizza found. Please enter a valid pizza name.")

def remove_from_cart(cart, pizzas):
    view_cart(cart)
    pizza_name = input("Enter pizza name you want to remove: ")
    pizza = get_most_similar_word(pizza_name, pizzas)
    choice = input(f"Did you mean {pizza[0]}? 'Y' or 'N' (q to go back): ").upper()
    
    if choice == "Y":
        while True:
            size = input("Enter pizza size:('S' 'M' 'L', q to go back): ").upper()
            if size in ['S', 'M', 'L']:
                break
            elif size == 'Q':
                return
            else:
                print("Invalid size. Please enter 'S', 'M', 'L', or 'q' to go back.")
        
        for idx, (p, s, price) in enumerate(cart):
            if p == pizza[0] and s[0].upper() == size:
                cart.pop(idx)
                print(f"{pizza[0]} ({size}) removed from your cart.\n")
                view_cart(cart)
                return
        
        print(f"{pizza[0]} ({size}) not found in your cart.")
    
    elif choice == "N":
        print("Please try again with the correct pizza name.")
    elif choice == "Q":
        return
    else:
        print("Invalid choice. Please enter 'Y', 'N', or 'q' to go back.")

def total(cart):
    return sum(row[2]*row[3] for row in cart)