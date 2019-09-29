import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

img_url = "http://img.hani.co.kr/imgdb/resize/2018/0313/00500561_20180313.JPG"
html_url = "http://google.com"

save_path1 = "/Users/joanlee/Downloads/test1.jpg"
save_path2 = "/Users/joanlee/Downloads/index.html"

f = dw.urlopen(img_url).read()
f2 = dw.urlopen(html_url).read()

save_file1 = open(save_path1, 'wb') # w: write, r: read, a: add
save_file1.write(f)
save_file1.close()
# 입출력 작업, db connection 작업 후에는
# resource 반납해야한다. (닫는 작업)

# with를 벗어나는 문장에서 resource가 자동으로 반납된다.
# close()를 사용하지 않아도 됨!
# 간지나고 가독성이 좋으니까 이것을 쓰도록 하자 ㅎㅎ
with open(save_path2, 'wb') as save_file2:
    save_file2.write(f2)

####### urlretrieve vs urlopen #######
# urlretrieve :
# 다이렉트로 불러온다.
# 저장 -> open("r") -> 변수에 할당 -> 파싱 -> 저장
# 용도: 사자 사진을 grouping 해서 다운 받을 때 (여러 문서, 사진 등을 받아올 때)
# urlopen : 하드디스크에 쓰기 전에 이미 변수에 할당 함. 메모리 변수에 할당
# 변수 할당 -> 파싱 -> with 구문 통해 저장(db, ...)
# 용도: 중간에 분석이 필요한 경우 사용함

print("다운로드 완료!")
