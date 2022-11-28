from hanlders.categories import get_category_list

def test_categories():
    assert get_category_list(False) == {'code': 200, 'data': " 1.['Фрукты', 'Овощи']"}
