import string

plain = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    result = ""
    for char in text.upper():
        if char in plain:
            index = plain.index(char)
            result += key[index]
        else:
            result += char
    return result

def decrypt(text):
    result = ""
    for char in text.upper():
        if char in key:
            index = key.index(char)
            result += plain[index]
        else:
            result += char
    return result

text = input("Enter plaintext: ")

cipher = encrypt(text)
print("Encrypted:", cipher)

print("Decrypted:", decrypt(cipher))
