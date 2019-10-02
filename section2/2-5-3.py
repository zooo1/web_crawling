from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

###### 태그 선택자를 활용하여 원하는 element를 가져오자 ######
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
# a 태그 안에 있는 속성(href)의 url 부분을 연속으로 가져와서 파싱한 후 출력
# li tag 의 모든 정보를 가져오자

# 태그 선택자 -> 태그에 직접 접근 
links = soup.find_all("a")
print(type(links)) # <class 'bs4.element.ResultSet'>
a = soup.find_all('a', string='daum') # 조건에 맞는 모든 것을 가져온다
print('a', a)
b = soup.find('a', string='daum') # 조건에 맞는 것 한 개만 가져온다.
print('b', b)
c = soup.find_all('a', limit=2)
print('c', c)
d = soup.find_all(string=['naver', 'google'])  # 일반적으로는 정규 표현식을 사용한다.
print('d', d)

# css 선택자를 가장 많이 사용한다.

for a in links:
    # print('a', type(a), a)
    # print(a)
    href = a.attrs.get('href')
    # href = a.attrs['href']
    txt = a.string
    # print('txt >>', txt, "\t", 'href >>', href)
    # print()
