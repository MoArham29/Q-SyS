# customer_app_gui.py

import customtkinter as ctk
from tkinter import messagebox
from system import QueueSystem


class CustomerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.system = QueueSystem()

        self.title("Customer Check-In")
        self.geometry("600x450")

        ctk.set_appearance_mode("dark")       # Dark theme
        ctk.set_default_color_theme("green")  # Accent colour

        # ---- Title ----
        self.title_label = ctk.CTkLabel(
            self,
            text="Customer Check-In",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        self.title_label.pack(pady=20)

        # ---- Form Frame ----
        form_frame = ctk.CTkFrame(self)
        form_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Name
        self.name_label = ctk.CTkLabel(form_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name_entry = ctk.CTkEntry(form_frame, width=300)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Reason
        self.reason_label = ctk.CTkLabel(form_frame, text="Reason for Visit:")
        self.reason_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.reason_entry = ctk.CTkEntry(form_frame, width=300)
        self.reason_entry.grid(row=1, column=1, padx=10, pady=10)

        # Phone (optional)
        self.phone_label = ctk.CTkLabel(form_frame, text="Phone (optional):")
        self.phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.phone_entry = ctk.CTkEntry(form_frame, width=300)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)

        # Email (required)
        self.email_label = ctk.CTkLabel(form_frame, text="Email (required):")
        self.email_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.email_entry = ctk.CTkEntry(form_frame, width=300)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)

        # ---- Submit Button ----
        self.submit_button = ctk.CTkButton(
            self,
            text="Register",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.register_customer
        )
        self.submit_button.pack(pady=15)

        # ---- Ticket Output Label ----
        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=18)
        )
        self.result_label.pack(pady=10)

    def register_customer(self):
        name = self.name_entry.get().strip()
        reason = self.reason_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Name is required.")
            return
        if not email:
            messagebox.showerror("Error", "Email is required.")
            return
        if not reason:
            messagebox.showerror("Error", "Reason is required.")
            return

        customer = self.system.register_customer(name, reason, phone, email)

        # Show success + ticket number
        self.result_label.configure(
            text=f"Registration successful! Your ticket number is {customer.ticket}."
        )
        messagebox.showinfo(
            "Registered",
            f"Thank you {customer.name}.\nYour ticket number is {customer.ticket}.\n"
            f"A confirmation email has been sent to {customer.email}."
        )

        # Clear fields
        self.name_entry.delete(0, "end")
        self.reason_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")


if __name__ == "__main__":
    app = CustomerApp()
    app.mainloop()
