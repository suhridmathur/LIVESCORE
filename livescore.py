from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
while 1:
    #html = urlopen("http://cricket.yahoo.com/cricket-live-score-bangladesh-vs-india_194256#fullScorecard")
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    Score=bsObj.find("span",{"class":"scr"}).get_text()
    Overs=bsObj.find("div",{"class":"ings-overs"}).get_text()
    a=bsObj.findAll("div",{"class":"right current"})
    b=bsObj.findAll("div",{"class":"right"})
    print("Score:"+str(Score))
    print("Overs:"+str(Overs))
    print(a[0].get_text())
    print(a[1].get_text())
    print(b[0].get_text())
    print(b[1].get_text())
    print("-----------------------------")
    time.sleep(5)   
