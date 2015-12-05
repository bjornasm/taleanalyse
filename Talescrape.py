#!/usr/bin/python
from __future__ import division
import httplib2
import re
import sys
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup

speeches = []
urls = []


def getSpeeches(url):
    r = urllib.urlopen(url).read()
 
    soup = BeautifulSoup(r)
 
    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if 'taler?' in tag['href']:
        	print tag['href']
        	getContent(tag['href'])

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def getContent(url):
    r = urllib.urlopen(url).read()
 
    soup = BeautifulSoup(r)
    try:
		soup = soup.find("div", {"class": "speech"})
		soup = soup.find("div", {"class": "body"})
		urls.append(url)
		speeches.append(remove_tags(str(soup)).replace(',','').replace('.','').replace('!','').replace('?',''))
    except Exception, e:
		print Exception(" error")
		print url

def getDetails(url):
	r = urllib.urlopen(url).read()

	soup = BeautifulSoup(r)
	soup = soup.find("div", {"class": "speech"})
	print remove_tags(str(soup.find("div", {"class": "title"})))
	print remove_tags(str(soup.find("div", {"class": "speaker"})))
	print remove_tags(str(soup.find("div", {"class": "event"}))).replace('\n','')
	print remove_tags(str(soup.find("div", {"class": "location"}))).replace('\n','').replace('    ', '')
	print "\n"

if __name__ == "__main__":
	# getSpeeches('http://virksommeord.uib.no/taler')
	# stats = []
	# for speach in speeches:
	# 	stats.append(len(speach))
	# for i in range(0,10):
	# 	maxstatindex = stats.index(max(stats))
	# 	print urls[maxstatindex]
	# 	print stats[maxstatindex]
	# 	stats[maxstatindex] = 0
	toplist = ['http://virksommeord.uib.no/taler?id=6401','http://virksommeord.uib.no/taler?id=4461','http://virksommeord.uib.no/taler?id=3121','http://virksommeord.uib.no/taler?id=402','http://virksommeord.uib.no/taler?id=2621','http://virksommeord.uib.no/taler?id=3141','http://virksommeord.uib.no/taler?id=1001','http://virksommeord.uib.no/taler?id=4081','http://virksommeord.uib.no/taler?id=75','http://virksommeord.uib.no/taler?id=103']
	for speech in toplist:
		getDetails(speech)




