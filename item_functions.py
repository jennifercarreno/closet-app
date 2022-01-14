from flask import Flask, render_template, redirect, url_for, request
# import app 

global filtered_items
global filtered_outfits
global outfit_items

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
    outfit_items = []
    
    for item in items.find():
        if item['name'] == outfit['item1']:
            outfit['item1'] = item['link']
            outfit_items.append(outfit['item1'])

        if item['name'] == outfit['item2']:
            outfit['item2'] = item['link']
            outfit_items.append(outfit['item2'])


        if item['name'] == outfit['item3']:
            outfit['item3'] = item['link']
            outfit_items.append(outfit['item3'])


        if item['name'] == outfit['item4']:
            outfit['item4'] = item['link']
            outfit_items.append(outfit['item4'])


        if item['name'] == outfit['item5']:
            outfit['item5'] = item['link']
            outfit_items.append(outfit['item5'])

    return outfit_items

def outfit_filter(outfits):
    filtered_outfits = []
    filter = request.form.get('occasion')
    for outfit in outfits.find():
        if outfit.get('occasion') == filter:
            filtered_outfits.append(outfit)
    return filtered_outfits

def outfits_links(outfit):
    outfit_items=[]
    if outfit['item1'] != '':
        outfit_items.append(outfit['item1'])
    if outfit['item2'] != '':
        outfit_items.append(outfit['item2'])
    if outfit['item3'] != '':
        outfit_items.append(outfit['item3'])
    if outfit['item4'] != '':
        outfit_items.append(outfit['item4'])
    if outfit['item5'] != '':
        outfit_items.append(outfit['item5'])
    return outfit_items