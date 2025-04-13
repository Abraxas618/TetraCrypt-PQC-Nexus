import unittest
from src.qidl_encrypt import QIDLEncoder
from src.tke import TetrahedralKeyExchange

class TestQIDLEncoder(unittest.TestCase):
    def setUp(self):
        self.qidl = QIDLEncoder()
        self.tke = TetrahedralKeyExchange()
        self.private_key, self.public_key = self.tke.generate_keypair()

    def test_encrypt_decrypt(self):
        message = "Hello, Quantum Swarm!"
        ciphertext, shared_secret = self.qidl.encrypt(self.public_key, message)
        decrypted = self.qidl.decrypt(self.private_key, ciphertext, shared_secret)
        self.assertEqual(decrypted, message)

if __name__ == '__main__':
    unittest.main()
