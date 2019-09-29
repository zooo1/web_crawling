import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

img_url = "http://img.hani.co.kr/imgdb/resize/2018/0313/00500561_20180313.JPG"
html_url = "http://google.com"

save_path = "/Users/joanlee/Downloads/test1.jpg"
save_path2 = "/Users/joanlee/Downloads/index.html"

dw.urlretrieve(img_url, save_path)
# 매개변수로 경로와 저장 경로를 받는다.
dw.urlretrieve(html_url, save_path2)


print("다운로드 완료!")
