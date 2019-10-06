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







