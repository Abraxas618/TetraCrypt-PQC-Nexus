from pathlib import Path

# Path to the patched run_all.py
patched_run_all = Path("/mnt/data/run_all_patched.py")

patched_code = '''\
"""
Run All TetraCrypt Modules: Demonstration CLI
Author: Michael Tass MacDonald
Version: v0.1.0
"""

import os
import sys

# Ensure src/ is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# --- External Simulations ---
def run_external_simulations():
    print("🚀 Running Quantum + Swarm Simulations")
    sim_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "sim"))
    os.system(f"python3 {os.path.join(sim_dir, 'simulate_quantum_attack.py')}")
    os.system(f"python3 {os.path.join(sim_dir, 'simulate_swarm.py')}")

# --- Internal Core Demos ---
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

patched_run_all.write_text(patched_code)
patched_run_all
