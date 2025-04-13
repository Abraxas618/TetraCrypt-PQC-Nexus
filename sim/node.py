# sim/node.py

import hashlib
import random
import numpy as np
from config import HASH_FUNCTION

class Node:
    def __init__(self, id):
        self.id = id
        self.seed = random.getrandbits(256).to_bytes(32, 'big')
        self.biohash = self.generate_biohash()
        self.state = self.recursive_tesseract_hash(self.biohash)
        self.trust_vector = np.zeros(100)

    def generate_biohash(self):
        # Simulated biometric + UTC hash
        return hashlib.shake_256(self.seed).digest(32)

    def recursive_tesseract_hash(self, data):
        r = data
        for _ in range(4):  # 4D tesseract recursion
            r = hashlib.shake_256(r).digest(32)
        return r

    def vote_trust(self, peer_state):
        # Compare RTH state similarity (simulated cosine similarity)
        return np.dot(np.frombuffer(self.state, dtype=np.uint8),
                      np.frombuffer(peer_state, dtype=np.uint8)) / 8192
