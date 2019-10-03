from urllib.parse import urljoin

base_url = "http://test.com/html/a.html"

print(">>", urljoin(base_url, "b.html"))
print(">>", urljoin(base_url, "sub/b.html"))
print(">>", urljoin(base_url, "../index.html"))
print(">>", urljoin(base_url, "../img/img.jpg"))
print(">>", urljoin(base_url, "../css/img.css"))