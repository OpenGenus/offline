import urllib.request as Ureq
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
def outputprint(url_in):
	file = open('output.txt','a')
	file.write('\n'+url_in)
	file.close()
def task(url,allurls=[]):
	url_p=urlparse(url)
	domain='{uri.scheme}://{uri.netloc}/'.format(uri=url_p)
	resp=requests.get(url)
	soup=bs(resp.text,'html.parser')
	for link in soup.find_all('a'):
		temp=link.get('href')
		domain_len=len(domain)
		found=1
		j=0
		while(found==1 and j<domain_len):
			if temp is not None:
				if temp[j]!=domain[j]:
					found = 0
				j=j+1
		if found ==1:
			urllen=len(allurls)
			found = 0
			i=0
			while(found==0 and i<urllen):
				if allurls[i]==temp:
					found=1
				i=i+1
			if found==0:
				allurls.append(temp)
				outputprint(temp)
				task(temp,allurls)


URl_User="abc"
outputarr=[]
URL_User=input('Enter URl : ')
URL_User.replace(" ","")
task(URL_User,outputarr)
