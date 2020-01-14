class Recipe:
    def __init__(
            self,
            name,
            cooking_lvl,
            cooking_time,
            ingredients,
            description,
            recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return "Recipe(\tname = " + self.name \
                + ",\n\tcooking_level = " + str(self.cooking_lvl) \
                + ",\n\tcooking_time = " + str(self.cooking_time) \
                + ",\n\tingredients = " + str(self.ingredients) \
                + ",\n\tdescription = " + self.description \
                + ",\n\trecipe_type = " + self.recipe_type + ")"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name not str")
        self._name = name

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if isinstance(cooking_lvl, str):
            if not cooking_lvl.isdigit():
                raise ValueError("Cooking level not int")
        elif not isinstance(cooking_lvl, int):
            raise ValueError("Cooking level not int")
        if int(cooking_lvl) < 1 or int(cooking_lvl) > 5:
            raise ValueError("Cooking level between 1 and 5")
        self._cooking_lvl = int(cooking_lvl)

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if isinstance(cooking_time, str):
            if not cooking_time.isdigit():
                raise ValueError("Cooking time not int")
        elif not isinstance(cooking_time, int):
            raise ValueError("Cooking time not int")
        if int(cooking_time) < 0:
            raise ValueError("Cooking time not negtive")
        self._cooking_time = cooking_time

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise ValueError("Ingredients not a list")
        self._ingredients = ingredients

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description not str")
        self._description = description

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        if not isinstance(recipe_type, str):
            raise ValueError("Recipe type not str")
        choice = ["starter", "lunch", "dessert"]
        if recipe_type not in choice:
            raise ValueError("Wromg recipe type :" + str(choice))
        self._recipe_type = recipe_type
