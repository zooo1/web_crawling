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

### urllib

>  URLs로 작업하는 모듈을 모아놓은 패키지
>
> - [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) : URL을 열고 읽기 위해 사용한다.
> - [`urllib.error`](https://docs.python.org/3/library/urllib.error.html#module-urllib.error) : urllib.request에서 발생하는 예외를 포함하고 있다.
> - [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) : url을 parsing 하는 데 쓰인다.
> - [`urllib.robotparser`](https://docs.python.org/3/library/urllib.robotparser.html#module-urllib.robotparser) : robots.txt 파일을 파싱하는 데 쓰인다.

#### urllib.request

urllib.request는 주로 http 형식의 url을 여는데 쓰이는 함수, 클래스를 정의해 놓은 모듈이다.



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

# Python urllib을 활용한 웹에서 필요한 데이터 추출하기(1)

`urllib.request.``urlopen`(*url*, *data=None*, [*timeout*, ]***, *cafile=None*, *capath=None*, *cadefault=False*, *context=None*)

Open the URL *url*, which can be either a string or a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) object.

*data* must be an object specifying additional data to be sent to the server, or `None` if no such data is needed. See [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) for details.

urllib.request module uses HTTP/1.1 and includes `Connection:close` header in its HTTP requests.

The optional *timeout* parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). This actually only works for HTTP, HTTPS and FTP connections.

If *context* is specified, it must be a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext) instance describing the various SSL options. See [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection) for more details.

The optional *cafile* and *capath* parameters specify a set of trusted CA certificates for HTTPS requests. *cafile* should point to a single file containing a bundle of CA certificates, whereas *capath* should point to a directory of hashed certificate files. More information can be found in [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations).

The *cadefault* parameter is ignored.

This function always returns an object which can work as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) and has methods such as

- `geturl()` — return the URL of the resource retrieved, commonly used to determine if a redirect was followed
- `info()` — return the meta-information of the page, such as headers, in the form of an [`email.message_from_string()`](https://docs.python.org/3/library/email.parser.html#email.message_from_string) instance (see [Quick Reference to HTTP Headers](http://jkorpela.fi/http.html))
- `getcode()` – return the HTTP status code of the response.

For HTTP and HTTPS URLs, this function returns a [`http.client.HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse) object slightly modified. In addition to the three new methods above, the msg attribute contains the same information as the [`reason`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.reason) attribute — the reason phrase returned by server — instead of the response headers as it is specified in the documentation for [`HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse).

For FTP, file, and data URLs and requests explicitly handled by legacy [`URLopener`](https://docs.python.org/3/library/urllib.request.html#urllib.request.URLopener) and [`FancyURLopener`](https://docs.python.org/3/library/urllib.request.html#urllib.request.FancyURLopener) classes, this function returns a `urllib.response.addinfourl` object.

Raises [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError) on protocol errors.

Note that `None` may be returned if no handler handles the request (though the default installed global [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector) uses [`UnknownHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.UnknownHandler) to ensure this never happens).

In addition, if proxy settings are detected (for example, when a `*_proxy` environment variable like `http_proxy` is set), [`ProxyHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler) is default installed and makes sure the requests are handled through the proxy.

The legacy `urllib.urlopen` function from Python 2.6 and earlier has been discontinued; [`urllib.request.urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen) corresponds to the old `urllib2.urlopen`. Proxy handling, which was done by passing a dictionary parameter to `urllib.urlopen`, can be obtained by using [`ProxyHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler) objects.

*Changed in version 3.2:* *cafile* and *capath* were added.

*Changed in version 3.2:* HTTPS virtual hosts are now supported if possible (that is, if [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI) is true).

*New in version 3.2:* *data* can be an iterable object.

*Changed in version 3.3:* *cadefault* was added.

*Changed in version 3.4.3:* *context* was added.

*Deprecated since version 3.6:* *cafile*, *capath* and *cadefault* are deprecated in favor of *context*. Please use [`ssl.SSLContext.load_cert_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain) instead, or let [`ssl.create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context) select the system’s trusted CA certificates for you.



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







