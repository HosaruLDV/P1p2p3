from hanlders.products import get_single_product

def test_get_single_product_out(data):
    data = {
    "action": 4,
    "data": {
      "id": 5
    }
}
    message = {'code': 404, 'message': 'Товара с таким номер не найдено'}
    assert get_single_product(data) == message

def test_get_single_product_in(data):
    data = {
        "action": 4,
        "data": {
            "id": 1
        }
    }
    message = {'code': 200, 'message': 'Яблоки. Голден\nЦена: 1000 рублей за кг\nОстаток на складе: 10 кг\nОписание: Зеленые яблоки, отлично подходят для приготовления пирога'}
    assert get_single_product(data) == message

