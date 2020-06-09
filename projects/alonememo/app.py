from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

##home
@app.route('/')
def home():
    return render_template('index.html')

## Save
@app.route('/memo', methods=['POST'])
def save():

    #사용자에게 입력 받은 값
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    #url에 해당하는 html 가져오기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    #가져온 html parsing 하기
    soup = BeautifulSoup(data.text, 'html.parser')

    #parsing 한 html에서 og tag를 추출하여 변수 설정
    og_title = soup.select_one('meta[property="og:title"]')
    og_image = soup.select_one('meta[property="og:image"]')
    og_description = soup.select_one('meta[property="og:description"]')

    #추출한 og tag의 content를 조회
    url_title = og_title['content']
    url_image = og_image['content']
    url_description = og_description['content']

    #sparta DB에 저장하기 위한 data 생성
    article = {
        'url' : url_receive,
        'title' : url_title,
        'image' : url_image,
        'desc' : url_description,
        'comment' : comment_receive
    }
    #DB에 data 저장
    db.articles.insert_one(article)

    #저장성공결과 반환
    return jsonify({'result':'success', 'msg':'등록성공 했습니다.'})


#Find
@app.route('/memo', methods=['GET'])
def find():
    #DB에 저장된 값을 조회함.
    articles = list(db.articles.find({}, {'_id':0}))
    #조회한 값을 client에 반환함.
    return jsonify({'result':'success', 'articles':articles})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
