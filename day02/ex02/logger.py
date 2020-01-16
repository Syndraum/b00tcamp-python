import time
import math
import logging
from random import randint


class CoffeeMachine():
    water_level = 100
    logging.basicConfig(
        filename='machine.log',
        level=logging.DEBUG,
        format="(roalvare)Running: %(message)s",
        filemode='w')
    begin = time.time()

    def log(func):
        def function_wrapper(self, *args, **kwargs):
            tmp = "\t\t[ exec-time = {:f} s ]".format(time.time() - self.begin)
            self.begin = time.time()
            logging.debug(func.__name__.replace("_", " ").capitalize()+tmp)
            return func(self, *args, **kwargs)
        return function_wrapper

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
