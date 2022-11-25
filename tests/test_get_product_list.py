import pytest
from handlers.hanlders.products import get_product_list


@pytest.mark.parametrize('a,b', [({"action": 2, "filter": {"price": ['>=100'], "category": None}},
                                  {'code': 200, 'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n'}),

                                 ({"action": 2, "filter": {"price": ['>=100', 77], "category": None}},
                                  {'code': 400, 'data': ''}),

                                 ([{"price": ['>=100']}, {"category": None}], {'code': 500, 'data': ''})
                                 ])
def test_get_product_list(a, b):
    assert get_product_list(a) == b
