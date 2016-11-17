# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import cleaner

class CleanerTest(unittest.TestCase):

    def test_cleaner_downcases_all_letters(self):
        self.assertEqual("test", cleaner.clean_case("TEST"))
        self.assertEqual("onetwothree", cleaner.clean_case("OneTwoThree"))
        self.assertEqual("unittest", cleaner.clean_case("Unittest"))

    def test_cleaner_pads_zip_codes_to_five_digits(self):
        self.assertEqual("00924", cleaner.clean_zipcode("924"))
        self.assertEqual("77004", cleaner.clean_zipcode("77004"))
        self.assertEqual("00001", cleaner.clean_zipcode("1"))

    def test_cleaner_zip_defaults_to_00000_if_nil_or_empty(self):
        self.assertEqual("00000", cleaner.clean_zipcode(None))
        self.assertEqual("00000", cleaner.clean_zipcode(""))

    def test_cleaner_reformats_numbers_with_no_spaces_no_characaters(self):
        self.assertEqual("615-438-5000", cleaner.clean_phone("6154385000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("3609046000"))

    def test_cleaner_reformats_numbers_with_special_characters(self):
        self.assertEqual("360-904-6000", cleaner.clean_phone("360-904-6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360) 904 6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360)-904 6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360) 904-6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360)-9046000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360)904-6000"))

        self.assertEqual("360-904-6000", cleaner.clean_phone("360.904.6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360).904 6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360) 904.6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360).9046000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360)904.6000"))

        self.assertEqual("360-904-6000", cleaner.clean_phone("360-904.6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("360.904-6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360).904-6000"))
        self.assertEqual("360-904-6000", cleaner.clean_phone("(360)-904.6000"))

    def test_cleaner_excludes_first_optional_1(self):
        self.assertEqual("508-237-5000", cleaner.clean_phone("1-508-237-5000"))
        self.assertEqual("857-498-1000", cleaner.clean_phone("1(857)498-1000"))
        self.assertEqual("614-236-7000", cleaner.clean_phone("1-(614) 236-7000"))
        self.assertEqual("111-111-1000", cleaner.clean_phone("111-111-1000"))

    def test_cleaner_returns_message_for_empty_or_nil_numbers(self):
        expected = "000-000-0000"
        self.assertEqual(expected, cleaner.clean_phone(""))
        self.assertEqual(expected, cleaner.clean_phone("0"))
        self.assertEqual(expected, cleaner.clean_phone(None))

    def test_cleaner_returns_message_for_numbers_containing_letters(self):
        expected = "000-000-0000"
        self.assertEqual(expected, cleaner.clean_phone("n000"))
        self.assertEqual(expected, cleaner.clean_phone("xxxx000"))
        self.assertEqual(expected, cleaner.clean_phone("ajgabrie@unca.000"))
        self.assertEqual(expected, cleaner.clean_phone("9.82E+00"))

    def test_cleaner_returns_message_for_number_less_than_10_digits(self):
        expected = "000-000-0000"
        self.assertEqual(expected, cleaner.clean_phone("999 23 9343"))
        self.assertEqual(expected, cleaner.clean_phone("324 300 333"))
        self.assertEqual(expected, cleaner.clean_phone("114 454 121"))
        self.assertEqual("993-343-1234", cleaner.clean_phone("993 343 1234"))
        

if __name__ == '__main__':
    unittest.main()
