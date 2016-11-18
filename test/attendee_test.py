from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import attendee as a

class AttendeeTest(unittest.TestCase):

    def setUp(self):
        self.data = {
            "RegDate": "1/1/1900",
            "first_Name": "FIRSTNAME",
            "last_Name": "LASTNAME",
            "Email_Address": "EMAIL@EMAIL",
            "HomePhone": "9999999999",
            "Street": "111 TEST ST",
            "City": "TEST CITY",
            "State": "TS",
            "Zipcode": "99999"
            }
    def test_attendee_holds_regdate(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.regdate, "1/1/1900")

    def test_attendee_holds_first_name(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.first_name, "firstname")

    def test_attendee_holds_last_name(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.last_name, "lastname")

    def test_attendee_holds_email_address(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.email_address, "email@email")

    def test_attendee_holds_homephone(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.homephone, "999-999-9999")

    def test_attendee_holds_street(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.street, "111 test st")

    def test_attendee_holds_city(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.city, "test city")

    def test_attendee_holds_state(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.state, "ts")

    def test_attendee_holds_zipcode(self):
        attendee = a.Attendee(self.data)
        self.assertEqual(attendee.zipcode, "99999")

if __name__ == '__main__':
    unittest.main()
