import tkinter as tk
from storage import load_data

REFRESH_MS = 2000  # Refresh interval (2 seconds)
last_serving = None  # Track previous serving number


def flash_now_serving(label, count=0):
    """Flash the 'Now Serving' number when it changes."""
    if count < 6:  # Flash 6 times (3 on/off)
        new_color = "red" if label.cget("foreground") != "red" else "black"
        label.config(foreground=new_color)
        label.after(300, flash_now_serving, label, count + 1)
    else:
        label.config(foreground="red")  # Final color


def update_display(now_label, waiting_label):
    global last_serving

    customers_list, _, now_serving = load_data()

    # Trigger the flash animation if number changed
    if now_serving != last_serving:
        flash_now_serving(now_label)
        last_serving = now_serving

    # Update "Now Serving"
    now_label.config(text=now_serving if now_serving else "--")

    # Update waiting list
    if customers_list:
        tickets = ", ".join(str(c.ticket) for c in customers_list)
        waiting_label.config(text=f"Waiting: {tickets}")
    else:
        waiting_label.config(text="Waiting: None")

    now_label.after(REFRESH_MS, update_display, now_label, waiting_label)


def main():
    root = tk.Tk()
    root.title("Queue Display")

    now_label = tk.Label(
        root,
        text="--",
        font=("DS-Digital", 150),
        fg="red",
        pady=50
    )
    now_label.pack()

    waiting_label = tk.Label(
        root,
        text="Waiting:",
        font=("Arial", 40),
        pady=20
    )
    waiting_label.pack()

    update_display(now_label, waiting_label)
    root.mainloop()


if __name__ == "__main__":
    main()
