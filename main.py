from algorithms.Binary_search import *
from algorithms.Linear_search import *
from algorithms.Ternary_search import ternary


def main():
    init()


def init():
    print()
    print("Welcome to search arrays algorithms")
    print()
    print("1.) Linear search")
    print()
    print("2.) Binary search")
    print()
    print("3.) Terniary search")
    print()

    val = input("please type a number to proceed: ")
    value = int(val)

    if value == 1:
        entry_values = input("Please type the numbers of the array with spaces between each other: ")
        array = [int(number) for number in entry_values.split()]
        objective = int(input("Type the number that you want to search in the array: "))

        _linear = linear()

        _linear.search(array, objective)

        print(_linear.objective_index(objective))

        _linear.single_value()
        _linear.plot_graphs()

    if value == 2:
        entry_values = input("Please type the numbers of the array with spaces between each other: ")
        array = [int(number) for number in entry_values.split()]
        objective = int(input("Type the number that you want to search in the array: "))

        _binary = binary()

        _binary.binary_search(array, objective)

        print(_binary.objective_index(objective))


        _binary.plot_graphs()

    if value == 3:
        entry_values = input("Please type the numbers of the array with spaces between each other: ")
        array = [int(number) for number in entry_values.split()]
        objective = int(input("Type the number that you want to search in the array: "))

        _ternary = ternary()
        _ternary.ternary_search(array,objective)
        print(_ternary.objective_index(objective))

        _ternary.plot_graphs()

    else:

        print("Invalid entry, please try again")

if __name__ == "__main__":
    main()
