from pathlib import Path

# Path to create the updated run_all.py script
run_all_script = Path("/mnt/data/run_all.py")

# Full script content with improvements
script_code = '''\
"""
Run All TetraCrypt Modules: Demonstration CLI
Author: Michael Tass MacDonald
Version: v0.1.0
"""

import os
import sys
from pathlib import Path

# Ensure 'src' directory is in the Python path for imports
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

def run_external_simulations():
    print("🚀 Running Quantum + Swarm Simulations")
    os.system("python3 sim/simulate_quantum_attack.py")
    os.system("python3 sim/simulate_swarm.py")

def run_internal_demos():
    try:
        from tke import TetrahedralKeyExchange
        from qidl_encrypt import QIDLEncoder
        from rth import RecursiveTesseractHash
        from hbb_blockchain import HypercubeBlockchain
    except ImportError as e:
        print(f"[!] Import failed: {e}")
        return

    print("\\n🧪 Running Core Module Demos")

    # --- Tetrahedral Key Exchange Demo ---
    tke = TetrahedralKeyExchange()
    private_key, public_key = tke.generate_keypair()
    print("TKE Public Key:", public_key)

    # --- QIDL Encryption Demo ---
    message = "Hello, Hyperdimensional World!"
    qidl = QIDLEncoder()
    ciphertext, shared_secret = qidl.encrypt(public_key, message)
    print("QIDL Encrypted:", ciphertext)

    decrypted = qidl.decrypt(private_key, ciphertext, shared_secret)
    print("QIDL Decrypted:", decrypted)

    # --- Recursive Tesseract Hashing Demo ---
    rth = RecursiveTesseractHash()
    bio_sample = b"EEG_SAMPLE|DNA_SAMPLE"
    hashed = rth.hash(bio_sample)
    print("RTH Hash:", hashed.hex())

    # --- Hypercube Blockchain Demo ---
    hbb = HypercubeBlockchain()
    hbb.add_block({"payload": hashed.hex()})
    print("HBB Chain Length:", len(hbb.chain))

if __name__ == "__main__":
    run_external_simulations()
    run_internal_demos()
'''

# Write the script to file
run_all_script.write_text(script_code)

# Return the path to confirm
run_all_script
