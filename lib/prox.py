import hashlib
import os
import os.path
import requests

def sha1(str):
    m = hashlib.sha1()
    m.update(str.encode())
    return m.hexdigest()

def ensure_path(path):
    os.makedirs(path, exist_ok=True)

def HttpError(Error):
    def __init__(self, code):
        self.code = code

def prox_get(url):
    xsha1 = sha1(url)
    path0 = xsha1[0:2]
    path1 = xsha1[2:]
    ensure_path(f"/tmp/pprox/{path0}/")
    cachefilepath = f"/tmp/pprox/{path0}/{path1}"
    if os.path.isfile(cachefilepath):
        rs = open(cachefilepath, "r")
        content = rs.read()
        return content, True
    else:
        res = requests.get(url)
        if res.status_code != 200:
            raise HttpError(res.status_code)
        content = res.text
        with open(cachefilepath, "w") as ws:
            ws.write(content)
        return content, False
