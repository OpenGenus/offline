import download_webpage
file=open('output.txt','r')
i=1
for link in file:
	print ("Downloading "+link,end='')
	download_webpage.main(link,i)
	i+=1