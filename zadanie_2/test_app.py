import unittest
from app import is_valid_email, calculate_area, process_list, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        """Przygotowanie środowiska testowego."""
        self.valid_email = "test@example.com"
        self.invalid_email = "invalid-email"
        self.numbers = [5, 2, 8, 1, 3, 10]
        self.date = "25-03-2025"

    # Testy dla is_valid_email
    def test_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email(self.invalid_email))

    def test_email_without_domain(self):
        self.assertFalse(is_valid_email("test@com"))

    # Testy dla calculate_area
    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_area("circle", 3), 28.27431, places=5)

    def test_calculate_square_area(self):
        self.assertEqual(calculate_area("square", 4), 16)

    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_area("rectangle", 4, 5), 20)

    def test_calculate_area_invalid(self):
        with self.assertRaises(ValueError):
            calculate_area("triangle", 5, 10)

    # Testy dla process_list
    def test_sort_and_filter_even_numbers(self):
        self.assertEqual(process_list(self.numbers), [2, 8, 10])

    def test_sort_without_filter(self):
        self.assertEqual(process_list(self.numbers, filter_even=False), [1, 2, 3, 5, 8, 10])

    def test_process_empty_list(self):
        self.assertEqual(process_list([]), [])

    # Testy dla convert_date_format
    def test_valid_date_conversion(self):
        self.assertEqual(convert_date_format(self.date, "%d-%m-%Y", "%Y/%m/%d"), "2025/03/25")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date", "%d-%m-%Y", "%Y/%m/%d")

    def test_wrong_format(self):
        with self.assertRaises(ValueError):
            return convert_date_format(self.date, "%Y-%m-%d", "%d/%m/%Y")
            

    # Testy dla is_palindrome
    def test_palindrome_text(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_non_palindrome_text(self):
        self.assertFalse(is_palindrome("Python"))

    def test_palindrome_with_special_chars(self):
        self.assertTrue(is_palindrome("Kamil Ślimak"))

if __name__ == "__main__":
    unittest.main()



