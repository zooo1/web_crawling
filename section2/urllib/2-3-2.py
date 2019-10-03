import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

### urlencode ###

API = "https://www.ipify.org"

values = {
    'format': 'json'
}

print('before', values)
params = urlencode(values)
print(params)

url = API + "?" + params
print("요청 url: ", url)

req_data = req.urlopen(url).read().decode('utf-8')
print(req_data)
