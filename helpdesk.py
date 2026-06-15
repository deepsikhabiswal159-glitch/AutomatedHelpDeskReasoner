import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CFAI Helpdesk Portal")
root.geometry("800x600")

# Login Page
def login_page():
    clear()

    tk.Label(root, text="🎧 Helpdesk Portal", font=("Arial", 24)).pack(pady=20)

    tk.Entry(root, width=30).pack(pady=10)
    tk.Entry(root, width=30, show="*").pack(pady=10)

    tk.Button(root, text="Login", command=dashboard_page).pack(pady=10)
    tk.Button(root, text="Create Account", command=signup_page).pack()

# Signup Page
def signup_page():
    clear()

    tk.Label(root, text="Create Account", font=("Arial", 24)).pack(pady=20)

    tk.Entry(root, width=30).pack(pady=5)
    tk.Entry(root, width=30).pack(pady=5)
    tk.Entry(root, width=30, show="*").pack(pady=5)

    tk.Button(root, text="Create Account", command=dashboard_page).pack(pady=15)
    tk.Button(root, text="Back", command=login_page).pack()

# Dashboard
def dashboard_page():
    clear()

    tk.Label(root, text="🎧 Helpdesk Dashboard", font=("Arial", 24)).pack(pady=20)

    tk.Label(root, text="Open Tickets: 12").pack()
    tk.Label(root, text="Pending: 5").pack()
    tk.Label(root, text="Resolved: 20").pack()

    tk.Button(root, text="Create Ticket", command=create_ticket_page).pack(pady=10)
    tk.Button(root, text="Chatbot", command=chatbot_page).pack(pady=10)
    tk.Button(root, text="Logout", command=login_page).pack(pady=10)

# Create Ticket
def create_ticket_page():
    clear()

    tk.Label(root, text="Create Support Ticket", font=("Arial", 20)).pack(pady=20)

    tk.Entry(root, width=40).pack(pady=5)
    tk.Entry(root, width=40).pack(pady=5)

    issue = tk.Text(root, height=5, width=40)
    issue.pack(pady=10)

    tk.Button(
        root,
        text="Submit Ticket",
        command=lambda: messagebox.showinfo("Success", "Ticket Submitted!")
    ).pack(pady=10)

    tk.Button(root, text="Back", command=dashboard_page).pack()

# Chatbot
def chatbot_page():
    clear()

    tk.Label(root, text="🤖 Helpdesk Assistant", font=("Arial", 20)).pack(pady=20)

    question = tk.Entry(root, width=50)
    question.pack(pady=10)

    response = tk.Label(root, text="", wraplength=500)
    response.pack(pady=10)

    def send():
        text = question.get().lower()

        if "password" in text:
            msg = "Please use the password reset option."
        elif "course" in text:
            msg = "Please contact the course coordinator."
        elif "fee" in text:
            msg = "Please visit the Accounts Department."
        elif "login" in text:
            msg = "Try resetting your credentials."
        else:
            msg = "Please create a support ticket."

        response.config(text=msg)

    tk.Button(root, text="Send", command=send).pack(pady=10)
    tk.Button(root, text="Back", command=dashboard_page).pack()

# Helper Function
def clear():
    for widget in root.winfo_children():
        widget.destroy()

login_page()
root.mainloop()