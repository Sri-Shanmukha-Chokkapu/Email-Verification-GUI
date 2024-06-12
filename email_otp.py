# Import necessary modules
import random
import smtplib  # Simple Mail Transfer Protocol Module
from tkinter import *  # Popular GUI library
from tkinter import messagebox  # Popup dialog Box

# Function to generate a 6-digit random OTP
def generate_random_otp():
    random_code = ''
    for i in range(6):
        random_digit = random.randint(0, 9)
        random_code += str(random_digit)
    return random_code

# Global variables for sender's email credentials and OTP components
sender_email = 'xyz@gmail.com'
sender_password = 'password'
generated_otp = None
otp_label = None
otp_entry = None
verify_button = None
resend_button = None
send_otp_button = None

# Connect to SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()

# Function to connect to SMTP server and send OTP email
def connect_to_sender_smtp():
    recipient_email = receiver_email_entry.get()
    try:
        smtp_server.login(sender_email, sender_password)
        send_otp_email(recipient_email, smtp_server)
        messagebox.showinfo("Success", "OTP sent successfully to the provided email.")
        display_otp_section()  # Display OTP section after successful sending
        send_otp_button.destroy()  # Destroy the "Send OTP" button
    except Exception as e:
        # Print the actual error message for debugging purposes
        print(f"Error: {e}")
        messagebox.showerror("Error", "An error occurred while sending OTP. Please try again later.")

# Function to resend OTP email
def resend_otp():
    recipient_email = receiver_email_entry.get()
    send_otp_email(recipient_email, smtp_server)
    smtp_server.quit()

# Function to send OTP email
def send_otp_email(recipient_email, smtp_server):
    global generated_otp  # Access global variable
    generated_otp = generate_random_otp()  # Generate new OTP
    otp_message = f"Hello! \n This is your OTP: {generated_otp}"
    smtp_server.sendmail(sender_email, recipient_email, otp_message)

# Function to verify entered OTP
def verify_otp():
    user_entered_otp = otp_entry.get()
    if user_entered_otp == generated_otp:
        messagebox.showinfo("Success", "OTP verified successfully!\nAccess Granted")
        # Clear OTP and verification section after successful verification
        otp_label.destroy()
        otp_entry.destroy()
        verify_button.destroy()
        resend_button.destroy()
        create_send_otp_button()  # calling function
    else:
        messagebox.showerror("Incorrect OTP", "The entered OTP is incorrect.\nAccess Denied")

# Function to display OTP section
def display_otp_section():
    # Access global variables
    global generated_otp, otp_label, otp_entry, verify_button, resend_button

    # OTP Label
    otp_label = Label(otp_window, text="Enter OTP :", font=("Arial", 16, "bold italic"), bg="#BFBEF3", fg="#f08785")
    otp_label.place(x=50, y=150)

    # OTP Input Box
    otp_entry = Entry(otp_window, width=10, fg="black", bg="white", font=("Arial", 20), borderwidth=0,
                      highlightthickness=0, highlightbackground='#BDBDBD')
    otp_entry.place(x=150, y=150)

    # OTP Verify Button
    verify_button = Button(otp_window, text="Verify", width=10, height=1, bg="#0B58CA", fg="#DBDD76",
                           font=("Arial", 14, "bold"), command=verify_otp, borderwidth=0, highlightthickness=1,
                           highlightbackground='#BFBEF3')
    verify_button.place(x=280, y=220)

    # Resend OTP Button
    resend_button = Button(otp_window, text="Resend OTP", width=12, height=1, bg="#FFCC99", fg="#79E6B2",
                           font=("Arial", 12, "bold"), command=resend_otp, borderwidth=0, highlightthickness=1,
                           highlightbackground='#BFBEF3')
    resend_button.place(x=100, y=250)

# Tkinter GUI setup with enhancements
otp_window = Tk()
otp_window.title('Email OTP Verification System')
otp_window.geometry('800x500')
otp_window.config(bg="#BFBEF3")

# Heading
heading = Label(otp_window, text="Email OTP Verification", font=("Comic Sans MS", 28, "bold"), bg="#BFBEF3",
                fg="#EA5099")
heading.place(x=250, y=20)

# Email section(Label and Input Box)
email_label = Label(otp_window, text="Email Id:", font=("Arial", 16, "bold italic"), bg="#BFBEF3", fg="#f08785")
email_label.place(x=50, y=100)

receiver_email_entry = Entry(otp_window, width=35, font=("Arial", 20,), bg="white", fg="black", borderwidth=0,
                             highlightthickness=0, highlightbackground='#BDBDBD')
receiver_email_entry.place(x=150, y=100)

# Function to create send OTP button
def create_send_otp_button():
    global send_otp_button

    send_otp_button = Button(otp_window, text="Send OTP", width=12, height=1, fg="#c5c829",
                             font=("Arial", 14, "bold"), command=connect_to_sender_smtp, borderwidth=0,
                             highlightthickness=1, highlightbackground='#BFBEF3')
    send_otp_button.place(x=280, y=150)

# Call the function
create_send_otp_button()

# Run the Tkinter main loop
otp_window.mainloop()