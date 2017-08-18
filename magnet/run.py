# -*- coding: utf-8 -*-
import urllib2
import sys
#BeautifulSoup3不需要修改，BeautifulSoup4，改成from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding( "utf-8" )

def getcontent(url):
	print url
	req = urllib2.Request(url)
	res = urllib2.urlopen(req)
	magnetlist=[]
	html = res.read()
	res.close()
	soup = BeautifulSoup(html)
	#BeautifulSoup3不需要修改，BeautifulSoup4，改成soup.find_all('a')
	#allentry=soup.findAll('a')
	soup.find_all('a')
	for link in allentry:
		if "magnet:"==link.get('href')[0:7]:
			magnetlist.append(link.get('href'))
	magnetlist = [line+'\n' for line in magnetlist]
	f =open("magnet.txt",  "a")
	f.writelines(magnetlist)
	f.close()

def main():
	site="http://bt.shousibaocai.com/search/"
	keyword="地心引力"
	keyword=urllib2.quote(keyword)
	#总共抓前多少页
	page=3
	for i in range(1,page):
		searchurl=site+keyword+"/"+str(i)
		getcontent(searchurl)

if __name__ == '__main__':
	main()
	#end Jarett