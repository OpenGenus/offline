from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import tldextract
def outputprint(url_in):
	file = open('output.txt','a')
	file.write('\n'+url_in)
	file.close()
def obtaindomain(url_inn):
	list =tldextract.extract(url_inn)
	domainout=list.domain+'.'+list.suffix
	return domainout
def task(url,domain,allurls=[]):
	resp=urlopen(url)
	soup=bs(resp.read(),"lxml")
	for link in soup.find_all('a'):
		temp=link.get('href')
		if temp is not None:	
			domain_temp=obtaindomain(temp)
			if domain_temp==domain:
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
					task(temp,domain,allurls)
URl_User="abc"
outputarr=[]
URL_User=input('Enter URl : ')
URL_User.replace(" ","")
dom=obtaindomain(URL_User)
task(URL_User,dom,outputarr)
