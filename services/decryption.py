from Crypto.Cipher import AES
from binascii import unhexlify

def xor_decrypt(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def decrypt_data(payload):
    try:
        nonce = unhexlify(payload['nonce'])
        tag = unhexlify(payload['tag'])
        ciphertext = unhexlify(payload['ciphertext'])
        key = unhexlify(payload['key'])

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        final_plaintext = xor_decrypt(decrypted, key)

        return final_plaintext.decode("utf-8")
    except Exception as e:
        return {"error": f"Decryption failed: {str(e)}"}
