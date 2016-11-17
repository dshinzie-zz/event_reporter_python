# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import csv_manager as cm
import os.path

class CSVManagerTest(unittest.TestCase):

    def test_manager_intializes_with_empty_array(self):
        csv = cm.CSVManager()

        self.assertEqual(type(csv.data), list)

    def test_manager_loads_into_array(self):
        csv = cm.CSVManager()
        csv.load_file('./event_attendees.csv')

        self.assertTrue(csv.data)

    def test_manager_loads_all_data(self):
        csv = cm.CSVManager()
        csv.load_file('./event_attendees.csv')

        self.assertEqual(len(csv.data), 5175)

    def test_manager_saves_file(self):
        csv = cm.CSVManager()
        new_filename = './event_attendees_save.csv'
        csv.load_file('./event_attendees.csv')
        csv.save_file(new_filename, csv.data)

        assert os.path.exists(new_filename)
        
if __name__ == '__main__':
    unittest.main()
