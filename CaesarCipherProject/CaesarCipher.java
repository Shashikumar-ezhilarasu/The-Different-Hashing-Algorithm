package com.cipher;

public class CaesarCipher {
    private int shift;

    public CaesarCipher(int shift) {
        this.shift = shift;
    }

    public String encrypt(String plaintext) {
        StringBuilder ciphertext = new StringBuilder();
        for (char c : plaintext.toCharArray()) {
            if (Character.isLetter(c)) {
                char shiftedChar = (char) (c + shift);
                if ((Character.isLowerCase(c) && shiftedChar > 'z') ||
                    (Character.isUpperCase(c) && shiftedChar > 'Z')) {
                    shiftedChar -= 26;
                }
                ciphertext.append(shiftedChar);
            } else {
                ciphertext.append(c);
            }
        }
        return ciphertext.toString();
    }

    public String decrypt(String ciphertext) {
        StringBuilder plaintext = new StringBuilder();
        for (char c : ciphertext.toCharArray()) {
            if (Character.isLetter(c)) {
                char shiftedChar = (char) (c - shift);
                if ((Character.isLowerCase(c) && shiftedChar < 'a') ||
                    (Character.isUpperCase(c) && shiftedChar < 'A')) {
                    shiftedChar += 26;
                }
                plaintext.append(shiftedChar);
            } else {
                plaintext.append(c);
            }
        }
        return plaintext.toString();
    }
}
//modified spacing 