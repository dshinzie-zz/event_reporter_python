import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import cleaner

class Attendee:
    def __init__(self, data):
        self.regdate = data["RegDate"]
        self.first_name = cleaner.clean_case(data["first_Name"])
        self.last_name = cleaner.clean_case(data["last_Name"])
        self.email_address = cleaner.clean_case(data["Email_Address"])
        self.homephone = cleaner.clean_phone(data["HomePhone"])
        self.street = cleaner.clean_case(data["Street"])
        self.city = cleaner.clean_case(data["City"])
        self.state = cleaner.clean_state(data["State"])
        self.zipcode = cleaner.clean_zipcode(data["Zipcode"]).strip()
        self.district = ""
