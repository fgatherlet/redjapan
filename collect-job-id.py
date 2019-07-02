from urllib.parse import urlparse, urlunparse, parse_qs, urlencode, parse_qsl, urljoin
import requests
import sys
import os
import os.path
import time
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import prox

url_base = "https://www.green-japan.com/search_key/01?key=zc9dua2ci6wqmb1yftkl&keyword="
url = urlparse(url_base)
print(url)
print("---")
print(urlunparse(url))
print("---")
#query_hash = parse_qs(url.query, keep_blank_values=True)
qs = parse_qs(url.query, True)
#print(query_hash)
#print(urlunparse(url))
print("---")
print(f"netloc:{url.netloc}")
print(f"query:{url.query}")
print(f"params:{url.params}")
print("---")

# 41pages
def main():
    for page in range(1, 42):
        qs['page'] = [page]
        query = urlencode(qs, True)
        url2 = url._replace(query=query)
        url2str = urlunparse(url2)
        print(url2str)
        content, hitp = prox.prox_get(url2str)
        if hitp:
            print("hit")
        else:
            time.sleep(random.randrange(40, 80) * 0.1)
        print("contnt-length:%s" % (len(content)))

if __name__ == "__main__":
    main()
