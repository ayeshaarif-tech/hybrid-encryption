from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from binascii import hexlify

def xor_encrypt(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def encrypt_data(plaintext, key=None):
    if key is None:
        key = get_random_bytes(32)
    elif isinstance(key, str):
        key = key.encode('utf-8').ljust(32, b'\0')[:32]

    byte_data = plaintext.encode('utf-8') if isinstance(plaintext, str) else plaintext
    xor_ciphertext = xor_encrypt(byte_data, key)

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(xor_ciphertext)

    return {
        "nonce": hexlify(cipher.nonce).decode('utf-8'),
        "tag": hexlify(tag).decode('utf-8'),
        "ciphertext": hexlify(ciphertext).decode('utf-8'),
        "key": hexlify(key).decode('utf-8')
    }
