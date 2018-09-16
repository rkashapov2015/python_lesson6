from readerFile import ReaderFile
from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    reader = ReaderFile('sample_cookbook.txt')
    cookbook = reader.readCookBook()
    shop_list = {}

    if cookbook:
        for name_dish in cookbook:
            for ingredient in cookbook[name_dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'], 
                        'quantity': quantity * person_count
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += quantity * person_count

    return shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

pprint(shop_list)