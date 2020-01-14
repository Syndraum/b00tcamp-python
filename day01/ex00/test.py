from book import Book
from recipe import Recipe

my_book = Book("Cookbook")

try:
    cake = Recipe("Gateau", 2, 60, ["farine", "sucre", "oeuf"], "Un gateau fondant", "dessert")
    salad = Recipe("Salade", 1, 5, ["tomate", "laitue", "mais", "thon"], "Une slade légère", "starter")
    steak_frite = Recipe("Steak frite", 3, 15, ["steak", "patate", "gras"], "C'est lourd", "lunch")
except ValueError as e:
    print("ValueError :", e)
else:
    my_book.add_recipe(cake)
    my_book.add_recipe(salad)
    my_book.add_recipe(steak_frite)
    print(my_book.get_recipe_by_name("Gateau"))
    for recipe in my_book.get_recipes_by_types("lunch"):
        print(recipe)
