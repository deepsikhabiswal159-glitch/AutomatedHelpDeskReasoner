import tkinter as tk
from tkinter import messagebox

# Theme Colors
BACKGROUND = "#f7f1e8"
PRIMARY = "#9a5d34"
TEXT = "#5c3b28"

# Main Window
root = tk.Tk()
root.title("CFAI Helpdesk Portal")
root.geometry("900x650")
root.configure(bg=BACKGROUND)


# Clear Screen
def clear():
    for widget in root.winfo_children():
        widget.destroy()


# Login Page
def login_page():
    clear()

    tk.Label(
        root,
        text="🎧 Helpdesk Portal",
        font=("Arial", 28, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    tk.Label(
        root,
        text="Automated Helpdesk Reasoner",
        font=("Arial", 12),
        bg=BACKGROUND,
        fg="gray"
    ).pack()

    tk.Entry(root, width=35).pack(pady=10)

    tk.Entry(root, width=35, show="*").pack(pady=10)

    tk.Button(
        root,
        text="Login",
        bg=PRIMARY,
        fg="white",
        width=20,
        command=dashboard_page
    ).pack(pady=15)

    tk.Button(
        root,
        text="Create Account",
        width=20,
        command=signup_page
    ).pack()


# Signup Page
def signup_page():
    clear()

    tk.Label(
        root,
        text="✨ Create Account",
        font=("Arial", 26, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    tk.Entry(root, width=40).pack(pady=8)
    tk.Entry(root, width=40).pack(pady=8)
    tk.Entry(root, width=40, show="*").pack(pady=8)
    tk.Entry(root, width=40, show="*").pack(pady=8)

    tk.Button(
        root,
        text="Create Account",
        bg=PRIMARY,
        fg="white",
        width=20,
        command=dashboard_page
    ).pack(pady=15)

    tk.Button(
        root,
        text="Back to Login",
        command=login_page
    ).pack()


# Dashboard Page
def dashboard_page():
    clear()

    tk.Label(
        root,
        text="🎧 Helpdesk Dashboard",
        font=("Arial", 24, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    tk.Label(
        root,
        text="Open Tickets: 12",
        font=("Arial", 14),
        bg=BACKGROUND
    ).pack()

    tk.Label(
        root,
        text="Pending Tickets: 5",
        font=("Arial", 14),
        bg=BACKGROUND
    ).pack()

    tk.Label(
        root,
        text="Resolved Tickets: 20",
        font=("Arial", 14),
        bg=BACKGROUND
    ).pack()

    tk.Label(
        root,
        text="Recent Tickets",
        font=("Arial", 18, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    tk.Label(
        root,
        text="• Password Reset Request - Open",
        bg=BACKGROUND
    ).pack()

    tk.Label(
        root,
        text="• Course Access Issue - Pending",
        bg=BACKGROUND
    ).pack()

    tk.Label(
        root,
        text="• LMS Login Problem - Resolved",
        bg=BACKGROUND
    ).pack()

    tk.Button(
        root,
        text="Create Ticket",
        bg=PRIMARY,
        fg="white",
        width=20,
        command=create_ticket_page
    ).pack(pady=10)

    tk.Button(
        root,
        text="Helpdesk Chatbot",
        width=20,
        command=chatbot_page
    ).pack(pady=5)

    tk.Button(
        root,
        text="Logout",
        width=20,
        command=login_page
    ).pack(pady=5)


# Create Ticket Page
def create_ticket_page():
    clear()

    tk.Label(
        root,
        text="🎫 Create Support Ticket",
        font=("Arial", 24, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    tk.Label(root, text="Issue Title", bg=BACKGROUND).pack()
    tk.Entry(root, width=50).pack(pady=5)

    tk.Label(root, text="Category", bg=BACKGROUND).pack()
    tk.Entry(root, width=50).pack(pady=5)

    tk.Label(root, text="Issue Description", bg=BACKGROUND).pack()

    issue_box = tk.Text(root, width=50, height=8)
    issue_box.pack(pady=10)

    tk.Button(
        root,
        text="Submit Ticket",
        bg=PRIMARY,
        fg="white",
        command=lambda: messagebox.showinfo(
            "Success",
            "Ticket Submitted Successfully!"
        )
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        command=dashboard_page
    ).pack()


# Chatbot Page
def chatbot_page():
    clear()

    tk.Label(
        root,
        text="🤖 Helpdesk Assistant",
        font=("Arial", 24, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    question = tk.Entry(root, width=50)
    question.pack(pady=10)

    response = tk.Label(
        root,
        text="",
        bg=BACKGROUND,
        wraplength=500
    )
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
            msg = "Please create a support ticket for assistance."

        response.config(text=msg)

    tk.Button(
        root,
        text="Send",
        bg=PRIMARY,
        fg="white",
        command=send
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        command=dashboard_page
    ).pack()


# Start Application
login_page()
root.mainloop()