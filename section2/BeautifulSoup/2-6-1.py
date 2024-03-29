from bs4 import BeautifulSoup
import sys
import io
import re #regex 정규표현식(regular express)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.daum.com">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""


soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id='naver').string)

# python 정규표현식 공부하고 오기
li = soup.find_all(href=re.compile(r"da"))

for e in li:
    print(e.attrs['href'])
    print(e.string)
