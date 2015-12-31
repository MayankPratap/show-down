import requests
import bs4

address = "172.31.102.29"
port = "3128"
user = "edcguest"
password = "edcguest"

http_proxy  = "http://" + user + ":" + password + "@" + address + ":" + port
https_proxy = "http://" + user + ":" + password + "@" + address + ":" + port
ftp_proxy   = "http://" + user + ":" + password + "@" + address + ":" + port   
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }
            
            
class showDown:
    
    def __init__(self):
        self.url = 'http://tvshows4mobile.com/search/list_all_tv_series'
        
    def download(self,show_name):
        res = requests.get(self.url, stream=True, proxies=proxyDict)
        soup = bs4.BeautifulSoup(res.text)
        elems = soup.select('.data a')

        for i in range(len(elems)):
            if show_name in str(elems[i]).lower():
                temp = i
        
        self.url = elems[temp].get('href')
        self.url = self.url[:-10]
        
        self.updateSeason()
        self.updateEpisode()
        self.getVideoLink()
        self.downloader()
        
        
    def updateSeason(self):
        res=requests.get(self.url, stream=True, proxies=proxyDict)
        res.raise_for_status()        
        soup=bs4.BeautifulSoup(res.text)
        elems=soup.select('.data a')
        lastseason=elems[0].get('href')        
        self.url = lastseason  


    def updateEpisode(self):
        res=requests.get(self.url, stream=True, proxies=proxyDict)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)
        elems=soup.select('.data a')
        lastepisode=elems[0].get('href')
        self.url = lastepisode

    def getVideoLink(self):
        res=requests.get(self.url, stream=True, proxies=proxyDict)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)
        elems=soup.select('.data a')
        self.url=elems[-2].get('href')


    def downloader(self):
        r = requests.get(self.url, stream=True, proxies=proxyDict)
        with open("test.mp4", "wb") as f:
            print('Downloading at Flash Speed..')
            for chunk in r.iter_content(8*1024):
                if chunk:
                    f.write(chunk)
                    f.flush()