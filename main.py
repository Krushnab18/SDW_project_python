from modules.auth import create_new_user, validate_login
from modules.menu import display_menu, load_pizzas
from modules.cart import add_to_cart, view_cart, remove_from_cart
from modules.order import confirm_order, view_order_history, cancel_order

def main():
    pizzas = load_pizzas()
    cart = []
    user = None

    while True:
        print("\n\t\t\t\tHello!, Welcome to our Pizza ordering system")
        print("\t\t\t\t    Please select one of the options:\n")
        print("\t\t\t\t\t'A' --> User Login")
        print("\t\t\t\t\t'B' --> Admin Login")
        print("\t\t\t\t\t'C' --> New user Registration")
        print("\t\t\t\t\t'G' --> Guest")
        print("\t\t\t\t\t'Q' --> Quit\n\n")
        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            user = validate_login()
            if user:
                print("\n\t\t\t\tLogin Successful")
                break
        elif choice == 'C':
            user = create_new_user()
            print("\n\t\t\t\tCongratulations! Your account is registered Successfully.")
            break
        elif choice == 'G':
            user = None
            break
        elif choice == 'Q':
            print("\t\t\t\tThank you for visiting. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

    while True:
        print("\n\t\t\t\tPlease select one of the options:\n")
        print("\t\t\t\t\t'D' - Display menu")
        print("\t\t\t\t\t'O' - Order pizza/Add Pizza to cart")
        print("\t\t\t\t\t'V' - View cart")
        print("\t\t\t\t\t'C' - Confirm pizza order")
        print("\t\t\t\t\t'B' - View your order history")
        print("\t\t\t\t\t'A' - Cancel order")
        print("\t\t\t\t\t'R' - Remove pizza from cart")
        print("\t\t\t\t\t'Q' - Quit\n")
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
            cancel_order(user)
        elif choice == 'R':
            remove_from_cart(cart, pizzas)
        elif choice == 'Q':
            print("\t\t\t\tThank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()