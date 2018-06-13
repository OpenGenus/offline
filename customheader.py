from bs4 import BeautifulSoup as bs
import lxml
def addheader(sp):
	tag=sp.body
	temp='''<center><br><nav><a href=\"https://discourse.opengenus.org\"><img src="https://discourse.opengenus.org/uploads/opengenus/original/1X/b2f73aeb998e62df86bce346aae9de58784e0fcd.png" alt= \"OpenGenus\" height=\"97\" width=\"78\"></a> | <a href=\"https://discourse.opengenus.org\">Empty Element</a> | <a href=\"https://discourse.opengenus.org\">E E</a> | <a href=\"4.html\">E E</a></nav></center>'''
	newsoup=bs(temp,'lxml')
	tag.insert(0,newsoup)
	return sp
