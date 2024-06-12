import csv

def save_user_to_csv(user):
    with open("data/users.csv", "a") as fd:
        writer = csv.writer(fd, newline = "\n")
        writer.writerow([user.name, user.address, user.mob_no, user.emailId, user.passWord])

def isPizzaInPizzas(pizza, pizzas):
    for row in pizzas:
        if row[0] == pizza:
            return True
    return False