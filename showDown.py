import requests,bs4

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
            
url = 'http://tvshows4mobile.com/search/list_all_tv_series'

res = requests.get(url, stream=True, proxies=proxyDict)
soup = bs4.BeautifulSoup(res.text)
elems = soup.select('.data a')

show_name = raw_input()

for i in range(len(elems)):
    if show_name in str(elems[i]).lower():
        temp = i

link = elems[temp].get('href')
            
url = 'http://tvshows4mobile.com/Two-And-A-Half-Men-1/index.html'
url = url[:-10]

res=requests.get(url, stream=True, proxies=proxyDict)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)


elems=soup.select('.data a')
lastseason=elems[0].get('href')

url = lastseason  


res=requests.get(url, stream=True, proxies=proxyDict)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)

elems=soup.select('.data a')
lastepisode=elems[0].get('href')


url = lastepisode

res=requests.get(url, stream=True, proxies=proxyDict)

res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)
elems=soup.select('.data a')
url=elems[-2].get('href')


r = requests.get(url, stream=True, proxies=proxyDict)
#r=requests.get(url)
with open("test.mp4", "wb") as f:
    print('Downloading at Flash Speed..')
    for chunk in r.iter_content(8*1024):
        if chunk:
            f.write(chunk)
            f.flush()