KEY = b"NIGHTFALL"

with open("public/stolen_data.enc", "rb") as f:
    encrypted = f.read()

decrypted = bytearray()

for i, byte in enumerate(encrypted):
    decrypted.append(byte ^ KEY[i % len(KEY)])

with open("recovered/stolen_data.txt", "wb") as f:
    f.write(decrypted)

print(decrypted.decode("utf-8"))
