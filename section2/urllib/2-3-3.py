import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

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

# get 방식으로 url을 받아와서 파라미터 전달하는 방법
# dictionary, tuple, list
# urlparse, urlencode
# decode, geturl, status, ,..

# 과제
# 네이버 상단, 우측 광고를 나의 컴퓨터에 저장하기
# 이미지, 동영상을 다운로드
