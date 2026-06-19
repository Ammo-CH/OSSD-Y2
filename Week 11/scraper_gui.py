from scrapper import get_cars_data
import tkinter as tk
from tkinter import ttk, messagebox


# ---------------- FUNCTION ----------------

def set_textarea(data):
    textarea.delete(1.0, tk.END)

    if not data:
        status_label.config(text="No data found ❌")
        return

    status_label.config(text=f"Found {len(data)} results ✅")

    for car in data:
        textarea.insert(tk.END, f"🚗 {car['name']}  |  💰 {car['price']}\n")


def search():
    car = dropdown.get()

    if car == "":
        messagebox.showerror("Error", "Please select a brand")
        return

    status_label.config(text="Searching... 🔍")
    root.update()

    data = get_cars_data(car)
    set_textarea(data)


# ---------------- MAIN APP ----------------

def start_app():
    splash.destroy()
    main_window()


# ---------------- MAIN WINDOW ----------------

def main_window():
    global root, dropdown, textarea, status_label

    root = tk.Tk()
    root.title("🚗 Car Price Scraper")
    root.geometry("750x520")
    root.config(bg="#f5f5f5")


    # HEADER
    header = tk.Label(
        root,
        text="Car Price Scraper Dashboard",
        font=("Arial", 18, "bold"),
        bg="#f5f5f5"
    )
    header.pack(pady=10)


    # BRANDS
    frame = tk.Frame(root, bg="#f5f5f5")
    frame.pack(pady=10)

    car_manufact = [
        'toyota',
        'honda',
        'suzuki',
        'kia',
        'hyundai',
        'byd',
        'changan'
    ]

    dropdown = ttk.Combobox(frame, values=car_manufact, font=("Arial", 12), width=25)
    dropdown.set("Select Brand")
    dropdown.grid(row=0, column=0, padx=10)

    search_btn = tk.Button(
        frame,
        text="🔍 Search",
        command=search,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 11, "bold")
    )
    search_btn.grid(row=0, column=1, padx=10)


    # STATUS
    status_label = tk.Label(root, text="Ready to search 🚀", bg="#f5f5f5", fg="blue")
    status_label.pack()


    # TEXT AREA + SCROLL
    text_frame = tk.Frame(root)
    text_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    textarea = tk.Text(
        text_frame,
        height=18,
        width=80,
        yscrollcommand=scrollbar.set,
        font=("Consolas", 10)
    )
    textarea.pack()

    scrollbar.config(command=textarea.yview)

    root.mainloop()


# ---------------- SPLASH SCREEN (NO TERMINAL START) ----------------

splash = tk.Tk()
splash.title("Loading...")
splash.geometry("300x150")

tk.Label(
    splash,
    text="🚗 Car Scraper Loading...",
    font=("Arial", 12, "bold")
).pack(expand=True)

splash.after(1500, start_app)  # auto start main UI

splash.mainloop()