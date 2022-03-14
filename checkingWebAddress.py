import requests

res = requests.get('https://virtualpeople.pl/status')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))