

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

# 