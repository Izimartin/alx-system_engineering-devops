#import urllib.request
#with urllib.request.urlopen('http://python.org/') as response:
#   html = response.read()
#   print(html)
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)