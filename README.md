# SDW_Python_project
Pizza Ordering System
# Pizza Ordering System

The Pizza Ordering System is a command-line application designed to streamline the process of ordering pizzas from a pizza shop. It allows users to browse through a menu of available pizzas, select their desired pizzas with customizable sizes, add them to a cart, view their cart, and confirm their order. Additionally, users can view their order history, cancel orders, and remove pizzas from their cart.

## Key Features

- **Menu Display**: View available pizzas along with their sizes and prices.
- **Order Placement**: Place orders by selecting pizzas from the menu and specifying sizes.
- **Cart Management**: View, add, or remove pizzas in your cart before confirming your order.
- **Order Confirmation**: Confirm orders with options for online or cash payment modes.
- **Order History**: View past orders and track their status.
- **Order Cancellation**: Cancel orders if necessary, with appropriate refund handling for online payments.

## Technologies Used

- **Python**: The core programming language used to develop the application.
- **CSV**: Data storage for storing pizza menu, user information, and order history.
- **FPDF**: Library for generating PDF bills for confirmed orders.
- **HASLIB**: Library for Hashing password

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone git@github.com:yourusername/pizza-ordering-system.git
    cd pizza-ordering-system
    ```

2. **Install dependencies**:
    Ensure you have Python installed. Then, install required packages using pip:
    ```bash
    pip install fpdf
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## How to Use

1. **Login/Registration**: Log in with your existing credentials or create a new account.
2. **Browse Menu**: View available pizzas from the menu.
3. **Order Placement**: Add pizzas to your cart by specifying the pizza name and size.
4. **Cart Management**: View your cart, add more pizzas, or remove pizzas as needed.
5. **Order Confirmation**: Confirm your order, choose your payment mode, and complete the order process.
6. **Order History**: View your past orders and check their current status.
7. **Order Cancellation**: Cancel your orders if necessary, with appropriate refund handling for online payments.

## Project Structure

```plaintext
pizza-ordering-system/
│
├── data/
│   ├── pizzas.csv
│   ├── users.csv
│   └── orders.csv
│
├── modules/
│   ├── authentication.py
│   ├── billing.py
│   ├── cart.py
│   ├── menu.py
│   └── orders.py
│
├── main.py
├── README.md
└── requirements.txt
