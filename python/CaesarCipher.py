import tkinter as tk

# Encrypt the text without spaces
def encrypt(text, shift):
    text_no_spaces = text.replace(" ", "")  # Remove spaces before encryption
    encrypted_text = ""
    for char in text_no_spaces:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

# Decrypt the text and restore spaces
def decrypt(text, shift, space_positions):
    decrypted_text = encrypt(text, -shift)  # Decrypt without spaces
    text_with_spaces = list(decrypted_text)  # Convert to list to manipulate positions
    for pos in space_positions:  # Insert spaces back
        text_with_spaces.insert(pos, " ")
    return ''.join(text_with_spaces)

# Store positions of spaces
def get_space_positions(text):
    return [i for i, char in enumerate(text) if char == " "]  # List of space positions

# Encryption button event
def on_encrypt():
    text = input_text.get("1.0", tk.END).rstrip()  # Get input text without trailing spaces
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)  # Encrypt text without spaces
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)  # Display encrypted text without spaces

# Decryption button event
def on_decrypt():
    text = input_text.get("1.0", tk.END).rstrip()  # Get input text without trailing spaces
    shift = int(shift_entry.get())
    space_positions = get_space_positions(text)  # Store original space positions
    text_no_spaces = text.replace(" ", "")  # Remove spaces for decryption
    decrypted_text = decrypt(text_no_spaces, shift, space_positions)  # Decrypt and restore spaces
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)  # Display decrypted text with spaces

# Tkinter GUI setup
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

# Run the application
root.mainloop()
#spacing removed