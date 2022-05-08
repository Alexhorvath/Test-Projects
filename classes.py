from person_data import *


class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def walking(self, miles = 0):
        print(self.name)
        match miles:
            case 0:
                print("You haven't walked yet...")
            case n if miles == 1:
                print("Nice job walking 1 mile " + self.name + "...")
            case n if miles <=10000:
                print(f"Nice job walking {miles} miles " + self.name + "...")
            case n if miles >= 10001:
                print("Are you sure you haven't cheated?")
            case _:
                print("ERROR 404, TRY AGAIN")


    def running(self, miles = 0):
        print(miles)


def choose_player():
    print("Choose your player")
    print("1: Alex")
    print("2: Daniel")
    print("3: Jozef")

    player = input()

    match player:
        case "1":
            print("You've chosen", alex.name)
        case "2":
            print("You've chosen", daniel.name)
        case "3":
            print("You've chosen", jozef.name)
        case "4":
            print("There are only 3 players")
        case _:
            print("No selection has been made")

