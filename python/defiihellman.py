import tkinter as tk
from tkinter import messagebox

# Power function to return value of a^b mod P
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

# Function to compute the secret keys
def compute_keys():
    try:
        P = int(entry_P.get())
        G = int(entry_G.get())
        a = int(entry_a.get())
        b = int(entry_b.get())

        x = power(G, a, P)
        y = power(G, b, P)

        ka = power(y, a, P)  # Secret key for Alice
        kb = power(x, b, P)  # Secret key for Bob

        result_Alice.set(f"Secret key for Alice: {ka}")
        result_Bob.set(f"Secret key for Bob: {kb}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

# Create the main window
window = tk.Tk()
window.title("Diffie-Hellman Key Exchange")

# Create and place the widgets
tk.Label(window, text="Prime number P:").grid(row=0, column=0, padx=10, pady=10)
entry_P = tk.Entry(window)
entry_P.grid(row=0, column=1)

tk.Label(window, text="Primitive root G:").grid(row=1, column=0, padx=10, pady=10)
entry_G = tk.Entry(window)
entry_G.grid(row=1, column=1)

tk.Label(window, text="Alice's private key a:").grid(row=2, column=0, padx=10, pady=10)
entry_a = tk.Entry(window)
entry_a.grid(row=2, column=1)

tk.Label(window, text="Bob's private key b:").grid(row=3, column=0, padx=10, pady=10)
entry_b = tk.Entry(window)
entry_b.grid(row=3, column=1)

result_Alice = tk.StringVar()
tk.Label(window, textvariable=result_Alice).grid(row=4, columnspan=2, padx=10, pady=10)

result_Bob = tk.StringVar()
tk.Label(window, textvariable=result_Bob).grid(row=5, columnspan=2, padx=10, pady=10)

tk.Button(window, text="Compute Secret Keys", command=compute_keys).grid(row=6, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()
