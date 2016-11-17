import re
from pdb import set_trace as bp

#cleaner.py
def clean_case(data):
    if data is None or data == '':
        return 'NONE'
    else:
        return data.lower().strip()

def clean_zipcode(data):
    if data is None or data == '':
        return '00000'
    else:
        return str(data).zfill(5)

def clean_phone(data):
    if data is None:
        return '000-000-0000'

    data = re.sub('[^0-9]+', '', data)

    if len(data) == 11:
        data = data[1:]
    if len(data) != 10:
        return '000-000-0000'
    if len(data) == 10:
        d = list(data)
        d.insert(3, '-')
        d.insert(7, '-')
        return ''.join(d)

def clean_state(data):
    if data is None or data == '':
        return 'none'
    else:
        return data.lower()
