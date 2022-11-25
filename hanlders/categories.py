import json


def get_category_list(data):
    with open('../data/catalog.json', 'r', encoding='utf-8') as file:
        list = json.load(file)
        code = 200
        kk =""
    for i in list:
        kk += f" {i['id']}.{i['name']}"
    return {
        "code": code,
        "data": kk
    }
