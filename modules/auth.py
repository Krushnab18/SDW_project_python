import csv
from getpass import getpass
import hashlib
import re

class User:
    def __init__(self, name, address, mob_no, emailId, passWord):
        self.name = name
        self.address = address
        self.mob_no = mob_no
        self.emailId = emailId
        self.passWord = passWord

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def validate_mobile(mob_no):
    regex = r'^\d{10}$'
    return re.match(regex, mob_no)

def create_new_user():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    mob_no = input("Enter your mobile number: ")
    while not validate_mobile(mob_no):
        print("Invalid mobile number. It should be exactly 10 digits.")
        mob_no = input("Enter your mobile number: ")
    emailId = input("Enter your email address: ")
    while not validate_email(emailId):
        print("Invalid email format.")
        emailId = input("Enter your email address: ")
    while True:
        passWord = getpass("Create password for your account: ")
        password_confirm = getpass("Please confirm your password: ")
        if password_confirm != passWord:
            print("Confirm password does not match.")
        else:
            break
    newUser = User(name, address, mob_no, emailId, hash_password(passWord))
    save_user_to_csv(newUser)
    return newUser

def validate_login():
    user_id = input("Please enter your email address: ")
    password = getpass("Please enter your password: ")
    hashed_password = hash_password(password)
    try:
        with open("data/users.csv", "r") as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row[3] == user_id and row[4] == hashed_password:
                    print("Login successful")
                    return User(row[0], row[1], row[2], row[3], row[4])
    except FileNotFoundError:
        print("User data file not found.")
    return None

def save_user_to_csv(user):
    try:
        with open("data/users.csv", "a", newline='') as fd:
            writer = csv.writer(fd)
            writer.writerow([user.name, user.address, user.mob_no, user.emailId, user.passWord])
    except Exception as e:
        print(f"An error occurred while saving the user: {e}")