import unittest
from my_awesome_lib.text_processing import reverse_text, count_words

class TestTextProcessing(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")

    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)

if __name__ == "__main__":
    unittest.main()
