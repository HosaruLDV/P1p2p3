import json


def get_catalog() -> list:
    """
    Функция обрабатывает json-файл и возвращает его содержимое.
    :return: list
    """
    with open('data/catalog.json', 'r', encoding='utf-8') as file:
        catalog = json.load(file)
    return catalog


def choose_product(data: dict) -> tuple:
    """
    Функция позволяет найти запрошенный товар в каталоге.
    Возвращает содержимое каталога и информацию о выбранном товаре.
    :param data: dict
    :return: tuple
    """
    catalog_info = get_catalog()
    chosen_product = None
    for cat in catalog_info:
        for product in cat['products']:
            if product['id'] == data['data']['id']:
                chosen_product = product
    return catalog_info, chosen_product


def delete_products(catalog: list, product: dict, num: int) -> None:
    """
    Функция уменьшает количество выбранного товара в каталоге.
    :param catalog: list
    :param product: dict
    :param num: int
    :return: None
    """
    product['balance'] -= num

    with open('data/catalog.json', 'w', encoding='utf-8') as file:
        json.dump(catalog, file, ensure_ascii=False)


def put_product_to_cart(data: dict) -> dict:
    """
    Функция добавляет выбранный товар в корзину, возвращает сообщение об
    успешном результате с кодом 201 и информацией о добавленном товаре.

    Если такого товара нет, функция возвращает сообщение об ошибке с кодом 404.

    Если нет необходимого количества выбранного товара, функция возвращает
    сообщение об ошибке с кодом 409.
    :param data: dict
    :return: dict
    """
    catalog_info, chosen_product = choose_product(data)
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
            delete_products(catalog_info, chosen_product, product_num)

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
