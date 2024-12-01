def create_playfair_matrix(key):

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZĂÂÎȘȚ"
    key = key.upper().replace('J', 'I')
    key = "".join(dict.fromkeys(key))
    matrix = [char for char in key if char in alphabet]

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i + 6] for i in range(0, 30, 6)]
    return playfair_matrix


def print_matrix(matrix):
    print("\nGenerated Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    print()


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None


def preprocess_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')

    text = "".join(char for char in text if char.isalpha())

    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result.append('X')
        i += 1

    if len(result) % 2 != 0:
        extra_char = input("Enter an extra character to complete the pair: ").upper()
        result.append(extra_char)
    return "".join(result)



def split_pairs(text):
    return [text[i:i + 2] for i in range(0, len(text), 2)]


def encrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_cipher(text, key, mode):
    matrix = create_playfair_matrix(key)
    print_matrix(matrix)
    preprocessed_text = preprocess_text(text)
    pairs = split_pairs(preprocessed_text)

    result = []
    for pair in pairs:
        if mode == 'encrypt':
            result.append(encrypt_pair(matrix, pair[0], pair[1]))
        elif mode == 'decrypt':
            result.append(decrypt_pair(matrix, pair[0], pair[1]))
    return "".join(result)



while True:
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        continue

    key = input("Enter the key (min 7 characters): ")
    key = "".join(char for char in key if char.isalpha()).upper().replace('J', 'I')
    if len(key) < 7:
        print("Key is too short. Please enter a key with at least 7 letters.")
        continue

    text = input("Enter the text: ")
    result = playfair_cipher(text, key, mode)
    print(f"Result: {result}")
    break


