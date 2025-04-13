from pathlib import Path

# Define the file path and content for test_tke.py
test_tke_path = Path("tests/test_tke.py")
test_tke_content = '''
import unittest
from src.tke import generate_tetrahedral_keypair, derive_shared_key

class TestTetrahedralKeyExchange(unittest.TestCase):
    def test_keypair_generation(self):
        pub, priv = generate_tetrahedral_keypair()
        self.assertEqual(len(pub), 4)
        self.assertEqual(len(priv), 4)
    
    def test_shared_key(self):
        pubA, privA = generate_tetrahedral_keypair()
        pubB, privB = generate_tetrahedral_keypair()
        shared1 = derive_shared_key(privA, pubB)
        shared2 = derive_shared_key(privB, pubA)
        self.assertEqual(shared1, shared2)

if __name__ == '__main__':
    unittest.main()
'''

# Create the directory and write the file
test_tke_path.parent.mkdir(parents=True, exist_ok=True)
test_tke_path.write_text(test_tke_content)

test_tke_path.name
