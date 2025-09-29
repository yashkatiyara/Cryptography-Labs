# Playfair Cipher Basic Implementation

def generate_matrix(key):
    key = "".join(sorted(set(key), key=lambda x: key.index(x))).upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is merged with I
    matrix = [c for c in key if c in alphabet]
    matrix += [c for c in alphabet if c not in matrix]
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j

def process_text(text):
    text = text.upper().replace("J", "I")
    processed = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = "X" if i+1==len(text) else text[i+1]
        if a == b:
            b = "X"
        processed += a + b
        i += 2
    return processed

def encrypt(text, matrix):
    text = process_text(text)
    cipher = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            cipher += matrix[row1][(col1+1)%5]
            cipher += matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher += matrix[(row1+1)%5][col1]
            cipher += matrix[(row2+1)%5][col2]
        else:
            cipher += matrix[row1][col2] + matrix[row2][col1]
    return cipher

# Example
key = "SECURITY"
matrix = generate_matrix(key)
text = "HELLO WORLD".replace(" ", "")
cipher = encrypt(text, matrix)
print("Encrypted:", cipher)
