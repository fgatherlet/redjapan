from urllib.parse import urlparse, urlunparse, parse_qs, urlencode, parse_qsl, urljoin
import requests
import sys
import os
import os.path
import time
import random
import lxml
import lxml.html
import re
#import lxml.html as lx

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

def job_url(jobid):
    return f"https://www.green-japan.com/job/{jobid}"

def get_jobids():
    jobids = {}
    for page in range(1, 42):
        qs['page'] = [page]
        query = urlencode(qs, True)
        url2 = url._replace(query=query)
        url2str = urlunparse(url2)
        print(url2str)
        content, hitp = prox.prox_get(url2str)
        if hitp:
            #print("hit")
            pass
        else:
            time.sleep(random.randrange(40, 80) * 0.1)
        #print("contnt-length:%s" % (len(content)))
        doc = lxml.html.document_fromstring(content)
        elms = doc.xpath("//a")
        #elms = doc.xpath("//a[starts-with(@href, '/job/')]")
        for elm in elms:
            href = elm.attrib["href"]
            if href:
                m = re.match("^/job/(\d+)", href)
                if m:
                    jobid = m[1]
                    jobids[jobid] = 1
    return jobids.keys()

def analyze_job(jobid):
    xjob_url = job_url(jobid)
    content, hitp = prox.prox_get(xjob_url)
    job-offer-main-content
    return content

if __name__ == "__main__":
    job = analyze_job(56762)
    print(job)
