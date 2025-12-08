import tkinter as tk
from PIL import Image, ImageTk
from storage import load_data

BG_IMAGE_PATH = "backgrounds/89326.jpg"
REFRESH_MS = 2000

last_serving = None  # to detect changes


def flash_label(label, count=0):
    """Flash animation when now serving changes."""
    if count < 6:
        current_color = label.cget("foreground")
        new_color = "#ff4040" if current_color != "#ff4040" else "white"
        label.config(foreground=new_color)
        label.after(250, flash_label, label, count + 1)
    else:
        label.config(foreground="white")


def update_display(now_label, waiting_label):
    global last_serving

    customers_list, _, now_serving = load_data()

    # Flash animation when number changes
    if now_serving != last_serving:
        flash_label(now_label)
        last_serving = now_serving

    # Update now serving
    now_label.config(text=str(now_serving) if now_serving else "--")

    # Update waiting list
    if customers_list:
        tickets = ", ".join(str(c.ticket) for c in customers_list)
        waiting_label.config(text=f"Waiting: {tickets}")
    else:
        waiting_label.config(text="Waiting: None")

    now_label.after(REFRESH_MS, update_display, now_label, waiting_label)


def resize_background(event, bg_label, original_img):
    """Dynamically resize the background image while maintaining quality."""
    w, h = event.width, event.height
    resized = original_img.resize((w, h), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized)
    bg_label.config(image=bg_image)
    bg_label.image = bg_image


def main():
    root = tk.Tk()
    root.title("Queue Display")

   
