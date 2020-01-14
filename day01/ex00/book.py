import datetime


class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name not str")
        self._name = name

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        if not isinstance(last_update, datetime.datetime):
            raise ValueError("last_update not datetime")
        self._last_update = last_update

    @property
    def creattion_date(self):
        return self._creattion_date

    @creattion_date.setter
    def creattion_date(self, creattion_date):
        if not isinstance(creattion_date, datetime.datetime):
            raise ValueError("creattion_date not datetime")
        self._creattion_date = creattion_date

    @property
    def recipes_list(self):
        return self._recipes_list

    @recipes_list.setter
    def recipes_list(self, recipes_list):
        if not isinstance(recipes_list, dict):
            raise ValueError("recipes_list not dict")
        self._recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    return recipe
        print("No recipe found")

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type]
        print("No recipe type found")

    def add_recipe(self, recipe):
        self.recipes_list[recipe.recipe_type].append(recipe)
        # for recipe_type in self.recipes_list:
        #     if recipe_type.key() == recipe.recipe_type:
        #         recipe_type.valur().append(recipe)
