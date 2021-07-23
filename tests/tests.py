import unittest
import os
import warnings
from passwd_encrypt.passwd_encrypt import pw_create_rsa_key,\
    pw_encrypt_msg, pw_decrypt_msg


class Test(unittest.TestCase):

    # ============================================================
    def test_create_keys(self):

        lremove = ["mykey_test01.pem", "mykey_test01.pem.pub", "mykey_test02.pem", "mykey_test02.pem.pub" ]
        try:
            for item in lremove:
                os.remove(item)
        except FileNotFoundError:
            pass

        pw_create_rsa_key("mykey_test01")
        pw_create_rsa_key("mykey_test02", bits=2048)

    # ============================================================
    def test_encrypt_decrypt_to_file_key4096(self):

        msg = "PULP FICTION"
        public_key = "mykey_test01.pem.pub"
        private_key = "mykey_test01.pem"
        pw_encrypt_msg(public_key, msg)

        msg_decrypt = pw_decrypt_msg(private_key, "passwd_encrypted.bin")
        msg_decrypt = msg_decrypt.decode()

        self.assertEqual(msg, msg_decrypt)
        print("Message decrypted correctly")
        print("\tOriginal message: {}".format(msg))
        print("\tDecypher message: {}".format(msg_decrypt))

    # ============================================================
    def test_encrypt_decrypt_to_file_key2098(self):

        msg = "RESERVOIR DOGS"
        public_key = "mykey_test02.pem.pub"
        private_key = "mykey_test02.pem"
        pw_encrypt_msg(public_key, msg)

        msg_decrypt = pw_decrypt_msg(private_key, "passwd_encrypted.bin")
        msg_decrypt = msg_decrypt.decode()

        self.assertEqual(msg, msg_decrypt)
        print("Message decrypted correctly")
        print("\tOriginal message: {}".format(msg))
        print("\tDecypher message: {}".format(msg_decrypt))

    # ============================================================
    def test_encrypt_decrypt_to_string_key4096(self):

        msg = "KILL BILL Vol.1"
        public_key = "mykey_test01.pem.pub"
        private_key = "mykey_test01.pem"
        enc_data = pw_encrypt_msg(public_key, msg)

        msg_decrypt = pw_decrypt_msg(private_key, enc_data)
        msg_decrypt = msg_decrypt.decode()

        self.assertEqual(msg, msg_decrypt)
        print("Message decrypted correctly")
        print("\tOriginal message: {}".format(msg))
        print("\tDecypher message: {}".format(msg_decrypt))

    # ============================================================
    def test_using_incorrect_keys(self):

        warnings.filterwarnings("ignore", message="Enable tracemalloc to get the object allocation traceback")

        msg = "KILL BILL Vol.2"
        public_key = "mykey_test02.pem.pub"
        private_key = "mykey_test01.pem"
        pw_encrypt_msg(public_key, msg)

        self.assertRaises(ValueError, pw_decrypt_msg, private_key, "passwd_encrypted.bin")

    # ##################################################################################################################
    @classmethod
    def tearDownClass(cls):
        lremove = ["mykey_test01.pem", "mykey_test01.pem.pub", "mykey_test02.pem", "mykey_test02.pem.pub" ]
        try:
            for item in lremove:
                os.remove(item)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
