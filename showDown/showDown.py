#!/usr/bin/env python
from download import Downloader
import urllib.request as urllib2
import bs4
import os 
import time 
import sys        
temp = -1

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
            self.getVideoLink()
            print ("The file in latest available is : %s"%(self.filename))

            response = input("Do you wanna download it (y or n): ")
            if response=='y' or response=='Y':     
                video = Downloader()
                video.download(url = self.url ,filename = self.filename)

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

    def getVideoLink(self):
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        self.filename = str(elems[-2])
        self.filename = self.filename[self.filename.find(">")+1:]
        self.filename = self.filename[:self.filename.find("<")]
        self.url=elems[-2].get('href')
   
    def listAvailableShows(self):
        res = urllib2.urlopen(urllib2.Request(self.url, headers = self.header)).read()
        soup=bs4.BeautifulSoup(res, "html.parser")
        elems=soup.select('.data a')
        print ('List of TV Shows: \n')
        for i in range(len(elems)):
            show_name = str(elems[i])
            show_name = show_name[show_name.find(">")+1:]
            show_name = show_name[:show_name.find("<")]
            print ("\r " + show_name)
     
            
