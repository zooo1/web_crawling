import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

src = "https://ssl.pstatic.net/tveta/libs/1249/1249571/29e3d4255f28cc9b00f1_20191001171657968.jpg"
f = req.urlopen(src).read()
save_path = "/Users/joanlee/Downloads/hw1.jpg"

with open(save_path, 'wb') as save_file:
    save_file.write(f)
    print("ok")
