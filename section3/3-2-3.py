import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20')
print(r.text)
print(r.encoding)  # None
# 보기에는 json인데 이런식으로 하면 error 발생
# print(r.json())

r.encoding = 'utf-8'
print(r.encoding)  # utf-8


r = s.get('http://httpbin.org/stream/20')  # stream을 명시해주는 것이 좋다.
#### iter_lines ####
print(type(r.iter_lines(decode_unicode=True)))
for line in r.iter_lines(decode_unicode=True):
    print(line)
#     print(json.loads(line))


s.close()
