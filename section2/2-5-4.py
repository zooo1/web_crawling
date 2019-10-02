from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

############# CSS selector ################
# 스크래핑에서 가장 많이 사용하는 방법이다.
# 구글에서 css 선택자 -> 원하는 것 하나 클릭해서 읽어보세용
html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select('div#main > h1')
print('h1', h1)
print('type of h1: ',type(h1))

h1 = soup.select_one('div#main > h1') # id는 유일하기 때문에 div를 써주지 않아도 된다. 하지만 써주는 것이 찾을 때는 도움이 되겠지
print(h1.string)

list_li = soup.select('div#main > ul.lecs > li')
for li in list_li:
    print("li >>> ", li.string)

