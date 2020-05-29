import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dbsparta


#지니 음악 list 가져오기

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')
#classToIgnore=["rank", "rank-up"]
#soup.find_all('div', class_=lambda x: x not in classToIgnore)

# select를 이용해서, tr들을 불러오기
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr' )
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(3) > td.info


# music (tr들) 의 반복문을 돌리기
#count = 1
for music in musics:
    # music 안에 a
    rank_total = music.select_one('td.number').text
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    title_get = music.select_one('a.title.ellipsis').text
    title = title_get.strip()                                   # a 태그 사이의 텍스트를 가져오기
    singer = music.select_one('a.artist.ellipsis').text                # td 태그 사이의 텍스트를 가져오기
    rank = list(rank_total.split())

    #print(rank[0])
    print(rank[0], title, singer)
    #count +=1
        
