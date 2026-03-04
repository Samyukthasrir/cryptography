def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 65
            value = (ord(char) - 65 + shift) % 26
            result += chr(value + 65)
            j += 1
        else:
            result += char

    return result

def decrypt(cipher, key):
    result = ""
    key = key.upper()
    j = 0

    for char in cipher:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 65
            value = (ord(char) - 65 - shift) % 26
            result += chr(value + 65)
            j += 1
        else:
            result += char

    return result

text = input("Enter plaintext: ")
key = input("Enter key: ")

cipher = encrypt(text,key)

print("Encrypted:",cipher)
print("Decrypted:",decrypt(cipher,key))
