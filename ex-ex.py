import urllib.parse

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=drwtsn64'
parsed = urllib.parse.urlparse(url)

print(parsed)

query = urllib.parse.parse_qs(parsed.query, True)

print(query)

query['count'] = 200

print(query)

encoded = urllib.parse.urlencode(query, True)

print(encoded)

reversed = urllib.parse.ParseResult(parsed.scheme, parsed.netloc, parsed.path, parsed.params, encoded, parsed.fragment).geturl()

print(reversed)
