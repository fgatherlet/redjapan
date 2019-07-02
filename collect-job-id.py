from urllib.parse import urlparse, urlunparse, parse_qs, urlencode, parse_qsl, urljoin
import requests
import sys
import os
import os.path
import time
import random
import lxml
import lxml.html
from lxml import etree
import re

#import lxml.html as lx

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import prox

def prox_get_slowly(url):
    content, hitp = prox.prox_get(url)
    if content is None:
        return None
    if hitp:
        return content
    time.sleep(random.randrange(40, 80) * 0.1)
    return content

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
        content = prox_get_slowly(url2str)
        #content, hitp = prox.prox_get(url2str)
        #if hitp:
        #    #print("hit")
        #    pass
        #else:
        #    time.sleep(random.randrange(40, 80) * 0.1)
        #print("contnt-length:%s" % (len(content)))
        doc = lxml.html.document_fromstring(content)
        elms = doc.xpath("//a")
        #elms = doc.xpath("//a[starts-with(@href, '/job/')]")
        for elm in elms:
            href = elm.attrib["href"]
            if href:
                m = re.match("^/job/(\d+)", href)
                if m:
                    jobid = int(m[1])
                    jobids[jobid] = 1
    return list(jobids)
    #return jobids.keys()

def xfind(doc, xpathq):
    elms = doc.xpath(xpathq)
    if elms and len(elms) >= 1:
        return elms[0]

def xeasy_text(doc, xpathq):
    elm = xfind(doc, xpathq)
    if elm is None:
        return None
    return elm.text_content()

def analyze_job(jobid):
    xjob_url = job_url(jobid)
    #content, hitp = prox.prox_get(xjob_url)
    content = prox_get_slowly(xjob_url)
    doc = lxml.html.document_fromstring(content)
    #job-offer-main-content
    #main_contents = doc.xpath("//div[ contains(@class, 'job-offer-main-content') ]")
    jobinfo = {}
    elm = xfind(doc, "//a[text()='企業詳細']")
    if elm is None:
        return None
    m = re.match("^/company/(\d+)", elm.attrib['href'])
    if not m:
        return None
    jobinfo['id'] = jobid
    jobinfo['company_id'] = int(m[1])

    #<div class="job-offer-heading">
    jobinfo['heading'] = xeasy_text(doc, "//div[@class='job-offer-heading']")

    #<section class="com_content__basic-info">
    jobinfo['summary'] = xeasy_text(doc, "//section[@class='com_content__basic-info']")

    #<table class="detail-content-table js-impression"
    jobinfo['detail1'] = xeasy_text(doc, "(//table[ contains(@class, 'detail-content-table')] )[1]")

    #<table class="detail-content-table js-impression"
    jobinfo['detail2'] = xeasy_text(doc, "(//table[ contains(@class, 'detail-content-table')] )[2]")

    jobinfo['text'] = "{}{}{}{}".format(jobinfo['heading'], jobinfo['summary'], jobinfo['detail1'], jobinfo['detail2'])
    jobinfo['text'] = re.sub(r"[\s\n]+", " ", jobinfo['text'])

    return jobinfo

if __name__ == "__main__":
    master = {}
    jobids = get_jobids()
    for jobid in jobids:
        job = analyze_job(jobid)
        master[job['id']] = job['text']
        with open('/tmp/jobs', 'a') as out:
            print("{} {}".format(job['id'], job['text']),
                  file=out)
    #print(job['id'])
    #print(job['text'])
