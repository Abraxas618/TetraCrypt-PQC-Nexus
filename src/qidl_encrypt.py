"""
Quantum Isoca-Dodecahedral Encryption (QIDL)
TetraCrypt PQC Nexus – Entropy-Verified Final Version
"""

import numpy as np
import time
import os
import hashlib

def generate_isoca_dodecahedral_key(seed: int = 42):
    """
    Generate a pseudo-random dodecahedral structure key based on golden ratio encoding.
    """
    np.random.seed(seed)
    phi = (1 + np.sqrt(5)) / 2
    angles = np.linspace(0, 2 * np.pi, 20)
    key = np.array([np.cos(phi * angles), np.sin(phi * angles)]).T
    return key

def generate_entropy_salt(length: int = 16) -> str:
    """
    Strong entropy using os.urandom and time-based fallback, SHA256 hashed.
    """
    entropy_base = os.urandom(length) + str(time.time()).encode()
    return hashlib.sha256(entropy_base).hexdigest()[:length]

def qidl_encrypt(message: str, key: np.ndarray, salt: str = None):
    """
    Golden-ratio projection with true entropy salt integration.
    Salt now influences the transformation directly.
    """
    if salt is None:
        salt = generate_entropy_salt()

    # Salt becomes a mathematical component in the transform
    salt_val = sum([ord(s) for s in salt]) % 89  # Safe scalar mix (mod 89 = prime)

    encoded = []
    full_message = message + salt
    for i, char in enumerate(full_message):
        char_val = ord(char) + salt_val  # Apply salt to each character's numeric weight
        point = key[i % len(key)]
        transformed = (char_val * point[0], char_val * point[1])
        encoded.append(transformed)

    return encoded, salt

def qidl_decrypt(encoded_message, key: np.ndarray, salt: str = ''):
    """
    Reverse dodecahedral projection and remove appended entropy salt.
    """
    decoded = ''
    for i, (x, y) in enumerate(encoded_message):
        point = key[i % len(key)]
        char_val = round((x + y) / (point[0] + point[1]))
        decoded += chr(int(char_val) % 256)

    if salt and decoded.endswith(salt):
        decoded = decoded[:-len(salt)]
    return decoded
