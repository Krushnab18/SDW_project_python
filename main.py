from modules.auth import create_new_user, validate_login
from modules.menu import display_menu, load_pizzas
from modules.cart import add_to_cart, view_cart, remove_from_cart
from modules.order import confirm_order, view_order_history

def main():
    pizzas = load_pizzas()
    cart = []
    user = None

    while True:
        print("\nHello!, Welcome to our Pizza ordering system")
        print("Please select one of the options:\n")
        print("\t'A' --> User Login")
        print("\t'B' --> Admin Login")
        print("\t'C' --> New user Registration")
        print("\t'G' --> Guest")
        print("\t'Q' --> Quit")
        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            user = validate_login()
            if user:
                break
        elif choice == 'C':
            user = create_new_user()
            break
        elif choice == 'G':
            user = None
            break
        elif choice == 'Q':
            print("Thank you for visiting. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

    while True:
        print("\nPlease select one of the options:\n")
        print("\t'D' - Display menu")
        print("\t'O' - Order pizza/Add Pizza to cart")
        print("\t'V' - View cart")
        print("\t'C' - Confirm pizza order")
        print("\t'B' - View your order history")
        print("\t'A' - Cancel order")
        print("\t'R' - Remove pizza from cart")
        print("\t'Q' - Quit")
        choice = input("Enter choice: ").upper()

        if choice == 'D':
            display_menu(pizzas)
        elif choice == 'O':
            add_to_cart(cart, pizzas)
        elif choice == 'V':
            view_cart(cart)
        elif choice == 'C':
            confirm_order(cart, user)
        elif choice == 'B':
            view_order_history(user)
        elif choice == 'A':
            print("Feature not yet implemented.")
        elif choice == 'R':
            remove_from_cart(cart, pizzas)
        elif choice == 'Q':
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()