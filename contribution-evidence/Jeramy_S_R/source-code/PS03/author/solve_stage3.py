KEY = "SHADOW"


def vigenere_decrypt(text, key):

    result = []
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)].upper()) - ord('A')

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            decrypted_char = chr(
                (ord(char) - base - shift) % 26 + base
            )

            result.append(decrypted_char)

            key_index += 1

        else:
            result.append(char)

    return ''.join(result)


with open("public/ciphertext.txt", "r") as file:
    ciphertext = file.read().strip()

plaintext = vigenere_decrypt(ciphertext, KEY)

print("\nRecovered message:\n")
print(plaintext)
