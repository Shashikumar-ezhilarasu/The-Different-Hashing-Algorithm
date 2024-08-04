**Caesar Cipher Java Project**
*Overview*
The Caesar Cipher Java Project is a simple implementation of the classic Caesar Cipher encryption algorithm. This program allows users to encrypt and decrypt messages by shifting the letters of the alphabet by a specified number of positions. The project is written in Java and is intended to provide a basic understanding of how substitution ciphers work.

Features
Encryption: Encrypts plaintext by shifting each letter by a specified number of positions.
Decryption: Decrypts ciphertext by reversing the shift applied during encryption.
User Input: Allows users to specify the shift value and input the text via the console.
Preservation of Non-Letters: Non-letter characters (e.g., numbers, punctuation) remain unchanged.
Getting Started
Prerequisites
Java Development Kit (JDK): Make sure you have JDK installed on your system. You can download it from the Oracle website or use OpenJDK.
Visual Studio Code: You can download it from the Visual Studio Code website.
Java Extensions for VSCode: Install the Java Extension Pack from the VSCode Extensions Marketplace.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/CaesarCipherProject.git
cd CaesarCipherProject
Open in VSCode:

Launch Visual Studio Code.
Open the cloned repository folder.
Build the Project:

Open the terminal in VSCode.
Navigate to the project directory and compile the Java files:
bash
Copy code
javac -d bin src/com/cipher/*.java
Run the Application:

Use the terminal or the VSCode run configuration to execute the program:
bash
Copy code
java -cp bin com.cipher.CaesarCipherApp
Usage
Run the Application:

Open a terminal and navigate to the project directory.
Execute the main class:
bash
Copy code
java -cp bin com.cipher.CaesarCipherApp
Enter the Shift Value:

Provide an integer value for the shift. This determines how many positions each letter will be moved in the alphabet.
Input the Plaintext:

Type the text you want to encrypt. The program will output the encrypted message.
View Encrypted and Decrypted Text:

The application will display the encrypted text and then decrypt it back to the original plaintext.
Example
yaml
Copy code
Enter the shift value: 3
Enter the plaintext: HELLO WORLD
Encrypted text: KHOOR ZRUOG
Decrypted text: HELLO WORLD
Project Structure
plaintext
Copy code
CaesarCipherProject/
│
├── src/
│   └── com/
│       └── cipher/
│           ├── CaesarCipher.java
│           └── CaesarCipherApp.java
│
├── bin/  (compiled Java classes)
│
└── .vscode/
    └── launch.json  (VSCode configuration for running the project)
Code Explanation
CaesarCipher.java
Constructor: Initializes the cipher with a specified shift value.
encrypt(String plaintext): Encrypts the plaintext by shifting each letter.
decrypt(String ciphertext): Decrypts the ciphertext by reversing the shift.
CaesarCipherApp.java
Main Method: Handles user input for shift value and plaintext, then displays the encrypted and decrypted text.
Customization
Shift Value: You can modify the shift value directly in the code or allow the user to input it via the console.
Character Handling: Extend the algorithm to handle special characters, numbers, or ignore certain characters as needed.
