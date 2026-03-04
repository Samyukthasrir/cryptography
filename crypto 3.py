import string

def generate_matrix(key):
    key = key.upper().replace("J","I")
    matrix = []
    used = set()

    for c in key + string.ascii_uppercase:
        if c not in used and c != 'J':
            used.add(c)
            matrix.append(c)

    return [matrix[i:i+5] for i in range(0,25,5)]

def find(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i,j

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = text.upper().replace("J","I").replace(" ","")

    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = 'X'
        if i+1 < len(text):
            b = text[i+1]
        if a == b:
            pairs.append((a,'X'))
            i += 1
        else:
            pairs.append((a,b))
            i += 2

    cipher = ""

    for a,b in pairs:
        r1,c1 = find(matrix,a)
        r2,c2 = find(matrix,b)

        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5]
            cipher += matrix[r2][(c2+1)%5]

        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1]
            cipher += matrix[(r2+1)%5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

key = input("Enter key: ")
text = input("Enter plaintext: ")

print("Encrypted:", playfair_encrypt(text,key))
