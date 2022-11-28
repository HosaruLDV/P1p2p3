import json


## Добавил путь к файлу корзины
cart = 'data/cart.json'

def get_catalog():
    with open('data/catalog.json', 'r', encoding='utf-8') as file:
        catalog = json.load(file)
    return catalog

def get_cart(*args, **qwargs):
    ## Достаем корзину из файла
    try:
        with open(cart, 'r', encoding='utf-8') as file:
            cart_re = json.load(file)
    ## Файл не нашли - возвращаем пустой список
    except:
        cart_re = []
    return cart_re

def is_cart_exist(*args, **qwargs):
    try:
        with open(cart, 'r', encoding='utf-8') as file:
            cart_re = json.load(file)
    ## Файл не нашли (или криво читается) - создаем новый файл корзины
    except:
        with open(cart, 'w', encoding='utf-8') as file:
            json.dump([], file)



def delete_products(pr_id, num):
    catalog_info = get_catalog()
    for cat in catalog_info:
        for product in cat['products']:
            if product['id'] == pr_id:
                product['balance'] -= num

    with open('data/catalog.json', 'w', encoding='utf-8') as file:
        json.dump(catalog_info, file, ensure_ascii=False)

def put_product_to_cart(data):

    ## В коде не увидел проверку наличия корзины. Добавил.
    is_cart_exist()

    catalog_info = get_catalog()
    chosen_product = None
    for cat in catalog_info:
        for product in cat['products']:
            if product['id'] == data['filter']['id']:
                chosen_product = product
    if not chosen_product:
        return {
            "code": 404,
            "message": "Товара с таким номер не найдено."
        }

    else:
        product_id = chosen_product['id']
        product_name = chosen_product['name']
        product_price = str(chosen_product['price']) + 'руб./' + chosen_product['unit']
        product_unit = chosen_product['unit']
        product_num = data['filter']['count']

        if chosen_product['balance'] < product_num:
            return {
                "code": 409,
                "message": f"Невозможно добавить товар {product_name} в количестве {product_num} {product_unit} в корзину, потому что их осталось всего {chosen_product['balance']}."
            }

        else:
            delete_products(product_id, product_num)

            to_add = [{
                'product_id': product_id,
                'product_name': product_name,
                'product_price': product_price,
                'product_num': product_num,
                'product_unit': product_unit
            }]
            cart_list = []
            with open(cart, 'r', encoding='utf-8') as file:
                try:
                    cart_info = json.load(file)
                    for product_in_cart in cart_info:
                        cart_list.append(product_in_cart)
                    cart_list.append(to_add[0])
                    with open(cart, 'w', encoding='utf-8') as file:
                        json.dump(cart_list, file, ensure_ascii=False)
                except ValueError:
                    with open(cart, 'a', encoding='utf-8') as file:
                        json.dump(to_add, file, ensure_ascii=False)

            return {
                "code": 201,
                "message": f"Товар {product_name} в количестве {product_num} {product_unit} добавлен в корзину успешно"
            }

def get_cart(*args, **qwargs):
    cart_read = get_cart()
    message_re = {
        "code": 200,
        "message": []
    }
    if not cart_read:
        message_re["message"] = "Корзина пуста\nВоспользуйтесь поиском, чтобы найти всё что нужно."
    else:
        j = 1
        for i in cart_read:
            message_re["message"].append(str(j) + ". " + i["product_name"] + " (" + i["product_price"] + ") " + "добавлено " + str(i["product_num"] + " " + i["product_unit"])                                                                                                                             ]))
            j += 1
        message_re["message"].split("\n")

    return message_re
