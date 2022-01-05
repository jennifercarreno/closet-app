from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

host = os.environ.get('DB_URL')
client = MongoClient(host=host)
db = client.closet
items = db.items
app = Flask(__name__)


# home page
@app.route('/')
def index():
   return render_template('home.html')

#prompts to create a new item 
@app.route('/item/new')
def item_new():
    return render_template('item_new.html', items=items.find())

# displays items
@app.route('/items', methods=['POST'])
def items_submit():
    item = {
        'name': request.form.get('name'),
        'item-photo': request.form.get('item-photo'),
        'item-photo-link': request.form.get('item-photo-link')
    }
    items.insert_one(item)
    print(db.items)
    return render_template('items.html')

if __name__ == '__main__':
   app.run()
