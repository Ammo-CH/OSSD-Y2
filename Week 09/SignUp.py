import tkinter as tk
from tkinter import messagebox

def save_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    print("walue")

    if username == "" or password == "":
        messagebox.showerror("Error", "Fields cannot be empty")
        return
    print("rrrrrrrr")
    with open("test.txt", "a") as f:
        f.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Account Created Successfully")


def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    print("svdfsf")
    try:
        with open("test.txt", "r") as f:
            users = f.readlines()

        for user in users:
            stored_user, stored_pass = user.strip().split(",")

            if username == stored_user and password == stored_pass:
                messagebox.showinfo("Success", "Login Successful")
                return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users found. Please Sign Up first.")


root = tk.Tk()
root.title("Sign In / Sign Up")
root.geometry("300x250")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Sign In", command=check_credentials).pack(pady=5)
tk.Button(root, text="Sign Up", command=save_credentials).pack(pady=5)

root.mainloop()