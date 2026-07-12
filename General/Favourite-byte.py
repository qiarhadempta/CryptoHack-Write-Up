ciphertext_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

ciphertext = bytes.fromhex(ciphertext_hex)

key = ciphertext[0] ^ ord('c')

print(f"[+] secret key found: {key}")

flag_bytes = bytearray()
for byte in ciphertext:
    flag_bytes.append(byte ^ key)

flag = flag_bytes.decode()
print(f"[+] Flag: {flag}")