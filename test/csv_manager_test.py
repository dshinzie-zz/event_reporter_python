# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import csv_manager as cm

class CSVManagerTest(unittest.TestCase):

    def test_manager_intializes_with_empty_array(self):
        csv = cm.CSVManager()

        self.assertEqual(type(csv.data), list)

    def test_manager_loads_into_array(self):
        csv = cm.CSVManager()
        csv.load_file('./event_attendees.csv')

        # self.assertEqual(csv.data, list)
        assert csv.data is not None


if __name__ == '__main__':
    unittest.main()
