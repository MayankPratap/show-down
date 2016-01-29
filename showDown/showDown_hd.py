#!/usr/bin/python
import bs4
import os
import time 
import sys
import webbrowser
import urllib.request as urllib2

class showDown_hd:
   
    def __init__(self):
        self.url = 'http://dayt.se/tvseries/index.php?&page='
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        self.proxy_file = open("proxy.config","r")
        self.http_proxy = self.proxy_file.read()
        self.proxyDict = { 
              "http"  : self.http_proxy
            }
        self.proxy_file.close()
    
    def downloadLatest(self,show_name):
        print ('Sending request ... ')
        if self.http_proxy != '':
            proxy = urllib2.ProxyHandler(self.proxyDict)
            auth = urllib2.HTTPBasicAuthHandler()
            opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
        page_num=1
        while True:
            try:
                if page_num>3:
                    raise ValueError("Sorry, no match found...")
                found=False
                res = urllib2.urlopen(urllib2.Request(self.url+str(page_num), headers = self.header)).read()
                soup = bs4.BeautifulSoup(res, "html.parser")
                elems = soup.select('p[align="center"]')
                for i in range(len(elems)):
                    if elems[i].getText().lower()==show_name.lower():
                        global show_num
                        show_num=i
                        found=True
                        break
                if found:
                    break
                else:
                    page_num+=1
            except ValueError as e:
                print(e)
                exit()
        res = urllib2.urlopen(urllib2.Request(self.url+str(page_num), headers = self.header)).read()
        soup = bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.topic_head a')
        self.url="http://dayt.se/tvseries/"+elems[show_num].get('href')
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup = bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.title')
        print("Enter choice:")
        for i in range(len(elems)):
            print(str(i+1)+".  "+str(elems[i].getText()))
        choice=int(input())
        self.url="http://dayt.se/forum/"+elems[choice-1].get('href')
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup = bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('#dm1')
        self.url=elems[0].get('href')
        webbrowser.open(self.url)
##    def downloader(self,url,filename):
##     try:
##        r = urllib2.urlopen(urllib2.Request(self.url, headers = self.header))
##        print ('\rSend Get ... ')
##        time.sleep(1)
##        print ('\rDownload started .... ')
##        time.sleep(1)
##        content_length = r.headers['content-length']
##        print ('Filename : %s '%(filename))
##        print ('Filesize : %.2f MB'%(float(content_length)/(1024*1024)))
##        downloaded = 0
##        f = open(filename, "wb")
##        data=r.read(10240)
##        cur_speed = 0
##        session_data=0
##        start_time = lasttime = time.time()
##        if sys.platform!='win32':
##            os.system('setterm -cursor off')
##        while data :
##            f.write(data)
##            session_data += len(data)
##            if int(time.time()-lasttime) == 1:
##                cur_speed = (session_data/1000)/(time.time()-lasttime)
##                lasttime = time.time()
##                session_data = 0
##            downloaded += len(data)
##            sys.stdout.write('\rDownloaded : %.2f %%                              Downloading @ %.2f kBps  '%(float(downloaded*100)/float(content_length),cur_speed))
##            sys.stdout.flush()
##            data=r.read(10240)
##        f.close()
##        if sys.platform!='win32':
##            os.system('setterm -cursor on')
##        sys.stdout.write("\n"+filename + " downloaded successfully !!!\n%.2f MB downloaded in %.2f s ."%(float(content_length)/(1024*1024),time.time() - start_time))
##     except KeyboardInterrupt :
##        if sys.platform!='win32':
##            os.system('setterm -cursor on')
##        print ('you pressed Ctrl + C')
##        if os.path.isfile("./"+filename):
##            r.close()
##            f.close()
##            os.remove("./"+filename)
