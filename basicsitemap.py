import urllib.request as Ureq
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
def task(url,allurls=[]):
	url_p=urlparse(url)
	domain='{uri.scheme}://{uri.netloc}/'.format(uri=url_p)
	resp=requests.get(url)
	soup=bs(resp.text,'html.parser')
	for link in soup.find_all('a'):
		temp=link.get('href')
		if temp is not None and domain in temp:
			urllen=len(allurls)
			found = 0
			i=0
			while(found==0 and i<urllen):
				if allurls[i]==temp:
					found=1
				i=i+1
			if found==0:
				allurls.append(temp)
				print (temp)
				task(temp,allurls)


URl_User="abc"
outputarr=[]
URL_User=input('Enter URl : ')
task(URL_User,outputarr)
