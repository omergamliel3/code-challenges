import unittest
from solutions.convert_list_item import convert_list_item


class TestConvertListItem(unittest.TestCase):

    # ---------- VALID CASES ----------

    def test_valid_simple(self):
        self.assertEqual(convert_list_item("1. Item"), "<li>Item</li>")

    def test_valid_with_leading_spaces(self):
        self.assertEqual(convert_list_item(
            "   2. Something"), "<li>Something</li>")

    def test_valid_multi_digit_number(self):
        self.assertEqual(convert_list_item("10. Ten"), "<li>Ten</li>")

    def test_valid_multiple_spaces_after_period(self):
        self.assertEqual(convert_list_item(
            "3.    Many spaces"), "<li>Many spaces</li>")

    def test_valid_inner_spaces(self):
        self.assertEqual(convert_list_item(
            "4.   Hello   World"), "<li>Hello   World</li>")

    # ---------- INVALID: TYPE CHECK ----------

    def test_invalid_non_string_int(self):
        self.assertEqual(convert_list_item(123), "Invalid format")

    def test_invalid_non_string_none(self):
        self.assertEqual(convert_list_item(None), "Invalid format")

    def test_invalid_non_string_list(self):
        self.assertEqual(convert_list_item(["1. item"]), "Invalid format")

    # ---------- INVALID: MISSING PERIOD ----------

    def test_invalid_no_period(self):
        self.assertEqual(convert_list_item("1 Item"), "Invalid format")

    def test_invalid_period_not_after_number(self):
        self.assertEqual(convert_list_item("1 ) wrong"), "Invalid format")

    # ---------- INVALID: NUMBER PART ----------

    def test_invalid_number_not_digit(self):
        self.assertEqual(convert_list_item("x. Item"), "Invalid format")

    def test_invalid_zero_not_allowed(self):
        self.assertEqual(convert_list_item("0. Zero"), "Invalid format")

    def test_invalid_negative_number(self):
        self.assertEqual(convert_list_item("-1. Nope"), "Invalid format")

    def test_invalid_empty_number_before_period(self):
        self.assertEqual(convert_list_item(
            ". Missing number"), "Invalid format")

    # ---------- INVALID: TEXT PART ----------

    def test_invalid_no_space_after_period(self):
        self.assertEqual(convert_list_item("1.Item"), "Invalid format")

    def test_invalid_only_spaces_after_period(self):
        self.assertEqual(convert_list_item("1.     "), "Invalid format")

    def test_invalid_empty_after_strip(self):
        self.assertEqual(convert_list_item("1.    "), "Invalid format")

    def test_invalid_text_missing(self):
        self.assertEqual(convert_list_item("2."), "Invalid format")

    def test_invalid_text_none_after_period(self):
        self.assertEqual(convert_list_item("5."), "Invalid format")

    # ---------- INVALID: WEIRD FORMATTING ----------

    def test_invalid_extra_periods(self):
        self.assertEqual(convert_list_item("1.2. weird"), "Invalid format")

    def test_invalid_period_without_number(self):
        self.assertEqual(convert_list_item("    . No"), "Invalid format")

    def test_invalid_mixed_chars_in_number(self):
        self.assertEqual(convert_list_item("1a. Nope"), "Invalid format")

    def test_invalid_trailing_period_no_text(self):
        self.assertEqual(convert_list_item("7. "), "Invalid format")


if __name__ == "__main__":
    unittest.main()
