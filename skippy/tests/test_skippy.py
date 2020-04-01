#!/usr/bin/env python3

import random
import skippy
import sys
import unittest


class SkippyTest(unittest.TestCase):
    if sys.byteorder == "little":
        test_data = {42: 2444721374, 4711: 3970196332,
                     935425436: 42, 798322584: 4711}
    else:
        test_data = {42: 406043987, 4711: 4097152607,
                     935425436: 2123491105, 798322584: 2445249305}

    def test_too_short_keys_raise(self):
        with self.assertRaises(ValueError):
            skippy.Skippy(b"012345678")

    def test_long_keys_are_truncated(self):
        short_skippy = skippy.Skippy(b"0123456789")
        long_skippy = skippy.Skippy(b"0123456789abcdef")

        self.assertEqual(short_skippy.encrypt(42), long_skippy.encrypt(42))
        self.assertEqual(short_skippy.decrypt(42), long_skippy.decrypt(42))

    def test_encrypt_yields_same_result_as_skip32(self):
        uut = skippy.Skippy(b"s3cr3t k3y")
        for p, c in self.test_data.items():
            self.assertEqual(uut.encrypt(p), c)

    def test_decrypt_yields_same_result_as_skip32(self):
        uut = skippy.Skippy(b"s3cr3t k3y")

        for p, c in self.test_data.items():
            self.assertEqual(uut.decrypt(c), p)

    def test_encrypt_and_decrypt_are_symmetrical(self):
        key = "".join(random.choices(
            "0123456789abcdefghijklmnopqrstuvwxyz", k=10))
        uut = skippy.Skippy(bytes(key, "ascii"))
        for _ in range(1000):
            plain = random.getrandbits(32)
            cipher = uut.encrypt(plain)
            self.assertEqual(plain, uut.decrypt(
                cipher), f"Failed for key {key} and value {plain}!")


if __name__ == '__main__':
    unittest.main()
