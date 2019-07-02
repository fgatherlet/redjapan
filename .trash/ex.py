from urllib.parse import urlparse, parse_qs, urlencode, ParseResult

urlstr = "https://www.green-japan.com/search_key/01?key=zc9dua2ci6wqmb1yftkl&keyword="
url = urlparse(urlstr)
qs = parse_qs(url.query, True)
print("qs:%s" % (qs))
qs['page'] = 10

query = urlencode(qs, True)
print(query)
