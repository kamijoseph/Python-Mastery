
# Decoding a caesar cipher
def caesar_decipher(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

# Decrypt the ciphertext
ciphertext = "YMJ VZNY FSI VZNY NX BJFR UWTLWJQFYD."
print(caesar_decipher(ciphertext, 5))