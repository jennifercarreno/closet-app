from flask import Flask, render_template, redirect, url_for, request
# import app 

global filtered_items

def filter(items):
    filtered_items = []
    filter_color = request.form.get('color')
    print(filter_color)
    # filter_category = request.form.get('category')

    for item in items.find():
        item_color = item.get('color')
        if item_color == filter_color:
            filtered_items.append(item)
            print(filtered_items)
    return filtered_items

