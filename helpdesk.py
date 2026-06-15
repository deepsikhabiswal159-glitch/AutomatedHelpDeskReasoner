import tkinter as tk
from tkinter import messagebox

# Theme Colors
BACKGROUND = "#f7f1e8"
PRIMARY = "#9a5d34"
TEXT = "#5c3b28"

# Data
tickets = []
open_tickets = 0
resolved_tickets = 0

# Main Window
root = tk.Tk()
root.title("CFAI Helpdesk Portal")
root.geometry("900x700")
root.configure(bg=BACKGROUND)


def clear():
    for widget in root.winfo_children():
        widget.destroy()


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
        text="Automated Helpdesk Reasoner for CFAI",
        font=("Arial", 12),
        bg=BACKGROUND,
        fg="gray"
    ).pack(pady=10)

    tk.Label(root, text="Email Address", bg=BACKGROUND).pack()
    tk.Entry(root, width=40).pack(pady=5)

    tk.Label(root, text="Password", bg=BACKGROUND).pack()
    tk.Entry(root, width=40, show="*").pack(pady=5)

    tk.Button(
        root,
        text="Login",
        width=20,
        bg=PRIMARY,
        fg="white",
        command=dashboard_page
    ).pack(pady=15)

    tk.Button(
        root,
        text="Create Account",
        width=20,
        command=signup_page
    ).pack()


def signup_page():
    clear()

    tk.Label(
        root,
        text="✨ Create Account",
        font=("Arial", 26, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    tk.Label(root, text="Full Name", bg=BACKGROUND).pack()
    tk.Entry(root, width=40).pack(pady=5)

    tk.Label(root, text="Email Address", bg=BACKGROUND).pack()
    tk.Entry(root, width=40).pack(pady=5)

    tk.Label(root, text="Password", bg=BACKGROUND).pack()
    tk.Entry(root, width=40, show="*").pack(pady=5)

    tk.Label(root, text="Confirm Password", bg=BACKGROUND).pack()
    tk.Entry(root, width=40, show="*").pack(pady=5)

    tk.Button(
        root,
        text="Create Account",
        width=20,
        bg=PRIMARY,
        fg="white",
        command=dashboard_page
    ).pack(pady=15)

    tk.Button(
        root,
        text="Back to Login",
        command=login_page
    ).pack()


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
        text=f"📂 Open Tickets: {open_tickets}",
        font=("Arial", 14),
        bg=BACKGROUND
    ).pack()

    tk.Label(
        root,
        text=f"✅ Resolved Tickets: {resolved_tickets}",
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

    if len(tickets) == 0:
        tk.Label(
            root,
            text="No tickets created yet",
            bg=BACKGROUND
        ).pack()
    else:
        for ticket in tickets[-5:]:
            tk.Label(
                root,
                text=f"• {ticket['title']} ({ticket['priority']})",
                bg=BACKGROUND
            ).pack()

    tk.Button(
        root,
        text="Create Ticket",
        width=20,
        bg=PRIMARY,
        fg="white",
        command=create_ticket_page
    ).pack(pady=15)

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

    title_entry = tk.Entry(root, width=50)
    title_entry.pack(pady=5)

    tk.Label(root, text="Category", bg=BACKGROUND).pack()

    category_var = tk.StringVar(value="Technical Issue")

    tk.OptionMenu(
        root,
        category_var,
        "Technical Issue",
        "Course Access",
        "Account Problem",
        "Fee Related",
        "Other"
    ).pack(pady=5)

    tk.Label(root, text="Priority", bg=BACKGROUND).pack()

    priority_var = tk.StringVar(value="Medium")

    tk.OptionMenu(
        root,
        priority_var,
        "Low",
        "Medium",
        "High"
    ).pack(pady=5)

    tk.Label(root, text="Issue Description", bg=BACKGROUND).pack()

    description = tk.Text(root, width=50, height=8)
    description.pack(pady=10)

    def submit_ticket():
        global open_tickets

        ticket = {
            "title": title_entry.get(),
            "category": category_var.get(),
            "priority": priority_var.get()
        }

        tickets.append(ticket)
        open_tickets += 1

        messagebox.showinfo(
            "Success",
            "Ticket Submitted Successfully!"
        )

        dashboard_page()

    tk.Button(
        root,
        text="Submit Ticket",
        bg=PRIMARY,
        fg="white",
        command=submit_ticket
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        command=dashboard_page
    ).pack()


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
            msg = "🔒 Please use the password reset option."
        elif "course" in text:
            msg = "📚 Please contact the course coordinator."
        elif "fee" in text:
            msg = "💳 Please visit the Accounts Department."
        elif "login" in text:
            msg = "👤 Try resetting your credentials."
        else:
            msg = "🤖 Please create a support ticket."

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


# Start App
login_page()
root.mainloop()