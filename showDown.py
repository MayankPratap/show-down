#!/usr/bin/python
import bs4
import os , time ,sys        
temp = -1        

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2   

class showDown:
   
    def __init__(self):
        self.url = 'http://tvshows4mobile.com/search/list_all_tv_series'
        self.header = { 'USER_AGENT' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        self.proxy_file = open("proxy.config","r")
        self.http_proxy = self.proxy_file.read()
        self.proxyDict = { 
              "http"  : self.http_proxy
            }
        self.proxy_file.close()
    
    def setproxy(self,proxy) :
        self.proxy_file = open("proxy.config","w")
        self.proxy_file.write(proxy)
        print ("Proxy updated")
        self.proxy_file.close()
        
    def unsetproxy(self) :
        self.proxy_file = open("proxy.config","w")
        self.proxy_file.write("")
        print ("Proxy removed")
        self.proxy_file.close()
        
    def downloadLatest(self,show_name):
        print ('Sending request ... ')
        if self.http_proxy != '':
            proxy = urllib2.ProxyHandler(self.proxyDict)
            auth = urllib2.HTTPBasicAuthHandler()
            opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup = bs4.BeautifulSoup(res, "html.parser")
        elems = soup.select('.data a')
        for i in range(len(elems)):
            if show_name.lower() in str(elems[i]).lower():
               global temp              
               temp = i
        if temp != -1 :
            self.url = elems[temp].get('href')
            self.url = self.url[:-10]
            self.currentSeason()
            self.latestEpisode()
            self.getVideoLinkmp4()
            print ("The file in latest available is : %s"%(self.filename))
            response = input("Do you wanna download it (y or n): ")
            if response=='y' or response=='Y':     
               self.downloader(url = self.url , filename = self.filename )
            else :
                if sys.platform!='win32':
                    os.system("setterm -cursor on")
                return
            temp = -1
        else :
            print ('Sorry , no match found . ')
    def currentSeason(self):
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()       
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        lastseason=elems[0].get('href')        
        self.url = lastseason  


    def latestEpisode(self):
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        lastepisode=elems[0].get('href')
        self.url = lastepisode

    def getVideoLinkmp4(self):
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        self.filename = str(elems[-2])
        self.filename = self.filename[self.filename.find(">")+1:]
        self.filename = self.filename[:self.filename.find("<")]
        self.url=elems[-2].get('href')

    def downloader(self,url,filename):
     try:
        r = urllib2.urlopen(urllib2.Request(self.url, headers = self.header))
        print ('\rSend Get ... ')
        time.sleep(1)
        print ('\rDownload started .... ')
        time.sleep(1)
        content_length = r.headers['content-length']
        print ('Filename : %s '%(filename))
        print ('Filesize : %.2f MB'%(float(content_length)/(1024*1024)))
        downloaded = 0
        f = open(filename, "wb")
        data=r.read(10240)
        cur_speed = 0
        session_data=0
        start_time = lasttime = time.time()
        if sys.platform!='win32':
            os.system('setterm -cursor off')
        while data :
            f.write(data)
            session_data += len(data)
            if int(time.time()-lasttime) == 1:
                cur_speed = (session_data/1000)/(time.time()-lasttime)
                lasttime = time.time()
                session_data = 0
            downloaded += len(data)
            sys.stdout.write('\rDownloaded : %.2f %%                              Downloading @ %.2f kBps  '%(float(downloaded*100)/float(content_length),cur_speed))
            sys.stdout.flush()
            data=r.read(10240)
        f.close()
        if sys.platform!='win32':
            os.system('setterm -cursor on')
        sys.stdout.write("\n"+filename + " downloaded successfully !!!\n%.2f MB downloaded in %.2f s ."%(float(content_length)/(1024*1024),time.time() - start_time))
     except KeyboardInterrupt :
        if sys.platform!='win32':
            os.system('setterm -cursor on')
        print ('you pressed Ctrl + C')
        if os.path.isfile("./"+filename):
            r.close()
            f.close()
            os.remove("./"+filename)
            
    def showSeason(self , url):
        res = urllib2.urlopen(urllib2.Request(url, headers = self.header)).read()       
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        for season in elems : 
            season_name = str(season.get('href'))
        season_name = season_name[season_name.find(">")+1:]
        season_name = season_name[:season_name.find("<")]
        print (season_name+"\n")  


    def showEpisode(self , url , page):
        res = urllib2.urlopen(urllib2.Request(url+"page"+page+".html", headers = self.header)).read()
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        for episode in elems : 
            episode_name = str(episode.get('href'))
        episode_name = episode_name[episode_name.find(">")+1:]
        episode_name = episode_name[:episode_name.find("<")]
        print (episode_name+"\n")
