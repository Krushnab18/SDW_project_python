from fpdf import FPDF

def generate_bill(cart, total_payment, current_date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "Thank you for your order!", ln = True, align = "C")
    pdf.cell(200, 10, txt = "Your Order details are here:", ln = True, align = "C")
    pdf.cell(200, 10, txt = "", ln = True, align = "C")
    pdf.cell(200, 10, txt = current_date, ln = True, align = "C")
    pdf.cell(200, 10, txt = "", ln = True, align = "C")
    pdf.cell(200, 10, txt = "", ln = True, align = "C")
    pdf.cell(200, 10, txt = "", ln = True, align = "C")

    for idx, (pizza, size, price) in enumerate(cart, start=1):
        pdf.cell(200, 10, txt = f"  {idx}    {pizza}   {size}    {price}", ln = True, align = "C")
    pdf.cell(200, 10, txt = "", ln = True, align = "C")
    pdf.cell(200, 10, txt = "", ln = True, align = "C")
    pdf.cell(200, 10, txt = f"Total payment --> {total_payment}", ln = True, align = "C")
    pdf.output("order_bill.pdf")