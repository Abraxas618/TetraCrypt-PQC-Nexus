# sim/simulate_quantum_attack.py

import hashlib, random
from config import Q_ATTACK_DEPTH

target = hashlib.shake_256(b"secret").digest(16)
attempts = 0
found = False

for _ in range(Q_ATTACK_DEPTH):
    guess = random.getrandbits(128).to_bytes(16, 'big')
    h = hashlib.shake_256(guess).digest(16)
    attempts += 1
    if h == target:
        found = True
        print(f"🔓 Hash collision after {attempts} attempts!")
        break

if not found:
    print(f"✅ SHAKE256 survived {Q_ATTACK_DEPTH} quantum attempts.")
