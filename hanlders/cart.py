import json


def get_catalog():
    with open('data/catalog.json', 'r', encoding='utf-8') as file:
        catalog = json.load(file)
    return catalog


def delete_products(pr_id, num):
    catalog_info = get_catalog()
    for cat in catalog_info:
        for product in cat['products']:
            if product['id'] == pr_id:
                product['balance'] -= num

    with open('data/catalog.json', 'w', encoding='utf-8') as file:
        json.dump(catalog_info, file, ensure_ascii=False)


def put_product_to_cart(data):
    print(data)
    catalog_info = get_catalog()
    chosen_product = None
    for cat in catalog_info:
        for product in cat['products']:
            if product['id'] == data['data']['id']:
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
        product_num = data['data']['count']

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
            with open('data/cart.json', 'r', encoding='utf-8') as file:
                try:
                    cart_info = json.load(file)
                    if_add_item = True
                    for product_in_cart in cart_info:
                        if product_in_cart['product_id'] == to_add[0]['product_id']:
                            product_in_cart['product_num'] += to_add[0]['product_num']
                            if_add_item = False
                        cart_list.append(product_in_cart)

                    if if_add_item:
                        cart_list.append(to_add[0])

                    with open('data/cart.json', 'w', encoding='utf-8') as file:
                        json.dump(cart_list, file, ensure_ascii=False)
                except ValueError:
                    with open('data/cart.json', 'a', encoding='utf-8') as file:
                        json.dump(to_add, file, ensure_ascii=False)

            return {
                "code": 201,
                "message": f"Товар {product_name} в количестве {product_num} {product_unit} добавлен в корзину успешно"
            }


def get_cart(data):
    pass
