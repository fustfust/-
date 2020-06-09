from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분 (HOME)
@app.route('/')
def home():
    return render_template('index.html')

## SAVE shopping list
@app.route('/shoppings', methods=['POST'])
def write_shopping():
    #사용자에게 입력 받은 값
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    
    shopping = {
        'name' : name_receive,
        'quantity' : quantity_receive,
        'address' : address_receive,
        'phone' : phone_receive
    }
    db.shoppings.insert_one(shopping)

    return jsonify({'result':"success",'msg':'주문이 성공적으로 저장되었습니다.'})

    

#FIND
@app.route('/shoppings', methods=['GET'])
def read_shopping():
    shoppings = list(db.shoppings.find({}, {'_id':0}))

    return jsonify({'result':"success",'shoppings':shoppings})
    


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)