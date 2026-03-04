def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 + k) % 26
            result += chr(shift + 65)
        else:
            result += char
    return result

def caesar_decrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 - k) % 26
            result += chr(shift + 65)
        else:
            result += char
    return result

text = input("Enter text: ")
k = int(input("Enter shift value: "))

cipher = caesar_encrypt(text, k)
print("Encrypted:", cipher)

print("Decrypted:", caesar_decrypt(cipher, k))
