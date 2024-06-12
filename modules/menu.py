import csv

def display_menu(pizzas):
    print(" " * 34, "Here are the available Pizzas in our shop\n")
    print(" " * 25, "-" * 55)
    print(" " * 25, f"| {'Sr. No.':<8} | {'PIZZA':<15} | {'SIZE':<10} | {'PRICE (RS)':<10}|")
    print(" " * 25, "-" * 55)
    for idx, (pizza, size, price) in enumerate(pizzas, start=1):
        print(" " * 25, f"| {idx:<8} | {pizza:<15} | {size:<10} | {price:<10}|")
    print(" " * 25, "-" * 55)

def load_pizzas():
    with open("data/pizzas.csv", "r") as fd:
        reader = csv.reader(fd)
        pizzas = [(row[0], row[1], int(row[2])) for row in reader]
    return pizzas

def get_pizza_count():
    while True:
        try:
            count = int(input("Please enter how many pizzas do you want to order: "))
            return count
        except ValueError:
            print("Please enter an integer value only")

def get_most_similar_word(word, pizzas):
    syllable = set(word)
    max_count = 0
    similar_pizza = ()
    if word.upper() == 'Q':
        return None
    for pizza in pizzas:
        count = sum(1 for y in pizza[0] if y in syllable)
        if count > max_count:
            max_count = count
            similar_pizza = pizza
    return similar_pizza