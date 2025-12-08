import tkinter as tk
from storage import load_data

REFRESH_MS = 2000  # refresh every 2 seconds

def update_display(now_label, waiting_label):
    customers_list, _, now_serving = load_data()

    # Update "Now Serving"
    if now_serving:
        now_label.config(text=f"Now Serving: {now_serving}")
    else:
        now_label.config(text="Now Serving: None")

    # Update waiting queue display
    if not customers_list:
        waiting_label.config(text="Waiting: No customers")
    else:
        tickets = [str(c.ticket) for c in customers_list]
        waiting_label.config(text="Waiting: " + ", ".join(tickets))

    now_label.after(REFRESH_MS, update_display, now_label, waiting_label)

def main():
    root = tk.Tk()
    root.title("Queue Display")

    now_label = tk.Label(root, text="Now Serving: --",
                         font=("Arial", 48), pady=20)
    now_label.pack()

    waiting_label = tk.Label(root, text="Waiting: ",
                             font=("Arial", 32), pady=20)
    waiting_label.pack()

    update_display(now_label, waiting_label)
    root.mainloop()

if __name__ == "__main__":
    main()
