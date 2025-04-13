import unittest
from src.tke import TetrahedralKeyExchange

class TestTetrahedralKeyExchange(unittest.TestCase):
    def setUp(self):
        self.tke = TetrahedralKeyExchange()
        self.private_key, self.public_key = self.tke.generate_keypair()

    def test_keypair_generation(self):
        self.assertIsInstance(self.private_key, bytes)
        self.assertIsInstance(self.public_key, bytes)

    def test_key_exchange_simulation(self):
        shared_secret1 = self.tke.derive_shared_secret(self.private_key, self.public_key)
        shared_secret2 = self.tke.derive_shared_secret(self.private_key, self.public_key)
        self.assertEqual(shared_secret1, shared_secret2)

if __name__ == '__main__':
    unittest.main()
