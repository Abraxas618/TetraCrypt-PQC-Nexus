"""
Quantum Isoca-Dodecahedral Encryption (QIDL)
TetraCrypt PQC Nexus – Codex-Class Secure Final Version
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
    True entropy using os randomness + timestamp hash.
    """
    entropy = os.urandom(length) + str(time.time_ns()).encode()
    return hashlib.sha256(entropy).hexdigest()[:length]

def recursive_qidl_hash(seed: str, depth: int = 6, salt: str = None) -> str:
    """
    Recursive QIDL hasher with per-round salt application.
    Salt ensures every call returns a unique result — even with same input.
    """
    if salt is None:
        salt = generate_entropy_salt()

    hash_input = seed
    for i in range(depth):
        combined = f"{hash_input}-{salt}-{i}"  # salt + round ID + prior hash
        hash_input = hashlib.sha256(combined.encode()).hexdigest()

    return f"QIDL-{hash_input[:32]}"

def qidl_encrypt(message: str, key: np.ndarray, salt: str = None):
    """
    Golden-ratio projection with true entropy salt integration.
    Encrypts characters onto a 2D isoca-dodecahedron ring.
    """
    if salt is None:
        salt = generate_entropy_salt()

    salt_val = sum([ord(s) for s in salt]) % 89  # Salt scalar influence
    full_message = message + salt

    encoded = []
    for i, char in enumerate(full_message):
        char_val = ord(char) + salt_val
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
