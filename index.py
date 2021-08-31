from tkinter import *
import os

def run():
    sender_email = str(sender_email_entry.get())
    sender_email_password  = str(sender_email_password_entry.get())
    emails_path_str = str(emails_path_entry.get())
    
    os.system(f'python3 mail_bot.py {sender_email} {sender_email_password} {emails_path_str}')
    
root = Tk()
root.geometry('1000x500')
root.title('Bulk Emailer')

sender_email_label = Label(root, text="Sender email:", width=20)
sender_email_label.place(x=100, y=100)

sender_email_password_label = Label(root, text="Sender email password:")
sender_email_password_label.place(x=100, y=150)

emails_path = Label(root, text="Emails list (csv) path:")
emails_path.place(x=100, y=200)

sender_email_entry = Entry(root, width=60)
sender_email_entry.place(x=300, y=100)

sender_email_password_entry = Entry(root)
sender_email_password_entry.place(x=300, y=150)

emails_path_entry = Entry(root, width=60)
emails_path_entry.place(x=300, y=200)

Button(root, text="Submit", width=20, command=run).place(x=180, y=380)

root.mainloop()