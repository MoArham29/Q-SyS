
import customtkinter as ctk
from tkinter import messagebox
from system import QueueSystem


class OperatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.system = QueueSystem()

        self.title("Operator Dashboard")
        self.geometry("900x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ---- Top Frame: Now Serving + Controls ----
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=20, pady=10)

        self.now_serving_label = ctk.CTkLabel(
            top_frame,
            text="Now Serving: --",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.now_serving_label.pack(side="left", padx=10, pady=10)

        self.call_next_button = ctk.CTkButton(
            top_frame,
            text="Call Next Customer",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.call_next_customer
        )
        self.call_next_button.pack(side="right", padx=10, pady=10)

        # ---- Middle Frame: Waiting List ----
        middle_frame = ctk.CTkFrame(self)
        middle_frame.pack(fill="both", expand=True, padx=20, pady=10)

        waiting_label = ctk.CTkLabel(
            middle_frame,
            text="Waiting Customers",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        waiting_label.pack(anchor="w", padx=10, pady=(10, 0))

        self.waiting_box = ctk.CTkTextbox(
            middle_frame,
            height=220,
            font=ctk.CTkFont(size=14)
        )
        self.waiting_box.pack(fill="both", expand=True, padx=10, pady=10)

        # ---- Bottom Frame: Search ----
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(fill="x", padx=20, pady=10)

        search_label = ctk.CTkLabel(bottom_frame, text="Search by ticket:")
        search_label.pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(bottom_frame, width=120)
        self.search_entry.pack(side="left", padx=5)

        self.search_button = ctk.CTkButton(
            bottom_frame, text="Search", command=self.search_ticket
        )
        self.search_button.pack(side="left", padx=5)

        self.refresh_button = ctk.CTkButton(
            bottom_frame, text="Refresh List", command=self.refresh_waiting_list
        )
        self.refresh_button.pack(side="right", padx=5)

        # Initial display
        self.refresh_waiting_list()
        self.update_now_serving_label()

    def update_now_serving_label(self):
        if self.system.now_serving:
            self.now_serving_label.configure(
                text=f"Now Serving: {self.system.now_serving}"
            )
        else:
            self.now_serving_label.configure(text="Now Serving: --")

    def refresh_waiting_list(self):
        self.waiting_box.delete("1.0", "end")
        waiting = self.system.list_waiting()
        if not waiting:
            self.waiting_box.insert("end", "No customers waiting.\n")
        else:
            for c in waiting:
                self.waiting_box.insert(
                    "end",
                    f"Ticket #{c.ticket}  |  {c.name}  |  {c.reason}  |  {c.email}\n"
                )

    def call_next_customer(self):
        next_customer = self.system.call_next()
        if next_customer:
            self.update_now_serving_label()
            self.refresh_waiting_list()
            messagebox.showinfo(
                "Next Customer",
                f"Now serving ticket #{next_customer.ticket}\n"
                f"Name: {next_customer.name}\n"
                f"An email has been sent to {next_customer.email}."
            )
        else:
            messagebox.showinfo("Queue Empty", "No customers waiting in the queue.")

    def search_ticket(self):
        ticket_str = self.search_entry.get().strip()
        if not ticket_str.isdigit():
            messagebox.showerror("Error", "Ticket must be a number.")
            return

        ticket = int(ticket_str)
        found = self.system.search_by_ticket(ticket)

        if found:
            messagebox.showinfo(
                "Customer Found",
                f"Ticket: {found.ticket}\n"
                f"Name: {found.name}\n"
                f"Reason: {found.reason}\n"
                f"Email: {found.email}\n"
                f"Phone: {found.phone}"
            )
        else:
            messagebox.showinfo("Not Found", f"No customer with ticket #{ticket}.")


if __name__ == "__main__":
    app = OperatorApp()
    app.mainloop()
