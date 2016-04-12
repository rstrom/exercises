from datetime import datetime
from urllib.request import urlopen
import json


def is_date(s, f):
    try:
        datetime.strptime(s, f)
    except ValueError:
        return False
    else:
        return True


def clean_int(n):
    # - indicates missing data
    if n == '-':
        return 0
    else:
        return int(n)

base_url = 'http://or.water.usgs.gov/non-usgs/bes/'
endpoint = 'mt_tabor.rain'

with urlopen(base_url + endpoint) as f:
    rows = [r.decode('utf-8').split() for r in list(f) if len(r.split()) > 0]
    days_hourly = [
        {
            'date': d[0],
            'hourly': [clean_int(h) for h in d[2:]]
        } for d in rows if is_date(d[0], '%d-%b-%Y')
    ]
    with open(endpoint + '.js', 'w') as js:
        js.write('var rainfall = ' + json.dumps(days_hourly))
