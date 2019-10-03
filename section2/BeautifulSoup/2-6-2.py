from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open('food-list.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

### nth-of-type ###
# nth-of-child와의 차이점?
print("1", soup.select_one("li:nth-of-type(5)"))
# 자식, 자손 선택자의 차이점
# #ac-list > ~~ : 자식 선택자
# #ac-list ~~ : 자손 선택
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
# select는 list 형태로 되어있기 때문에 인덱스로 접근해야한다.
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4", soup.select("#ac-list > li.alcohol.high")[0].string)

param = {'data-lo':'cn', 'class':'alcohol'}
# 가독성이 좋음
print("5", soup.find("li", param))
print("6", soup.find(id="ac-list").find("li", param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
