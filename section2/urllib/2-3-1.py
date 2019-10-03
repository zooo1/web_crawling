import sys
import io
import urllib.request as req
import pprint
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

# print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl ", mem.geturl())
# print("status ", mem.status)
# print("headers ", mem.getheaders())
# print("info ", mem.info())
# print("code ", mem.getcode())
# print("read ", mem.read(50).decode("utf-8")) # euc-kr

# # status
# # 200(ok), 404(no page), 403(rejected), 500(server error)
#
# print(mem.info())
# # read(int) -> 사용자가 설정한 양 만큼 읽어온다. 디폴트: 전체
# print(mem.read(50))
#
# # decoding:s 문자열이 깨지거나 캐릭터셋이 맞춰야 나온다.
# # read 너무 많이 하면 read 할 때 디코드에서 에러남
# print("read ", mem.read().decode("utf-8")) # euc-kr

print(urlparse("http://www.encar.com?test=test67"))
