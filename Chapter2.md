# 스크래핑 전 Chrome 개발자 도구에서 알아야 할 것들

### Dom 구조 분석(요소검사)

### 선택자(selector) 추출

copy selector

### console 도구

console 창에서 다양한 연산을 실행할 수 있다. js File을 붙여놓고 실행하면 귀찮으니까..1

memory -> 병목현상, 메모리 누수 등을 알려준다.

network -> preserve log를 반드시 알아두자

performance -> record f5 -> network 탭의 녹화와 같다.

### source 

### network 및 기타



# Python urllib을 활용한 웹에서 필요한 데이터 추출하기(1)

## Web crawling 방식

1. HTML에서 파일을 다운로드 한 후
2. page에서 필요한 정보(text, img)등을 파싱하여 
3. txt, json, DB의 형태로 서버에게 정보를 보내준다.



## tips

#### atom에서 한글을 출력하기 위해 필요한 코드

```python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
```



## library

### urllib

>  URLs로 작업하는 모듈을 모아놓은 패키지
>
> - [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) : URL을 열고 읽기 위해 사용한다.
> - [`urllib.error`](https://docs.python.org/3/library/urllib.error.html#module-urllib.error) : urllib.request에서 발생하는 예외를 포함하고 있다.
> - [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) : url을 parsing 하는 데 쓰인다.
> - [`urllib.robotparser`](https://docs.python.org/3/library/urllib.robotparser.html#module-urllib.robotparser) : robots.txt 파일을 파싱하는 데 쓰인다.
> - 

### urllib.request

> 주로 http 형식의 url을 여는데 쓰이는 함수, 클래스를 정의해 놓은 모듈이다.

#### urllib.request.urlopen

> string 또는 request object 형태의 url을 열어준다. 
>
> HTTP, HTTPS URL에서는 `http.client.HTTPResponse` 객체(조금 수정된)를 반환하고 FTP, file, data URL에서는 `urllib.response.addinfourl` 객체를 반환한다. 
>
> 아래와 같은 메소드를 지닌다.

- `geturl()` : 검색된 리소스의 url을 리턴한다. 
- `info()` : 페이지의 헤더 같은 메타 정보를 리턴한다.
- `getcode()` :응답에 대한 HTTP 상태 코드를 리턴한다.



## code

### ver1 - urlretrieve

```python
import urllib.request as dw
img_url = "http://img.hani.co.kr/imgdb/resize/2018/0313/00500561_20180313.JPG"
html_url = "http://google.com"

save_path = "/Users/joanlee/Downloads/test1.jpg"
save_path2 = "/Users/joanlee/Downloads/index.html"

dw.urlretrieve(img_url, save_path)
dw.urlretrieve(html_url, save_path2)
```



### ver2 - urlopen

```python
import urllib.request as dw
img_url = "http://img.hani.co.kr/imgdb/resize/2018/0313/00500561_20180313.JPG"
html_url = "http://google.com"

save_path = "/Users/joanlee/Downloads/test1.jpg"
save_path2 = "/Users/joanlee/Downloads/index.html"

f = dw.urlopen(img_url).read()
f2 = dw.urlopen(html_url).read()

save_file1 = open(save_path1, 'wb') # w: write, r: read, a: add
save_file1.write(f)
save_file1.close()
```

입출력 작업, db connection 작업 후에는 resource를 반납해야한다. 즉, 닫는 작업이 필요하다.



### ver3 - with open

```python
with open(save_path2, 'wb') as save_file2:
    save_file2.write(f2)
```

with를 벗어나는 문장에서 resource가 자동으로 반납된다. 즉, 닫는 작업이 필요 없다.



### urlretrieve VS urlopen

urlretrieve 는 데이터를 저장 -> read 형태로 open -> 변수에 할당 -> 파싱 -> 저장

urlopen은 하드디스크에 쓰기 전에 이미 변수에 할당 -> 파싱 -> with 구문 이용하여 저장하는 방식이다.

urlretrieve는 parsing이 필요없는 데이터를 저장할 때 유용하고 urlopen은 저장하기 전에 분석이 필요한 경우에 사용하는 것이 유용하다.



# 2019.10.01

# Python urllib을 활용한 웹에서 필요한 데이터 추출하기(2)

## libraray

### urllib.urlrequest.urlopen

* `geturl()` : 검색된 리소스의 url을 리턴

- `info()` : 페이지의 헤더 같은 메타 정보를 리턴한다.
- `getcode()` :응답에 대한 HTTP 상태 코드를 리턴한다.

* `status` : 응답에 대한 HTTP 상태 코드
* `getheaders() `: 서버에 대한 정보를 리스트로 반환
* `read([nBytes])`: n byte의 데이터를 바이트 문자열로 반환
* `read.decode('utf-8')` : 사람이 읽을 수 있는 형태로 decode해줌

### status

* 200: 성공
* 403: 거부당함
* 404: 페이지가 존재하지 않음
* 500: 서버 내부 오류



### urllib.parse

> URL string을 component(주소 스케마, 네트워크 위치, 경로) 등으로 분리, component를 URL string으로 결합, 주어진 base URL을 이용하여 상대적인 URL을 절대 URL 로 변환 시키는 표준 인터페이스를 정의한 모듈이다.
>
> URL parsing 함수는 url string을 component로 분리하거나 URL component를 URL string으로 합치는 데 초점을 둔다.
>
> * `urlparse` : URL을 6개의 컴포넌트로 분리하여 6개의 원소를 가진 튜플을 리턴한다. 
> * `urljoin` : base url에 다른 url을 합쳐준 것을 리턴한다.
> * `urlencode` : mapping 되는 object 또는 두 개의 요소를 가진 튜플을 string 형태로 변환한다. 두 개의 요소는 **key=value** 형태의 값을 가지게된다.
> * 







## code

### urlopen methods

```python
import urllib.request as req

url = "http://www.encar.com"

mem = req.urlopen(url)

print(type(mem))
print("geturl ", mem.geturl())
print("status ", mem.status)
print("headers ", mem.getheaders())
print("info ", mem.info())
print("code ", mem.getcode())
print("read ", mem.read(50).decode("utf-8")) # euc-kr
```



### urllib.parse.urlencode

```python
from urllib.parse import urlencode

API = "https://www.ipify.org"
values = {
    'format': 'json'

print('before', values)
params = urlencode(values)
print(params)

url = API + "?" + params
print("요청 url: ", url)

req_data = req.urlopen(url).read().decode('utf-8')
print(req_data)

```



# 2019.10.03

# CSS selector

css selector는 HTML의 요소를 찾기 위해 쓰인다. 

자세한 내용과 예시는 이 [페이지](https://www.w3schools.com/cssref/trysel.asp) 를 참고하도록 하자

`.class명` : 해당 클래스의 모든 요소

`#id명` : 해당 아이디의 모든 요소 (아이디는 고유한 값을 지닌다.)

`element1, element2, ..` : 해당하는 것들의 모든 요소

`상위element 하위element ` : 상위 요소에 포함되는 모든 하위 요소

`상위 element > 하위element` : 상위 요소의 **자식** 하위 요소

`element1 + element2` : 각 element1 다음에 오는 element2 요소 

`형제element1 ~ 형제element2` : element1의 형제인 모든 요소인 element2

`*` : 모든 요소

`[attribute]`: 특정 속성을 가진 모든 요소

`[attr=value]` : 특정 속성이 주어진 값과 일치하는 모든 요소

`[attr$=value]` : 특성 속성이 주어진 값으로 끝나는 모든 요소

`[attr|=value]` : 특정 속성이 주어진 값과 같거나 주어진 값으로 시작하고 하이픈(-)이 따라붙는 모든 요소  

`[attr^=value]` : 특정 속성이 주어진 값으로 시작하는 모든 요소

`[attr~=value]` : 특정 속성이 주어진 값을 포함하는 모든 요소

`[attr*=value]` : 특정 속성이 주어진 값을 포함하는 모든 요소

`:checked` `:disabled`  `:empty`  `:focus`

`element:first-child` : 특정 요소 부모의 첫 번째 자식에 해당되는 모든 요소

`element::first-letter`  `element::first-line` `element:first-of-type`

`element:hover` : 특정 element에 마우스를 올리는 경우 그 요소가 선택된다.

`input:in-range` `input:out-of-range` `input:invalid` `input:valid`

`element:last-child` : 특정 요소 부모의 마지막 자식인 모든 요소



# BeautifulSoup 사용법 및 간단 웹 파싱 기초(1)

## BeautifulSoup

~~예쁜 국물~~

> HTML, XML 파일의 데이터를 추출하는 데 사용하는 파이썬 라이브러리이다.



### 설치 방법 

![bs4 install](./assets/bs4.png)



### 사용 방법

``` python
from bs4 import BeautifulSoup
```

BeautifulSoup 객체를 import



### 데이터 구조 파악하기

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html_parser')
```

soup => string 형태의 html_doc 을 html_parser를 이용하여 파싱한 형태



#### type, prettify, string

``` python
type(soup) 								# <class 'bs4.BeautifulSoup'>
soup											# html_doc 내용
soup.prettify()						# html_doc 내용 indenting 되어서 나옴
h1 = soup.html.body.h1		# 데이터에 접근하는 방식
h1.type										# <class 'bs4.element.Tag'> 
h1 												# <h1>파이썬 BeautifulSoup 공부</h1>
h1.string									# 파이썬 BeautifulSoup 공부

```

#### next_sibling, prev_sibling

```python
p1 = soup.html.body.p			# 데이터에 접근하는 방식
p1												# <p>태그 선택자</p>
p2 = p1.next_sibling			# 다음 요소에 접근하는 방법		
p2												# ' '			

#### 해결방안(번거로움) ####
p2 = p1.next_sibling.next_sibling  # <p>CSS 선택자</p>
p3 = p1.previous_sibling.next_sibling  # <p>태그 선택자</p>
```

예상되는 p2 값은  `<p>css 선택자<p>` 이지만 아무것도 출력되지 않는다. html_doc을 작성할 때, 엔터키를 치지 않았더라면 예상 값이 p2의 값이 되었을 것이다. 엔터키를 치면 우리 눈에는 보이지 않는  `\n`  키가 p2에 할당된다. 이것을 해결하기 위해서는 공백을 없애주는 작업을 거쳐야한다. 



## library

### find_all(name, attrs, recursive, string, limit, **kwargs)

> 필터에 걸러지는 모든 자손들을 찾아주는 메소드이다. 이 모든 자손들을 모아 리스트 형태로 리턴한다.
>
> 이것은 굉장히 대중적인 메소드이기 때문에 아래와 같이 줄여서 사용할 수 있다. 
>
> ```python
> soup.find_all('a')
> soup('a')
> ```

#### find_all()의 filter 종류

* 문자열(string) 

  ```python
  soup.find_all('b')	# [<b>The Dormouse's story</b>]
  ```

* 정규표현식(regular expression)

  ```python
  import re
  for tag in soup.find_all(re.compile("^b")):
      print(tag.name)
  # body
  # b
  ```

* 리스트(list)

  ```python
  soup.find_all(["a", "b"])
  # [<b>The Dormouse's story</b>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
  ```

* True

  ```python
  for tag in soup.find_all(True):
    print(tag.name)
  # html
  # head
  # title
  # body
  # p
  # b
  ```

* 함수(function)

  ```python
  def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
  
  soup.find_all(has_class_but_not_id)
  # [<p class="title"><b>The Dormouse's story</b></p>, <p class="story">...</p>]
  ```

  

### select([tag name]), select_one([tag name])

> * select : tag name에 해당하는 요소들을 모아 리스트 형태로 리턴한다.
> * select_one: 한 개만 리턴한다.

```python
from bs4 import BeautifulSoup
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

soup = BeautifulSoup(html, 'html_parser')
list_li = soup.select('div#main > ul.lecs > li')
# [<li>Java 초고수 되기</li>, <li>파이썬 기초 프로그래밍</li>, <li>파이썬 머신러닝 프로그래밍</li>, <li>안드로이드 블루투스 프로그래밍</li>]
one_li = soup.select_one('div#main > ul.lecs > li')
# <li>Java 초고수 되기</li>
```



## code 

```python
  
from bs4 import BeautifulSoup

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
print('type of select: ',type(h1))

h1 = soup.select_one('div#main > h1') # id는 유일하기 때문에 div를 써주지 않아도 된다.
print(h1)
print("type of select_one: ", type(h1))

list_li = soup.select('div#main > ul.lecs > li')
for li in list_li:
    print("li >>> ", li.string)
```







