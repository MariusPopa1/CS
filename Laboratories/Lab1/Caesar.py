def encrypt_decrypt(t, s):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_choice = (input("Would you like to use an encryption key? "))
    if key_choice == "yes":
        alphabet = alphabet_transform(alphabet)

    choice = int(input("Choose: \nEncrypt(1) \nDecrypt(2)? \n"))
    while choice != 1 and choice != 2:
        input("Invalid choice, choose 1 or 2\n")
    if choice == 1:
        for char in t.upper():
            result += alphabet[(alphabet.index(char)+s) % 26]
    else:
        for char in t.upper():
            result += alphabet[(alphabet.index(char)-s) % 26]
    return result


def alphabet_transform(alphabet):
    key = input("input key: ")
    while len(key) < 7:
        key = input("The length of the key must be 7 or more. Enter it again: ")
    key = key.upper()
    key1 = ""
    for char in key:
        if char not in key1:
            key1 += char

    for char in alphabet:
        if char not in key1:
            key1 += char
    print("The new alphabet is: ", key1)
    return key1


text = input("Input text: ")
saved_text = text

text = text.replace(' ', '')
while not text.isalpha():
    text = input("Enter only letters: ")

shift = int(input("Enter shift: "))

print(encrypt_decrypt(text, shift))
