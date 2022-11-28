import json


def get_product_list(data):
    pass


def get_single_product(data):
    with open("../data/catalog.json", encoding='utf-8') as catalog:
        catalog_data = json.load(catalog)

    user_product_id = data["data"]['id']
    code = 404
    message = "Товара с таким номером не найдено"
    for i in catalog_data:
        for product in i['products']:
            if user_product_id == product['id']:
                code = 200
                message = f"{product['name']}\nЦена: {product['price']} рублей за {product['unit']}\nОстаток на складе: {product['balance']} {product['unit']}\nОписание: {product['description']}"

    return {
        "code": code,
        "message": message}
