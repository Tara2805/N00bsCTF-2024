# Vinegar
263

Can you decode this message? Note: Wrap the decrypted text in n00bz{}
Attachments

    enc.txt


# Walkthrough

research Vigenère cipher
use the following python script to decrypt

def vigenere_decrypt(ciphertext, key):
    # Prepare key and ciphertext
    key = key.lower()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    # Decrypting the message
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)  # 97 is the ASCII value of 'a'
        
    return plaintext

# Encrypted message and key
encrypted_message = 'nmivrxbiaatjvvbcjsf'
key = 'secretkey'

# Decrypt the message
decrypted_message = vigenere_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")

# Flag
vigenerecipherisfun