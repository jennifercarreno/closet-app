from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

host = os.environ.get('DB_URL')
client = MongoClient(host=host)
db = client.closet
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

if __name__ == '__main__':
   app.run()
