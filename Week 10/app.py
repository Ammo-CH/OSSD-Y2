import tkinter as tk
from tkinter import messagebox

def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Fields cannot be empty")
        return

    with open("test.txt", "a") as f:
        f.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Account Created Successfully")
    sign_in_window()


def sign_in():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("test.txt", "r") as f:
            users = f.readlines()

        for user in users:
            stored_user, stored_pass = user.strip().split(",")

            if username == stored_user and password == stored_pass:
                messagebox.showinfo("Success", "Login Successful")
                main_menu()
                return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users found. Please Sign Up first.")


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def sign_in_window():
    clear_window()

    global username_entry, password_entry

    tk.Label(root, text="Sign In", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)
    tk.Button(root, text="Go to Sign Up", command=sign_up_window).pack()


def sign_up_window():
    clear_window()

    global username_entry, password_entry

    tk.Label(root, text="Sign Up", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)
    tk.Button(root, text="Go to Sign In", command=sign_in_window).pack()


def main_menu():
    clear_window()

    tk.Label(root, text="Welcome to Main Menu", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Logout", command=sign_in_window).pack()


root = tk.Tk()
root.title("Application")
root.geometry("300x250")

sign_in_window()

root.mainloop()