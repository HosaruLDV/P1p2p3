import json


def get_product_list(data):
    code = 200
    products = ''

    try:
        with open('../data/catalog.json', 'r', encoding='utf8') as file:
            json_file = json.loads(file.read())
            price = data['filter']['price'][0]
            category = data['filter']['category']

            # Code 400
            good = False
            match data:
                case {'action': _, 'filter': {'price': [_], 'category': [*ec]}}:
                    print(ec)
                    if all([T in [None, int] for T in ec]):
                        good = True
            if not good:
                code = 400
                return {'code': code, 'data': products}
            # Main
            for j in json_file:
                for prd in j['products']:

                    # Check price and category
                    if eval(f'{prd["price"]} {price}') and prd['price']:
                        products += f'{prd["id"]}. {prd["name"]} ({prd["price"]} руб/{prd["unit"]}) {prd["balance"]}шт.\n'

    except:
        code = 500
    finally:
        return {'code': code, 'data': products}





<<<<<<< HEAD
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
=======
>>>>>>> gtl
