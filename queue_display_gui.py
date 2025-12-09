
import customtkinter as ctk
from storage import load_data

REFRESH_MS = 2000
last_serving = None


class QueueDisplay(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Queue Display")
        self.geometry("900x500")

        # ---- Main Layout ----
        self.now_frame = ctk.CTkFrame(self)
        self.now_frame.pack(fill="x", padx=20, pady=(20, 10))

        self.now_label_title = ctk.CTkLabel(
            self.now_frame,
            text="NOW SERVING",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.now_label_title.pack(pady=(10, 0))

        self.now_number_label = ctk.CTkLabel(
            self.now_frame,
            text="--",
            font=ctk.CTkFont(size=100, weight="bold")
        )
        self.now_number_label.pack(pady=10)

        self.waiting_frame = ctk.CTkFrame(self)
        self.waiting_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.waiting_label = ctk.CTkLabel(
            self.waiting_frame,
            text="Waiting Tickets",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.waiting_label.pack(anchor="w", padx=10, pady=(10, 0))

        self.waiting_box = ctk.CTkTextbox(
            self.waiting_frame,
            font=ctk.CTkFont(size=18),
            height=150
        )
        self.waiting_box.pack(fill="both", expand=True, padx=10, pady=10)

        # Start auto-refresh
        self.update_display()

    def update_display(self):
        global last_serving

        customers_list, _, now_serving = load_data()

        # Update "Now Serving"
        if now_serving != last_serving:
            last_serving = now_serving
            if now_serving:
                self.now_number_label.configure(text=str(now_serving))
            else:
                self.now_number_label.configure(text="--")

        # Update waiting list
        self.waiting_box.delete("1.0", "end")
        if customers_list:
            tickets = ", ".join(str(c.ticket) for c in customers_list)
            self.waiting_box.insert("end", tickets)
        else:
            self.waiting_box.insert("end", "No customers waiting.")

        # Schedule next refresh
        self.after(REFRESH_MS, self.update_display)


if __name__ == "__main__":
    app = QueueDisplay()
    app.mainloop()
