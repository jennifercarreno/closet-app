from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient
# from werkzeug.utils import secure_filename
import os
# import item_functions

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

@app.route('/items')
def items():
    items = db.items
    print(items)
    return render_template('items.html', items = items.find())

# displays items when created
@app.route('/items/submit', methods=['POST', 'GET'])
def items_submit():
    items = db.items
    item = {
        'name': request.form.get('name'),
        # 'item-photo': request.form.get('item-photo'),
        'link': request.form.get('photo-link'), 
        'category': request.form.get('category'),
        'color':request.form.get('color')
    }
    
    items.insert_one(item)
    # print(db.items)
    print(item['name'])
    print(item['link'])
    print(item['category'])
    print(item['color'])
    # item_photo_func = item_functions.get_item_photo(items)
    return render_template('items.html', items=items.find())

# displays a single item
@app.route('/items/<item_id>')
def item_show(item_id):
    items=db.items
    item = items.find_one({'_id': ObjectId(item_id)})
    return render_template('items_show.html', item = item)

# deletes an item
@app.route('/items/<item_id>/delete', methods=['POST'])
def items_delete(item_id):
    items=db.items
    items.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('.items'))

#edit an item
@app.route('/items/<item_id>/edit', methods=['POST'])
def items_edit(item_id):
    items=db.items
    item = items.find_one({'_id': ObjectId(item_id)})
    return render_template('items_edit.html', item=item)

#updates an item
@app.route('/items/<item_id>/update', methods=['POST'])
def items_update(item_id):
    items=db.items
    updated_item = {
       'name': request.form.get('name'),
        # 'item-photo': request.form.get('item-photo'),
        'link': request.form.get('photo-link'), 
        'category': request.form.get('category'),
        'color':request.form.get('color')
    }
    # set the former playlist to the new one we just updated/edited
    items.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': updated_item})

    item=items.find_one({'_id': ObjectId(item_id)})
    print(item['name'])
    # take us back to the playlist's show page
    return redirect(url_for('item_show', item_id=item_id))



# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'

if __name__ == '__main__':
   app.run()
