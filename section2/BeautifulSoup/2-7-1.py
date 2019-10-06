from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

URL = "http://finance.daum.net/"

res = req.urlopen(URL).read()
soup = BeautifulSoup(res, 'html.parser')

# print(soup.prettify())

top = soup.select_all("list boxKospi")
print(top)
