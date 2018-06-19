from bs4 import BeautifulSoup as bs
import lxml
def addheader(sp):
	new_link =  sp.new_tag("link")
	new_link.attrs["href"] = "custom_opengenus_offline_header_css.css"
	sp.head.insert(0,new_link)
	tag=sp.body
	new_tag=sp.new_tag('div',**{'class':'custom_opengenus_offline_header_class'},id="custom_opengenus_offline_header_div")
	tag.insert(0,new_tag)
	tag=sp.find("div",{"id":"custom_opengenus_offline_header_div"})
	new_tag=sp.new_tag('nav',id="custom_opengenus_offline_header_nav")
	tag.append(new_tag)
	tag=sp.find("nav",{"id":"custom_opengenus_offline_header_nav"})
	new_tag=sp.new_tag('a',href="https://discourse.opengenus.org",id="custom_opengenus_offline_header_a1")
	tag.append(new_tag)
	new_tag=sp.new_tag('img',src="https://discourse-cdn-sjc2.com/standard17/uploads/opengenus/original/1X/5c936e504d024c2da59395fe5a9ca54241106f1b.png", alt="OpenGenus",height="50", width="205",id="custom_opengenus_offline_header_i1")
	tag=sp.find("a",{"id":"custom_opengenus_offline_header_a1"})
	tag.append(new_tag)
	new_tag=sp.new_tag('a',href="https://twitter.com/opengenus?lang=en",id="custom_opengenus_offline_header_a2")
	tag.append(new_tag)
	new_tag=sp.new_tag('img',src="https://logos-download.com/wp-content/uploads/2016/02/Twitter_logo_bird_transparent_png.png", alt="OpenGenus Twitter",height="35", width="43",id="custom_opengenus_offline_header_i2")
	tag=sp.find("a",{"id":"custom_opengenus_offline_header_a2"})
	tag.append(new_tag)
	#jstag =  sp.new_tag('script',type="text/javascript",src="custom_opengenus_offline_header_js.js")
	#sp.body.append(jstag)
	return sp
