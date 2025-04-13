from pathlib import Path

# Define the content of the test_qidl_encrypt.py
test_qidl_encrypt_content = '''\
import unittest
import numpy as np
from src.qidl_encrypt import QIDL_Encryptor

class TestQIDLEncrypt(unittest.TestCase):
    def setUp(self):
        self.encryptor = QIDL_Encryptor(seed=123)
        self.message = "hypersecure"
        self.key = self.encryptor.generate_key()

    def test_key_shape(self):
        self.assertEqual(self.key.shape, (12, 20))

    def test_encryption_decryption(self):
        ciphertext = self.encryptor.encrypt(self.message, self.key)
        decrypted = self.encryptor.decrypt(ciphertext, self.key)
        self.assertEqual(decrypted, self.message)

    def test_entropy_variation(self):
        cipher1 = self.encryptor.encrypt(self.message, self.key)
        cipher2 = self.encryptor.encrypt(self.message, self.key)
        self.assertNotEqual(cipher1.tolist(), cipher2.tolist())

if __name__ == "__main__":
    unittest.main()
'''

# Write the file to the tests directory
tests_dir = Path("tests")
tests_dir.mkdir(parents=True, exist_ok=True)
(test_file := tests_dir / "test_qidl_encrypt.py").write_text(test_qidl_encrypt_content)

test_file

