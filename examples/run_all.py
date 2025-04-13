from pathlib import Path

# Create the script for examples/run_all.py
examples_dir = Path("/mnt/data/TetraCrypt_PQC_Structure/examples")
examples_dir.mkdir(parents=True, exist_ok=True)

run_all_script = examples_dir / "run_all.py"
run_all_script.write_text('''\
"""
Run All TetraCrypt Modules: Demonstration CLI
Author: Michael Tass MacDonald
"""

from src.tke import TetrahedralKeyExchange
from src.qidl_encrypt import QIDLEncoder
from src.rth import RecursiveTesseractHash
from src.hbb_blockchain import HypercubeBlockchain

# --- Initialize modules ---
tke = TetrahedralKeyExchange()
qidl = QIDLEncoder()
rth = RecursiveTesseractHash()
hbb = HypercubeBlockchain()

# --- Tetrahedral Key Exchange Demo ---
private_key, public_key = tke.generate_keypair()
print("TKE Public Key:", public_key)

# --- QIDL Encryption Demo ---
message = "Hello, Hyperdimensional World!"
ciphertext, shared_secret = qidl.encrypt(public_key, message)
print("QIDL Encrypted:", ciphertext)

decrypted = qidl.decrypt(private_key, ciphertext, shared_secret)
print("QIDL Decrypted:", decrypted)

# --- Recursive Tesseract Hashing Demo ---
bio_sample = b"EEG_SAMPLE|DNA_SAMPLE"
hashed = rth.hash(bio_sample)
print("RTH Hash:", hashed)

# --- Hypercube Blockchain Demo ---
hbb.add_block({"payload": hashed})
print("HBB Chain Length:", len(hbb.chain))
''')

run_all_script
