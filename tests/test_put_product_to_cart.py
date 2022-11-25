from hanlders.cart import put_product_to_cart
from main import main

expected_result = {"code": 201,
    "message": f"Товар Яблоки. Голден. в количестве 5 кг добавлен в корзину "
               f"успешно"}


def test_put_product_to_cart_func():
    result = put_product_to_cart(
        {"action": 5, "filter": {"id": 1, "count": 5}})

    assert result.get('code') == expected_result.get('code')
    assert result.get('message') == expected_result.get('message')


def test_put_product_to_cart_main():
    result = main({"action": 5})

    assert result.get('code') == expected_result.get('code')
    assert result.get('message') == expected_result.get('message')
