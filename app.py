from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from item_functions import filter

host = os.environ.get('DB_URL')
client = MongoClient(host=host)
db = client.closet
items = db.items
wishlistItems = db.wishlistItems
app = Flask(__name__)

# home page
@app.route('/')
def index():
   return render_template('home.html')

# start of ITEMS

#prompts to create a new item 
@app.route('/item/new')
def item_new():
    return render_template('items/item_new.html')

@app.route('/items')
def items():
    items = db.items
    print(items)
    return render_template('items/items.html', items = items.find())

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
    return render_template('items/items.html', items=items.find())

# displays a single item
@app.route('/items/<item_id>')
def item_show(item_id):
    items=db.items
    item = items.find_one({'_id': ObjectId(item_id)})
    return render_template('items/items_show.html', item = item)

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
    return render_template('items/items_edit.html', item=item)

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
    items.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': updated_item})

    item=items.find_one({'_id': ObjectId(item_id)})
    print(item['name'])
    return redirect(url_for('items/item_show', item_id=item_id))

@app.route('/items/filter', methods=['POST'])
def items_filter():
    items = db.items
    filtered_items = filter(items)
    return render_template('items/items.html', items=filtered_items)

# start of WISHLIST

# wishlist page
@app.route('/wishlist')
def wishlist_home():
    return render_template('wishlist/wishlist-home.html', items=wishlistItems.find())

# new item to wishlist
@app.route('/wishlist/new')
def wishlist_new():
    return render_template('wishlist/wishlist-new.html')

# creates a wishlist item
@app.route('/wishlist/submit', methods=['POST'])
def wishlist_submit():
    wishlistItem = {
        'name': request.form.get('name'),
        'link': request.form.get('photo-link'),
        'color': request.form.get('color'),
        'category': request.form.get('category')
    }
    wishlistItems.insert_one(wishlistItem)
    return render_template('wishlist/wishlist-home.html', items=wishlistItems.find())

# shows a single item in wishlist
@app.route('/wishlist/<item_id>')
def wishlist_show(item_id):
    wishlistItem = wishlistItems.find_one({'_id': ObjectId(item_id)})
    return render_template('wishlist/wishlist-show.html', wishlistItem=wishlistItem)

# deletes an item in wishlist
@app.route('/wishlist/<wishlistItem_id>/delete', methods=['POST'])
def wishlist_delete(wishlistItem_id):
    wishlistItems.delete_one({'_id': ObjectId(wishlistItem_id)})
    return redirect(url_for('.wishlist_home'))

# edit an item in wishlist
@app.route('/wishlist/<wishlistItem_id>/edit', methods=['POST'])
def wishlist_edit(wishlistItem_id):
    wishlistItem=wishlistItems.find_one({'_id': ObjectId(wishlistItem_id)})
    return render_template('wishlist/wishlist-edit.html',wishlistItem=wishlistItem)

#updates an item in wishlist
@app.route('/wishlist/<wishlistItem_id>/update', methods=['POST'])
def wishlist_update(wishlistItem_id):
    updated_item = {
       'name': request.form.get('name'),
        'link': request.form.get('photo-link'), 
        'category': request.form.get('category'),
        'color':request.form.get('color')
    }
    wishlistItems.update_one(
        {'_id': ObjectId(wishlistItem_id)},
        {'$set': updated_item})

    wishlistItem=wishlistItems.find_one({'_id': ObjectId(wishlistItem_id)})
    return redirect(url_for('.wishlist_show', item_id=wishlistItem_id))

# filters for wishlist
@app.route('/wishlist/filter', methods=['POST'])
def wishlist_filter():
    # wishlistItems = db.wishlistitems
    filtered_items = filter(wishlistItems)
    return render_template('wishlist/wishlist-home.html', items=filtered_items)

# start of OUTFITS
@app.route('/outfits')
def outfits_home():
    return render_template('outfits/outfits_home.html')

# creates a new outfit
@app.route('/outfits/new')
def outfits_new():
    items=db.items
    return render_template('outfits/outfits_new.html', items=items.find())

if __name__ == '__main__':
   app.run()
