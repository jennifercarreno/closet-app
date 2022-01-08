from flask import Flask, render_template, redirect, url_for, request
# import app 

global filtered_items

def filter(items):
    filtered_items = []
    filter_color = request.form.get('color')
    print(filter_color)
    filter_category = request.form.get('category')

    # check to see if a filter has been selected
    if filter_color != '--' and filter_category != '--':
        # if only color filter is selected
        if filter_color != '--' and filter_category == '--':
            for item in items.find():
                item_color = item.get('color')
                if item_color == filter_color:
                    filtered_items.append(item)
        # if only category filter is selected
        if filter_color == '--' and filter_category != '--':
            for item in items.find():
                item_category = item.get('category')
                if item_category == filter_category:
                    filtered_items.append(item)

        if filter_color != '--' and filter_category != '--':
            for item in items.find():
                item_category = item.get('category')
                item_color = item.get('color')
                if item_category == filter_category and item_color == filter_color:
                    filtered_items.append(item)

    return filtered_items

