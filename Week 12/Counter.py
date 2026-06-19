import tkinter as tk

count = 0


def update_label():
    counter.config(text=str(count))


def increment():
    global count
    count += 1
    update_label()


def decrement():
    global count
    count -= 1
    update_label()


def reset():
    global count
    count = 0
    update_label()


root = tk.Tk()
root.title("Counter App")
root.geometry("250x200")


counter = tk.Label(root, text="0", font=("Arial", 20))
counter.pack(pady=10)


tk.Button(root, text="Increment", command=increment).pack(pady=5)
tk.Button(root, text="Decrement", command=decrement).pack(pady=5)
tk.Button(root, text="Reset", command=reset).pack(pady=5)


root.mainloop()