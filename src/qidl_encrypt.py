from pathlib import Path

# Define the content for qidl_encrypt.py
qidl_encrypt_content = '''"""
Quantum Isoca-Dodecahedral Encryption (QIDL)
Part of the TetraCrypt PQC Nexus
"""

import numpy as np

def generate_isoca_dodecahedral_key(seed: int = 42):
    """
    Generate a pseudo-random dodecahedral structure key based on golden ratio encoding.
    """
    np.random.seed(seed)
    phi = (1 + np.sqrt(5)) / 2
    angles = np.linspace(0, 2 * np.pi, 20)
    key = np.array([np.cos(phi * angles), np.sin(phi * angles)]).T
    return key

def qidl_encrypt(message: str, key: np.ndarray):
    """
    Quantum layer simulation using rotational golden-ratio projection.
    Each character is transformed into a vector projection on a dodecahedron.
    """
    encoded = []
    for i, char in enumerate(message):
        char_val = ord(char)
        point = key[i % len(key)]
        transformed = (char_val * point[0], char_val * point[1])
        encoded.append(transformed)
    return encoded

def qidl_decrypt(encoded_message, key: np.ndarray):
    """
    Reverse the dodecahedral projection and extract characters.
    """
    decoded = ''
    for i, (x, y) in enumerate(encoded_message):
        point = key[i % len(key)]
        char_val = round((x + y) / (point[0] + point[1]))
        decoded += chr(int(char_val) % 256)
    return decoded
'''

# Create the file structure and write the content
src_path = Path("/mnt/data/src")
src_path.mkdir(parents=True, exist_ok=True)
qidl_path = src_path / "qidl_encrypt.py"
qidl_path.write_text(qidl_encrypt_content)

qidl_path.name
