#멜론 Top50 차트 크롤링

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

########################################    
#######R E S U L T: 2019-Feb-18#########  
########################################
# 1 . 멍청이(twit) - 화사(Hwa Sa)
# 2 . 이 노래가 클럽에서 나온다면 - 우디 (Woody)
# 3 . 달라달라 - ITZY (있지)
# 4 . 넘쳐흘러 - 엠씨더맥스
# 5 . 신청곡 (Feat. SUGA of BTS) - 이소라
# 6 . 벌써 12시 - 청하
# 7 . 띵 (Prod. By 기리보이) - Jvcki Wai
# 8 . 초록빛 - 영비
# 9 . 너도 그냥 날 놓아주면 돼 - Osshun Gum
# 10 . 신용재 - 한요한
# 11 . 180도 - 폴킴
# 12 . 너를 만나 - 윤건
# 13 . 모든 날, 모든 순간 (Every day, Every Moment) - 하은 (라코스테남)
# 14 . SOLO - 벤
# 15 . 오랜만이야 (Feat. Zion.T) - 폴킴
# 16 . 아낙네 - 폴킴
# 17 . 그때가 좋았어 - 제니 (JENNIE)
# 18 . 내 생에 아름다운 - 로꼬
# 19 . MILLIONS - MINO (송민호)
# 20 . YES or YES - 케이시 (Kassy)
# 21 . Love Shot - 케이윌
# 22 . Home - WINNER
# 23 . IDOL - TWICE (트와이스)
# 24 . Way Back Home - EXO
# 25 . 이별하러 가는 길 - 세븐틴
# 26 . thank u, next - 방탄소년단
# 27 . Tempo - 숀 (SHAUN)
# 28 . 흔한 이별 - 임한별
# 29 . 삐삐 - Ariana Grande
# 30 . 가을 타나 봐 - EXO
# 31 . 해야 (Sunrise) - 허각
# 32 . 7 rings - 아이유
# 33 . 고백 - 바이브
# 34 . 사계 (하루살이) - 여자친구 (GFRIEND)
# 35 . 봄날 - Ariana Grande
# 36 . 열애중 - 양다일
# 37 . 아름답고도 아프구나 - 엠씨더맥스
# 38 . FAKE LOVE - 방탄소년단
# 39 . 하루도 그대를 사랑하지 않은 적이 없었다 - 벤
# 40 . 그대만 떠올라 - 비투비
# 41 . 오롯이 - 방탄소년단
# 42 . 너는 어땠을까 - 임창정
# 43 . 지나오다 - 로이킴
# 44 . Good Day (Feat. 팔로알토) (Prod. 코드 쿤스트) - 헤이즈 (Heize)
# 45 . 첫눈에 - 노을
# 46 . We all lie - 닐로 (Nilo)
# 47 . %%(응응) - pH-1
# 48 . 봄바람 - Kid Milli
# 49 . 알았다면 - 루피(Loopy)
# 50 . 뚜두뚜두 (DDU-DU DDU-DU) - 헤이즈 (Heize)
#################################
