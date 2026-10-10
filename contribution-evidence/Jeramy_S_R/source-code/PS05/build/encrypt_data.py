KEY = b"NIGHTFALL"

with open("stolen_data.txt", "rb") as f:
    data = bytearray(f.read())

for i in range(len(data)):
    data[i] ^= KEY[i % len(KEY)]

with open("stolen_data.enc", "wb") as f:
    f.write(data)

print("Created stolen_data.enc")
