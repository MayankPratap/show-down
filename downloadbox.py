import requests
import os

""" address = "172.31.100.30"
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


"""

print('Downloading at Flash Speed')
url = "http://download1.tvshows4mobile.com/Sherlock/Season%2001/Sherlock%20-%20S01E01%20-%201%20(O2TvSeries.Com).mp4"
#r = requests.get(url, stream=True, proxies=proxyDict)
r=requests.get(url)
with open("test.mp4", "wb") as f:
    for chunk in r.iter_content(8*1024):
        if chunk:
            f.write(chunk)
            f.flush()


