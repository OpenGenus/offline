from bs4 import BeautifulSoup as bs
import lxml
def addheader(sp):
	new_link =  sp.new_tag("link")
	new_link.attrs["href"] = "cstmhdr.css"
	sp.head.insert(0,new_link)
	tag=sp.body
	new_tag=sp.new_tag('div',**{'class':'cheader'},id="cstmhdrdiv")
	tag.insert(0,new_tag)
	tag=sp.find("div",{"id":"cstmhdrdiv"})
	new_tag=sp.new_tag('nav',id="cstmhdrnav")
	tag.append(new_tag)
	tag=sp.find("nav",{"id":"cstmhdrnav"})
	new_tag=sp.new_tag('a',href="https://discourse.opengenus.org",id="cstmhdra1")
	tag.append(new_tag)
	new_tag=sp.new_tag('img',src="https://discourse-cdn-sjc2.com/standard17/uploads/opengenus/original/1X/5c936e504d024c2da59395fe5a9ca54241106f1b.png", alt="OpenGenus",height="50", width="205",id="cstmhdri1")
	tag=sp.find("a",{"id":"cstmhdra1"})
	tag.append(new_tag)
	new_tag=sp.new_tag('a',href="https://twitter.com/opengenus?lang=en",id="cstmhdra2")
	tag.append(new_tag)
	new_tag=sp.new_tag('img',src="https://logos-download.com/wp-content/uploads/2016/02/Twitter_logo_bird_transparent_png.png", alt="OpenGenus Twitter",height="35", width="43",id="cstmhdri2")
	tag=sp.find("a",{"id":"cstmhdra2"})
	tag.append(new_tag)
	#jstag =  sp.new_tag('script',type="text/javascript",src="cstmhdr.js")
	#sp.body.append(jstag)
	return sp
