from flask import Flask, render_template, redirect, url_for, request
# import app 

global filtered_items

def filter(items):
    filtered_items = []
    filter_color = request.form.get('color')
    print(filter_color)
    filter_category = request.form.get('category')

    # check to see if a filter has been selected
    if filter_color != '--' or filter_category != '--':
        # if only color filter is selected
        if filter_color != '--' and filter_category == '--':
            for item in items.find():
                item_color = item.get('color')
                print(item_color)
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
                    
    print(filtered_items)
    return filtered_items



def link_converter(outfit, items):
    for item in items.find():
        if item['name'] == outfit['item1']:
            outfit['item1'] = item['link']

        if item['name'] == outfit['item2']:
            outfit['item2'] = item['link']

        if item['name'] == outfit['item3']:
            outfit['item3'] = item['link']

        if item['name'] == outfit['item4']:
            outfit['item4'] = item['link']

        if item['name'] == outfit['item5']:
            outfit['item5'] = item['link']
    return

