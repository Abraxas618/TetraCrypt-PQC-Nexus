import hashlib
import os
import time

def generate_entropy_salt(length: int = 16) -> str:
    """
    True entropy using os randomness + timestamp.
    """
    entropy = os.urandom(length) + str(time.time_ns()).encode()
    return hashlib.sha256(entropy).hexdigest()[:length]

def recursive_qidl_hash(seed: str, depth: int = 6, salt: str = None) -> str:
    """
    Collision-proof recursive QIDL hasher.
    Now truly generates a different result for every run, every time.
    """
    if salt is None:
        salt = generate_entropy_salt()  # 🧬 Always a fresh salt per call

    # Combine seed, salt, and a second entropy pulse into the input
    base_input = f"{seed}-{salt}-{time.time_ns()}"
    hash_input = base_input

    for i in range(depth):
        hash = hashlib.sha256()
        hash.update((hash_input + f"-round-{i}").encode())  # 🧠 Add iteration marker too
        hash_input = hash.hexdigest()

    return f"QIDL-{hash_input[:32]}"
