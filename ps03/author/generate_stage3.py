KEY = "SHADOW"

PLAINTEXT = """ATTACKER NOTE: ACCESS THE FILE SHARE AT fileserver01:/srv/shadow/evidence.dd. FLAG: SHADOW{weak_ciphers_leave_traces}"""


def vigenere_encrypt(text, key):
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():

            shift = ord(key[key_index % len(key)].upper()) - ord('A')

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encrypted_char = chr(
                (ord(char) - base + shift) % 26 + base
            )

            result.append(encrypted_char)

            key_index += 1

        else:
            result.append(char)

    return ''.join(result)


ciphertext = vigenere_encrypt(PLAINTEXT, KEY)

with open("public/ciphertext.txt", "w") as file:
    file.write(ciphertext + "\n")

print("Stage 3 ciphertext generated.")
print(ciphertext)
