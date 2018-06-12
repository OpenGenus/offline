import json
from bs4 import BeautifulSoup
def dothis(urlin,count,hash_map):
	import download_webpage
	finalhtml=download_webpage.core(urlin)
	for linkon in finalhtml.find_all('a'):
		try:
			linkon['href']=hash_map[linkon['href']]
		except KeyError:
			pass
	outhtml=str(finalhtml)
	temp=str(count)+'.html'
	if temp and temp != '-':
		with open(temp,'w') as f:
			f.write(outhtml)
	else:
		sys.stdout.write(outhtml)
file=open('output.txt','r')
i=1
hash_map={}
with open('mapping.json') as jsonfile:
	jsondata=json.load(jsonfile)
	for indx in jsondata['index']:
		hash_map[indx['url']]=indx['filename']

for link in file:
	print ("Downloading "+link)
	dothis(link.rstrip(),i,hash_map)
	i+=1
