import csv
from getpass import getpass
from modules.utils import save_user_to_csv

class User:
    def __init__(self, name, address, mob_no, emailId, passWord):
        self.name = name
        self.address = address
        self.mob_no = mob_no
        self.emailId = emailId
        self.passWord = passWord

def create_new_user():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    mo_no = input("Enter your mobile no: ")
    emailId = input("Enter your email address: ")
    while True:
        print("Create password for your account ", end="")
        passWord = getpass()
        print("Please confirm your ", end="")
        password = getpass()
        if password != passWord:
            print("Confirm password does not match.")
        else:
            break
    newUser = User(name, address, mo_no, emailId, passWord)
    save_user_to_csv(newUser)
    return newUser

def validate_login():
    user_id = input("Please enter your email address: ")
    print("Please enter your ", end="")
    password = getpass()
    with open("data/users.csv", "r") as fd:
        reader = csv.reader(fd)
        for row in reader:
            if row[3] == user_id and row[4] == password:
                print("Login successful")
                return User(row[0], row[1], row[2], row[3], row[4])
    return None