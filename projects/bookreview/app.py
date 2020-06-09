from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

##home
@app.route('/')
def home():
    return render_template('index.html')

##save reviews
@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    review = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive
    }

    db.reviews.insert_one(review)

    return jsonify({'result':"success",'msg':'리뷰가 성공적으로 저장되었습니다'})

##get reviews
@app.route('/reviews', methods=['GET'])
def read_review():
    reviews = list(db.reviews.find({}, {'_id':0}))

    return jsonify({'result':"success",'reviews':reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)