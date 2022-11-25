def get_product_list(data):
    import json
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
                case {'action': _, 'filter': {'price': [_], 'category': cat}}:
                    if cat in [None, int]:
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


print(get_product_list([{"price": ['>=100']}, {"category": None}]))
