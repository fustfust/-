import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

###
##입맛에 맞게 코딩
##
movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title a')
    star = movie.select_one('td.point')
    order = movie.select_one('td.ac img')

    if a_tag is not None:
        title = a_tag.text
        print(order['alt'], title, star.text)


#3333333333333333333333333333333333333333333333333333333333333333333333333333
# import requests # requests 라이브러리 설치 필요

# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
# print(rjson['RealtimeCityAir']['row'][0]['NO2'])

# gus = rjson['RealtimeCityAir']['row']

# #for gu in gus:
# #	print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

# for gu in gus:
# 	if gu['IDEX_MVL'] < 100:
# 		print (gu['MSRSTE_NM'], gu['IDEX_MVL'])
# #222222222222222222222222222222222222222222222222222222222222222
# people = [{'name': 'bob', 'age': 20}, 
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7}]

# def get_age(name):
#     for person in people:
#             if person['name'] == name:
#                 return person['age']
#             else:
#                 return '입력한 이름이 존재하지 않습니다.'
# age = get_age('bo')
# print(age)



# #11111111111111111111111111111111111111111111111111111111111111111111111
# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# count = 0
# def count(fruit_name):
#     count = 0
#     for fruit in fruits:
#         if fruit == fruit_name:
#             count +=1
#     return count

# num = count('수박')
# print(num)