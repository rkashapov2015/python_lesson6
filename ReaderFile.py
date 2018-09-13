class ReaderFile:
    filename = ''
    cookbook = {}
    def __init__(self, filename):
        self.filename = filename
    def readCookBook(self):
        elementOfCookBook = []
        nameDish = ''
        countOfIngredients = 0
        order = 0
        with open(self.filename, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if len(line.strip()) == 0:
                    order = 0
                    if len(elementOfCookBook) > 0 and nameDish:
                        self.cookbook[nameDish] = elementOfCookBook
                        elementOfCookBook = []
                    continue
                if order == 0:
                    nameDish = line
                if order == 1:
                    countOfIngredients = int(line)
                    order +=1
                    continue
                if order == 2:
                    (nameIngredient, quantity, measure) = line.split(' | ')
                    elementOfCookBook.append({'ingredient_name': nameIngredient, 'quantity': int(quantity), 'measure': measure})
                    countOfIngredients -= 1
                if countOfIngredients == 0:
                    order +=1
        return self.cookbook
