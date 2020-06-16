from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
clinet = MongoClinet('localhost', 27017)
db = client.dbsparta

##HTML을 주는 부분 
@app.route('/')
def home():
    return render_template('index.html')

