#멜론 Top100 차트 크롤링

import requests
from bs4 import BeautifulSoup

#헤더 생성
request_headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    "Referer":'Referer: https://www.melon.com/chart/index.htm'
}
url = "https://www.melon.com/chart/index.htm"
html = requests.get(url, headers=request_headers).text

soup = BeautifulSoup(html, "html.parser")
title = "#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a"
singer = "#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a"
title_List = soup.select(title)
singer_List = soup.select(singer)

x=0
for title,singer in zip(title_List,singer_List):
    x += 1
    print(x, ".", title.text, "-", singer.text)

  
