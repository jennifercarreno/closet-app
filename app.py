from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import item_functions

host = os.environ.get('DB_URL')
client = MongoClient(host=host)
db = client.closet
items = db.items
app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'

# home page
@app.route('/')
def index():
   return render_template('home.html')

#prompts to create a new item 
@app.route('/item/new')
def item_new():
    return render_template('item_new.html')

# displays items
@app.route('/items', methods=['POST'])
def items_submit():
    item = {
        'name': request.form.get('name'),
        'item-photo': request.form.get('item-photo'),
        'link': request.form.get('photo-link')
    }
    items.insert_one(item)
    # print(db.items)
    print(item['name'])
    print(item['link'])
    # item_photo_func = item_functions.get_item_photo(items)
    return render_template('items.html', items=items.find())

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run()
