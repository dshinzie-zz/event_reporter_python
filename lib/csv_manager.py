import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import attendee as a
import csv
from pdb import set_trace as bp

#csv_manager.py
class CSVManager:
    def __init__(self):
        self.data = []
        self.headers = [
            "last_Name",
            "first_Name",
            "Email_Address",
            "Zipcode",
            "City",
            "State",
            "Street",
            "HomePhone"
            ]

    def load_file(self, filename):
        self.data = []
        with open(filename, 'rb') as inputfile:
            reader = csv.DictReader(inputfile)
            for line in reader:
                self.data.append(a.Attendee(line))

        return self.data

    def save_file(self, filename, data):
        save_data = []
        with open(filename, 'wb') as outputfile:
            writer = csv.writer(outputfile)
            writer.writerow(self.headers)

            for row, header in zip(self.data, self.headers):
                lower_header = header.lower()
                save_data.append(getattr(row, lower_header))

            writer.writerow(save_data)
