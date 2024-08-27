import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def on_encrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def on_decrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    decrypted_text = decrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

//drivercode
root = tk.Tk()
root.title("Caesar Cipher")
tk.Label(root, text="Input Text:").pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()
tk.Label(root, text="Shift:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()
encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack()
decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.pack()
tk.Label(root, text="Output Text:").pack()
output_text = tk.Text(root, height=5, width=40)
output_text.pack()


root.mainloop()
