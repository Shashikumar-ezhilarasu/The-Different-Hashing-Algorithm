package com.cipher;

import java.util.Scanner;

public class CaesarCipherApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the shift value: ");
        int shift = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        CaesarCipher cipher = new CaesarCipher(shift);

        System.out.print("Enter the plaintext: ");
        String plaintext = scanner.nextLine();

        String encryptedText = cipher.encrypt(plaintext);
        System.out.println("Encrypted text: " + encryptedText);

        String decryptedText = cipher.decrypt(encryptedText);
        System.out.println("Decrypted text: " + decryptedText);
    }
}
