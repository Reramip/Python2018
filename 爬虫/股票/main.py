import requests
import traceback
import time
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        kv={"user-agent":"Google Chrome 67.0.3396.62"}
        r=requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.text
    except:
        return "error"

def getStockInfo(stockurl,fpath,slist):
    f=open(fpath,"a",encoding="utf-8")
    for stock in slist:
        url=stockurl+stock+".html"
        html=getHTMLText(url)
        try:
            if html=="":
                continue
            infoList=[]
            soup=BeautifulSoup(html,"lxml")
            stockNum=soup.find("a",attrs={"class":"bets-name"})
            snum=stockNum.find_all("span")
            stockPrice=soup.find("strong",attrs={"class":"_close"})
            stockInfo=soup.find("div",attrs={"class":"bets-content"})
            infoList=stockInfo.find_all("dd")
            f.writelines(str(snum)+str(stockPrice)+str(infoList)+'\n')

        except:
            traceback.print_exc()
            continue
    f.close()

def main():
    outpath=time.strftime("%y%m%d%H", time.localtime())
    infourl="https://gupiao.baidu.com/stock/"
    output=outpath+".txt"
    f=open("Nums.txt","r",encoding="utf-8")
    string=f.read()
    slist=string.split(',')
    f.close()
    getStockInfo(infourl,output,slist)

main()