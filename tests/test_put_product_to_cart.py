from hanlders.cart import put_product_to_cart, get_catalog
from main import main

put_product_to_cart_expected_result = {
    "code": 201,
    "message": f"Товар Яблоки. Голден. в количестве 5 кг добавлен в корзину "
               f"успешно"
}
put_product_to_cart_expected_result_no_product = {
    "code": 404,
    "message": "Товара с таким номер не найдено."
}
put_product_to_cart_expected_result_not_enough = {
    "code": 409,
    "message": f"Невозможно добавить товар Яблоки. Голден. в количестве 1000000 кг в корзину, потому что их осталось всего"
}

expected_result_getter = 'Фрукты'


def test_put_product_to_cart_func():
    result = put_product_to_cart({"action": 5, "data": {"id": 1, "count": 5}})
    result_no_product = put_product_to_cart({"action": 5, "data": {"id": 1000000, "count": 5}})
    result_not_enough = put_product_to_cart({"action": 5, "data": {"id": 1, "count": 1000000}})

    assert result.get('code') == put_product_to_cart_expected_result.get('code')
    assert result.get('message') == put_product_to_cart_expected_result.get('message')

    assert result_no_product.get('code') == put_product_to_cart_expected_result_no_product.get('code')
    assert result_no_product.get('message') == put_product_to_cart_expected_result_no_product.get('message')

    assert result_not_enough.get('code') == put_product_to_cart_expected_result_not_enough.get('code')
    assert put_product_to_cart_expected_result_not_enough.get('message') in result_not_enough.get('message')


def test_put_product_to_cart_main():
    result = main({"action": 5, "data": {"id": 1, "count": 5}})

    assert result.get('code') == put_product_to_cart_expected_result.get('code')
    assert result.get('message') == put_product_to_cart_expected_result.get('message')


def test_get_catalog_funk():
    result = get_catalog()
    result_first_name = result[0]['name']

    assert result_first_name == expected_result_getter

