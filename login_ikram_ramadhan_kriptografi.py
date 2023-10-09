import random

def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ''
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            key_index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text

def login_system():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Enkripsi password dengan kata kunci "rahasia"
    key = "rahasia"
    encrypted_password = vigenere_encrypt(password, key)

    # Simpan username dan password yang telah dienkripsi dalam database
    database = {
        "user1": vigenere_encrypt("password1", key),
        "user2": vigenere_encrypt("password2", key),
    }

    if username in database and database[username] == encrypted_password:
        print("Login berhasil!")
    else:
        print("Login gagal. Coba lagi.")

if __name__ == "__main__":
    login_system()
