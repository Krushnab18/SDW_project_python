from fpdf import FPDF
from modules.cart import total
import os

def generate_bill(order_id,cart, user, timestamp):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Pizza Order Bill", ln=True, align='C')

    # User Information
    pdf.cell(200, 10, txt=f"Name: {user.name}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {user.address}", ln=True)
    pdf.cell(200, 10, txt=f"Mobile No: {user.mob_no}", ln=True)
    pdf.cell(200, 10, txt=f"Email ID: {user.emailId}", ln=True)

    # Order Information
    pdf.cell(200, 10, txt=f"Order ID: {order_id}", ln=True)
    pdf.cell(200, 10, txt=f"Order Date: {timestamp}", ln=True)
    pdf.cell(200, 10, txt=" ", ln=True)
    # Table Header
    pdf.cell(50, 10, txt="Pizza", border=1)
    pdf.cell(50, 10, txt="Size", border=1)
    pdf.cell(50, 10, txt="Quantity", border=1)
    pdf.cell(50, 10, txt="Price (Rs)", border=1)
    pdf.ln()

    # Table Rows
    for item in cart:
        pdf.cell(50, 10, txt=item[0], border=1)
        pdf.cell(50, 10, txt=item[1], border=1)
        pdf.cell(50, 10, txt=str(item[3]), border=1)
        pdf.cell(50, 10, txt=str(item[2]), border=1)
        pdf.ln()

    # Total
    pdf.cell(100, 10, txt=f"Total : RS{total(cart)}", border=1)
    pdf.ln()

    # Save the PDF
    pdf_filename = f"bill_{order_id}.pdf"
    pdf.output(f"./Bills/{pdf_filename}")

    print(f"Bill generated and saved as {pdf_filename}")
    os.system(f"xdg-open \"{os.path.join('./Bills', pdf_filename)}\"")
