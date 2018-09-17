class ReaderFile:
    STATE_READ_NAME_DISH = 0
    STATE_READ_NUMBER_INGREDIENTS = 1
    STATE_READ_INGREDIENT = 2

    def __init__(self, filename):
        self.filename = filename
        self.cookbook = {}

    def readCookBook(self):
        element_of_cookbook = []
        name_dish = ''
        number_of_ingredients = 0
        current_state = self.STATE_READ_NAME_DISH
        with open(self.filename, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    current_state = self.STATE_READ_NAME_DISH
                    if len(element_of_cookbook) > 0 and name_dish:
                        self.cookbook[name_dish] = element_of_cookbook
                        element_of_cookbook = []
                    continue

                if current_state == self.STATE_READ_NAME_DISH:
                    name_dish = line
                    current_state = self.STATE_READ_NUMBER_INGREDIENTS
                    continue

                if current_state == self.STATE_READ_NUMBER_INGREDIENTS:
                    number_of_ingredients = int(line)
                    current_state = self.STATE_READ_INGREDIENT
                    continue

                if current_state == self.STATE_READ_INGREDIENT:
                    (name_ingredient, quantity, measure) = line.split(' | ')
                    element_of_cookbook.append({
                        'ingredient_name': name_ingredient, 
                        'quantity': int(quantity), 
                        'measure': measure
                    })
                    number_of_ingredients -= 1

                if number_of_ingredients == 0:
                    current_state = self.STATE_READ_NAME_DISH

        return self.cookbook
