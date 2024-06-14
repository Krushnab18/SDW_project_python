import csv
import hashlib
def save_user_to_csv(user):
    with open("data/users.csv", "a") as fd:
        writer = csv.writer(fd, newline = "\n")
        writer.writerow([user.name, user.address, user.mob_no, user.emailId, user.passWord])

def isPizzaInPizzas(pizza, pizzas):
    for row in pizzas:
        if row[0] == pizza:
            return True
    return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

from fpdf import FPDF
from modules.cart import total
import os

class PDF(FPDF):
    def header(self):
        self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Pizza Order System', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Ekta park society, Wakdewadi, pune - 413725', 0, 1, 'C')
        self.cell(0, 10, 'Phone: +91-8888888888, Email: pizzaordersystem@gmail.com', 0, 1, 'C')
        self.cell(0, 10, '', 0, 1)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'C', 1)
        self.ln(10)

def generate_bill(order_id, cart, user, date):
    pdf = PDF()
    pdf.add_page()

    # Title
    pdf.chapter_title("Pizza Order Bill")

    # User Information
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Name: {user.name}", ln=True)
    pdf.cell(0, 10, txt=f"Address: {user.address}", ln=True)
    pdf.cell(0, 10, txt=f"Mobile No: {user.mob_no}", ln=True)
    pdf.cell(0, 10, txt=f"Email ID: {user.emailId}", ln=True)
    pdf.cell(0, 10, '', ln=True)  

    # Order Information
    pdf.cell(0, 10, txt=f"Order ID: {order_id}", ln=True)
    pdf.cell(0, 10, txt=f"Order Date: {date}", ln=True)
    pdf.cell(0, 10, '', ln=True)

    # Table Header
    pdf.set_font("Arial", 'B', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(70, 10, txt="Pizza", border=1, align='C', fill=True)
    pdf.cell(30, 10, txt="Size", border=1, align='C', fill=True)
    pdf.cell(30, 10, txt="Quantity", border=1, align='C', fill=True)
    pdf.cell(30, 10, txt="Price (Rs)", border=1, align='C', fill=True)
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", size=12)
    for item in cart:
        pdf.cell(70, 10, txt=item[0], border=1)
        pdf.cell(30, 10, txt=item[1], border=1, align='C')
        pdf.cell(30, 10, txt=str(item[3]), border=1, align='C')
        pdf.cell(30, 10, txt=str(item[2]), border=1, align='C')
        pdf.ln()

    # Total
    pdf.cell(70 + 30 + 30, 10, txt=f"Total: Rs {total(cart)}", border=1, align='R')
    pdf.cell(30, 10, '', border=1)

    # Save the PDF
    pdf_filename = f"bill_{order_id}.pdf"
    pdf.output(f"./Bills/{pdf_filename}")

    print(f"Bill generated and saved as {pdf_filename}")
    os.system(f"xdg-open \"{os.path.join('./Bills', pdf_filename)}\"")
    
def generate_unique_order_id():
    starting = "ABCDE"
    with open("data/orders.csv") as fp:
        reader = csv.reader(fp)
        rows = list(reader)
        length = len(rows)
        end = length + 7498
    return starting + str(end)