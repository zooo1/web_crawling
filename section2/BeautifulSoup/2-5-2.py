# pip install beautifulsoup4
from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')

print('soup type: ', type(soup))
print('soup: \n', soup)
print('prettified: \n', soup.prettify)

h1 = soup.html.body.h1
print('type of h1: ', type(h1)) # <class 'bs4.element.Tag'>
print('h1: ', h1)
print('h1 string: ', h1.string)

p1 = soup.html.body.p
print('p1: ', p1)
p2 = p1.next_sibling
print('p2: ', p2) # 아무것도 가져오지 않는다.
# 무엇을 가져온 것인가?
# html에서 줄바꿈을 하지 않았다면 우리가 예상하는 p2를 가져왔을 것이다.
# 하지만, 엔터를 쳤기 때문에 <p>CSS 선택자</p>가 아닌 '\n'을 가져올 것이다.
# 해결하기 위해서는 공백을 없애주는 작업을 거친다.

p2 = p1.next_sibling.next_sibling
print('p2: ', p2)
p3 = p1.previous_sibling.next_sibling
print('p3: ', p3)

print('h1 >> ', h1.string)
print('p >> ', p1.string)
print('p >> ', p2.string)

# 계속 next_sibling, prev_sibling을 사용할 수만은 없다.
# (html의 코드가 변경될 수 있기 때문에)
# 하지만 기본적인 것이니까 알아두도록 하자! ㅎㅎ
