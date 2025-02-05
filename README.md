**Caesar Cipher Python Based Project**

![image](https://github.com/user-attachments/assets/505cac09-a93c-49b5-8128-293c37ca5ac2)

The Caesar Cipher Java Project is a simple implementation of the classic Caesar Cipher encryption algorithm. This program allows users to encrypt and decrypt messages by shifting the letters of the alphabet by a specified number of positions. The project is written in Java and is intended to provide a basic understanding of how substitution ciphers work.

How It Works:
Encrypt Function: The encrypt function shifts each letter in the input text by the given shift amount. If the character is not a letter, it is left unchanged.

Decrypt Function: The decrypt function shifts the text back by the negative of the shift amount, effectively reversing the encryption.

Input Text: A text box where you can enter the plain text to encrypt or the cipher text to decrypt.
Shift Entry: An entry field where you specify the shift amount.
Encrypt Button: Encrypts the text in the input text box and displays the result in the output text box.
Decrypt Button: Decrypts the text in the input text box and displays the result in the output text box.
Output Text: A text box where the result (encrypted or decrypted text) is displayed.
Running the Code:
Copy the code into a Python file (e.g., caesar_cipher_gui.py).
Run the file using Python: python caesar_cipher_gui.py.
A window will open where you can enter text, specify a shift value, and click buttons to encrypt or decrypt the text.
This GUI provides a simple way to interact with the Caesar Cipher algorithm.

**Deffie -Hellman**
*Overview*
The Diffie-Hellman algorithm is being used to establish a shared secret that can be used for secret communications while exchanging data over a public network using the elliptic curve to generate points and get the secret key using the parameters.  

For the sake of simplicity and practical implementation of the algorithm, we will consider only 4 variables, one prime P and G (a primitive root of P) and two private values a and b.
P and G are both publicly available numbers. Users (say Alice and Bob) pick private values a and b and they generate a key and exchange it publicly. The opposite person receives the key and that generates a secret key, after which they have the same secret key to encrypt.
GUI Components:

## Features

- Encrypt and decrypt messages using the Caesar Cipher.
- Adjustable shift value for encryption and decryption.
- Simple and intuitive GUI.

further imporovements can be made ~
