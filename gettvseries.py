import requests
import bs4

url = 'http://tvshows4mobile.com/search/list_all_tv_series'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text)
elems = soup.select('.data a')



for i in range(len(elems)):
    if "diaries" in str(elems[i]).lower():
        temp = i

link = elems[temp].get('href')

