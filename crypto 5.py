def encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            p = ord(char) - 65
            c = (a * p + b) % 26
            result += chr(c + 65)
        else:
            result += char
    return result

text = input("Enter plaintext: ")
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

print("Encrypted:", encrypt(text,a,b))
