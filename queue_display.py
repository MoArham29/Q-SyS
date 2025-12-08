# queue_display.py
import tkinter as tk
from storage import load_data

REFRESH_MS = 2000  # refresh every 2 seconds

def format_waiting_text():
    customers_list, _ = load_data()
    if not customers_list:
        return "No customers waiting"

    # show ticket numbers in order
    tickets = [str(c.ticket) for c in customers_list]
    return "Waiting tickets:\n" + ", ".join(tickets)

def update_label(label):
    label.config(text=format_waiting_text())
    label.after(REFRESH_MS, update_label, label)

def main():
    root = tk.Tk()
    root.title("Queue Display")

    label = tk.Label(
        root,
        text="Loading queue...",
        font=("Arial", 32),
        padx=40,
        pady=40,
        justify="center"
    )
    label.pack(expand=True, fill="both")

    update_label(label)
    root.mainloop()

if __name__ == "__main__":
    main()
