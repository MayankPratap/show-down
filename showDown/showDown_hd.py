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

