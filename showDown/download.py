import sys  
import os
import urllib.request as urllib2
import time

class Downloader(object):

    def __init__(self):
        None
        
    def download(self,url,filename):
     try:
        self.url = url
        self.header = { 'USER_AGENT' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        self.proxy_file = open("proxy.config","r")
        self.http_proxy = self.proxy_file.read()
        self.proxyDict = { 
              "http"  : self.http_proxy
        }
        self.proxy_file.close()
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
        print ('  Ctrl + C pressed')
        if os.path.isfile("./"+filename):
            r.close()
            f.close()
            os.remove("./"+filename) 
