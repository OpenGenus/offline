from bs4 import BeautifulSoup as bs
import lxml
def addheader(sp):
	tag=sp.body
	temp='''<center><br><nav><a href=\"https://discourse.opengenus.org\"><img src=\"https://discourse.opengenus.org/uploads/opengenus/original/1X/b2f73aeb998e62df86bce346aae9de58784e0fcd.png\" alt= \"OpenGenus\" height=\"70\" width=\"70\"></a> | 
	<a href=\"https://twitter.com/opengenus?lang=en\"><img src=\"https://en.wikipedia.org/wiki/File:Twitter_bird_logo_2012.svg\" alt=\"OpenGenus Twitter\" height=\"70\" width=\"70\"></a> | 
	<a href=\"https://github.com/OpenGenus\"><img src = \"https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png\" alt =\"OpenGenus Github\" height=\"70\" width=\"70\"></a> | 
	<a href=\"https://in.linkedin.com/company/opengenus\"><img src=\"https://static.licdn.com/sc/h/95o6rrc5ws6mlw6wqzy0xgj7y\" alt=\"Opengenus LinkedIn\" height=\"70\" width=\"150\"></a></nav></center>'''
	newsoup=bs(temp,'lxml')
	tag.insert(0,newsoup)
	return sp
