import pandas as pd 
import smtplib 
import tkinter as tk 
from email.message import  EmailMessage 
from tkinter import messagebox,filedialog 
from reportlab.pdfgen import canvas 
def generate_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files","*.xlsx")])
    if file_path == "":
        return 
    data = pd.read_excel(file_path)
    data.columns = data.columns.str.strip()
    print(data.columns)
    total = len(data)
    passed = (data["Status"]=="Pass").sum()
    failed = (data["Status"]=="Fail").sum()
    yet = (data["Status"]=="Yet to execute").sum()
    pdf_file = "Test Report.pdf"
    c = canvas.Canvas(pdf_file)
    c.drawString(200,750,"Test Execution Report")
    c.drawString(100,700,"Total TestCases:"+str(total))
    c.drawString(100,670,"Passed Testcases:"+str(passed))
    c.drawString(100,640,"Failed Testcases:"+str(failed))
    c.drawString(100,610,"Yet to execute"+str(yet))
    c.save()
    send_email(pdf_file)
    messagebox.showinfo("Success","Reported generated and email sent")
def send_email(pdf_file):
    sender = "tridevtsama76@gmail.com"
    receiver = "navya70135@gmail.com"
    password = "dqpv jzlq yhtq zlls"
    msg = EmailMessage()
    msg["Subject"] = "Test Report"
    msg["From"] = "navyakarnati2603@gmail.com"
    msg["To"] = "navya70135@gmail.com"
    msg.set_content("Attached thr test report.")
    file = open(pdf_file,"rb")
    file_data = file.read()
    file.close()
    msg.add_attachment(file_data,maintype="application",subtype="pdf",filename=pdf_file)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(sender,password)
    server.send_message(msg)
    server.quit()
root = tk.Tk()
root.title("Email automater Tool")
root.geometry("400x200")
label = tk.Label(root,text="Report from Excel",font=("Arial",14))
label.pack(pady=20)
button = tk.Button(root,text="select Excel File",command=generate_pdf)
button.pack(pady=10)
root.mainloop()