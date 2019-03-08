import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		kv={"user-agent":"Google Chrome 67.0.3396.62"}
		r=requests.get(url, headers=kv, timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "error"

def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	for tr in soup.find("tbody").children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr("td")
			ulist.append([tds[0].string,tds[1].string])
	
def printUnivList(ulist,num):
	tplt="{0:^10}\t\t{1:{2}^10}"
	print(tplt.format("排名","学校",chr(12288)))
	for i in range(num):
		u=ulist[i]
		try:
			print(tplt.format(u[0],u[1],chr(12288)))
		except:
			pass

def main():
	uinfo=[]
	url="https://www.dxsbb.com/news/5463.html"
	html=getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,50)

main()