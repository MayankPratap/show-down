import requests,bs4

url='http://tvshows4mobile.com/limitless/'
res=requests.get(url)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)


elems=soup.select('.row .value')
lastseason=elems[5].getText()


if int(lastseason)<10:
    season='0'+lastseason
else:
    season=lastseason

url='http://tvshows4mobile.com/limitless/Season-'+lastseason   

    
res=requests.get(url)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)

elems=soup.select('.row .value')
lastepisode=elems[1].getText()

if int(lastepisode)<10:
    episode='0'+lastepisode
else:
    episode=lastepisode



url='http://tvshows4mobile.com/Sherlock/Season-'+season+'/Episode-'+episode+'/index.html'
res=requests.get(url)

res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)
elems=soup.select('.data a')
print(elems)
temp=elems[-2].get('href')
print(temp)
