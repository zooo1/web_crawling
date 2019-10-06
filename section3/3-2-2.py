import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Response 상태 코드
s = requests.Session()
r = s.get('https://httpbin.org/get')

print(r.status_code)
print(r.ok)

if ok == True:~~~
if status_code == 200: ~~~

# #### JSON data Handling ####
url = 'https://jsonplaceholder.typicode.com/'
r = s.get(url+'posts/1')
print(r.text)
print()
# requests module에서 제공하는 함수 json()
print(r.json())
# python에서 제공하는
print(r.json().keys(), '\n')
print(r.json().values(), '\n')
print(r.encoding)
print(r.content) # content를 binary 형태
print(r.raw)

s.close()

with requests.Session() as r:
    print(r.get(url+'posts/1').json())
