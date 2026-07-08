key1_hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2_xor_key1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2_xor_key3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
encrypted_flag = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

k1 = int(key1_hex, 16)
k2_k1 = int(key2_xor_key1, 16)
k2_k3 = int(key2_xor_key3, 16)
enc_flag = int(encrypted_flag, 16)

k2 = k2_k1 ^ k1       
k3 = k2_k3 ^ k2       

flag_int = enc_flag ^ k1 ^ k2 ^ k3

flag_hex = hex(flag_int)[2:]
flag = bytes.fromhex(flag_hex).decode()

print(flag)