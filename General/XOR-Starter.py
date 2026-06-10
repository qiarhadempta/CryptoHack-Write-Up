label = "label"
flag_content = "".join(chr(ord(char) ^ 13) for char in label)

print(f"crypto{{{flag_content}}}")