# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import self as self

from src.main.gardener import Gardener
from src.main.tomato import Tomato
from src.main.tomatobush import TomatoBush


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(2)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
