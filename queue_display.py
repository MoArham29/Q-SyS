import tkinter as tk
from storage import load_data

REFRESH_MS = 2000  # refresh every 2 seconds


last_serving = None  # to detect when the number changes


def flash_now_serving(label, count=0):
    """Flash the 'Now Serving' label a few times when number changes."""
    if count < 6:  # 6 flashes (3 on/off cycles)
        current_color = label.cget("foreground")
        new_color = "red" if current_color != "red" else "black"
        label.config(foreground=new_color)
        label.after(300, flash_now_serving, label, count + 1)
    else:
        label.config(foreground="red")  # final color


def update_display(now_label, waiting_label):
    global last_serving

    customers_list, _, now_serving = load_data()

    # Detect number change to trigger flash animation
    if now_serving != last_serving:
        flash_now_serving(now_label)
        last_serving = now_serving

    # Update "Now Serving"
    if now_serving:
        now_label.config(text=f"{now_serving}")
    else:
        now_label.config(text="--")

    # Update waiting queue
    if customers_list:
        tickets = ", ".join(str(c.ticket) for c in customers_list)
        waiting_label.config(text="Waiting: " + tickets)
    else:
        waiting_label.config(text="Waiting: None")

    now_label.after(REFRESH_MS, update_display, now_label, waiting_label)


def main():
    root = tk.Tk()
    root.title("Queue Display")


    now_label = tk.Label(
        root,
        text="--",
        font=("DS-Digital", 150),  # DIGITAL CLOCK STYLE FONT
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
