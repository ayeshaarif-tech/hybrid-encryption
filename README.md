# Hybrid Encryption Service 

A dual-layer encryption module developed for secure data transmission between IoT devices (e.g., Raspberry Pi) and backend services. This repository implements a "Hybrid" approach by combining standard **AES-256 (EAX Mode)** with a custom **XOR bit-manipulation layer** for enhanced data security.

---

##  Features
* **Two-Layer Security:** Combines cryptographic standards with a custom logic layer to prevent simple pattern analysis.
* **Authenticated Encryption:** Uses AES-EAX mode to ensure both **confidentiality** and **integrity** (via MAC tags).
* **Hex-Encoded Payload:** Outputs data in a web-friendly hex format, ideal for JSON APIs and MQTT protocols used in IoT.
* **Simplified Integration:** Modularized structure for easy import into other Python projects.

##  Architecture
The system follows a specific sequence to ensure maximum entropy:

1.  **Encryption:** `Plaintext` → `XOR Cipher` → `AES-EAX` → `Hex Output`
2.  **Decryption:** `Hex Input` → `AES-EAX Verify` → `XOR Decipher` → `Plaintext`

##  Steps

### Prerequisites
* Python 3.x
* `pycryptodome` library

Install the required library using pip:

```bash
pip install pycryptodome
```

### Installation & Folder Structure
hybrid-encryption/
├── README.md
└── services/
    ├── __init__.py
    ├── encryption.py
    └── decryption.py
    
### Usage Example
1. Encrypting Data (Sender Side / IoT Device):

```bash
from Pythonservices.encryption import encrypt_data
# The data to secure
data = "Sensitive Smart City Sensor Data"
# Returns a dictionary with nonce, tag, ciphertext, and key
payload = encrypt_data(data)
print("Encrypted Payload:", payload)
```

2. Decrypting Data (Receiver Side / Backend):
```bash
from services.decryption import decrypt_data
# Pass the payload dictionary received from the sender
decrypted_text = decrypt_data(payload)
print(f"Decoded Result: {decrypted_text}")
```

##  Security Implementation Details
XOR Layer: Acts as a primary obfuscation step using the same key as the AES cipher.

AES-EAX: Provides high-security authenticated encryption, protecting against bit-flipping attacks and ensuring the data has not been tampered with during transit.

##  License
This module was designed as part of a Final Year Project (FYP) focused on Private Blockchain and Secure Data Storage.
Developed for Smart City Security Research.
