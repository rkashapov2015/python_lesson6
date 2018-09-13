from ReaderFile import ReaderFile
from pprint import pprint

class Main:
    __cookbook = {}
    __filename = ''
    def __init__(self, filename):
        self.filename = filename
    def run(self):
        reader = ReaderFile(self.filename)
        self.__cookbook = reader.readCookBook()
        self.getShopListByDishes(['Запеченный картофель', 'Омлет'], 5)
    def getShopListByDishes(self, dishes, personCount):
        if len(self.__cookbook) == 0:
            return False
        shopList = {}
        for nameDish in self.__cookbook.keys():
            for ingredient in self.__cookbook[nameDish]:
                if ingredient['ingredient_name'] not in shopList:
                    shopList[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * personCount}
                else:
                    shopList[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * personCount
        pprint(shopList)


main = Main('sample_cookbook.txt')
main.run()