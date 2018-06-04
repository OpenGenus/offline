import json
import bs4
import requests
def tojson(fileopen,data):
	with open(fileopen,'w') as f:
		f.write("{\"index\":")
		json.dump(data,f,indent=2)
		f.write("}")
filejson='mapping.json'
index=[]
file=open('output.txt','r')
i=0
for link in file:
	data={}
	print(link)
	resp=requests.get(link.rstrip())
	soup=bs4.BeautifulSoup(resp.text,'lxml')
	link.strip()
	data['url']=link.strip()
	data['filename']=str(i+1)+'.html'
	temp=soup.title.string
	data['meta-title']=temp
	metas=soup.find_all('meta')
	temp2= ([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ])
	if(len(temp2) !=0 ):
		temp3=temp2[0]
		temp3.strip()
		data['meta-description']=temp3
	else:
		data['meta-description']='no description'
	index.append(data)
	i=i+1
tojson(filejson,index)
