cookbook = {}


def stop():
    print("\nCookbook closed.")


def print_info():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def print_wrong():
    print("\nThis option does not exist, please \
type the corresponding number.")
    print("To exit, enter 5.")


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = (ingredients, meal, prep_time)


def add():
    print("\nPlease enter the recipe's name to get its details:")
    name = input(">> ")
    print("\nRecipe for", name + ':')
    ingredients = input("Ingredients list: ")
    meal = input("type of meal: ")
    prep_time = input("preparation time: ")
    add_recipe(name, ingredients, meal, prep_time)
    print("\nRecipe added !\n")


def delete_recipe(name):
    print("")
    if name in cookbook:
        cookbook.pop(name)
        print("Recipe", name, "deleted !")
    else:
        print("Recipe not in the cookbook")
    print("")


def print_recipe(name):
    print("")
    if name in cookbook:
        print(name, ":")
        print("    Ingredients list:\t", cookbook[name][0])
        print("    type of meal:\t\t", cookbook[name][1])
        print("    preparation time:\t", cookbook[name][2])
    else:
        print("Recipe not in the cookbook")
    print("")


def print_cookbook():
    print("\nAll the recipes !")
    for name, recipe in cookbook.items():
        print_recipe(name)
    print("")


def main():
    boucle = 1
    tab = ['1', '2', '3', '4', '5']
    while boucle:
        print_info()
        info = 1
        while info:
            choice = input(">> ")
            if choice in tab:
                if choice == '1':
                    add()
                elif choice == '2':
                    delete_recipe(input("\nRecipe name : "))
                elif choice == '3':
                    print_recipe(input("\nRecipe name : "))
                elif choice == '4':
                    print_cookbook()
                elif choice == '5':
                    stop()
                    boucle = 0
                info = 0
            else:
                print_wrong()


if __name__ == "__main__":
    main()
