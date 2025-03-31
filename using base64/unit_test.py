import unittest
from ascii85 import encode_ascii85, decode_ascii85

class TestAscii85(unittest.TestCase):
    def test_encode_ascii85(self):
        self.assertEqual(encode_ascii85(b'test'), "BOu!r")
        self.assertEqual(encode_ascii85(b'hello world'), "87cURD]i,")
        self.assertEqual(encode_ascii85(b''), "")
    
    def test_decode_ascii85(self):
        self.assertEqual(decode_ascii85("BOu!r"), b'test')
        self.assertEqual(decode_ascii85("87cURD]i,"), b'hello world')
        self.assertEqual(decode_ascii85(""), b'')
    
    def test_decode_invalid(self):
        with self.assertRaises(ValueError):
            decode_ascii85("!!")
        with self.assertRaises(ValueError):
            decode_ascii85("z!")

if __name__ == '__main__':
    unittest.main()
