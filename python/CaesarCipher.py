# remove the spacing in the output so to make it harder to predict and stay protected

import tkinter as tk

def encrypt(text, shift):
    text = text.replace(" ", "")  # Remove spaces before encryption
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    text = text.replace(" ", "")  # Remove spaces before decryption
    return encrypt(text, -shift)

def on_encrypt():
    text = input_text.get("1.0", tk.END).rstrip()  # remove trailing newline and spaces
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def on_decrypt():
    text = input_text.get("1.0", tk.END).rstrip()  # remove trailing newline and spaces
    shift = int(shift_entry.get())
    decrypted_text = decrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher")

# Input Text
tk.Label(root, text="Input Text:").pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Shift Entry
tk.Label(root, text="Shift:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Buttons for Encryption and Decryption
encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.pack()

# Output Text
tk.Label(root, text="Output Text:").pack()
output_text = tk.Text(root, height=5, width=40)
output_text.pack()
<<<<<<< HEAD

=======
#remive spacing in the output
>>>>>>> 18d6acc09bbb6975ef6b3a1af65e80ca726469e1
root.mainloop()
