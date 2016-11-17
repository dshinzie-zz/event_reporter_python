import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import attendee as a
import csv
from pdb import set_trace as bp

#csv_manager.py
class CSVManager:
    def __init__(self):
        self.data = []

    def load_file(self, filename):
        self.data = []
        with open(filename, 'rb') as inputfile:
            reader = csv.DictReader(inputfile)
            for line in reader:
                self.data.append(a.Attendee(line))
        return self.data
