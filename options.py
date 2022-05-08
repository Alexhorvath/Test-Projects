class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def walking(self, miles = 0):
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


Alex = Person("Alex", 21, 1)

Daniel = Person("Daniel", 21, 2)

Jozef = Person("Jozef", 49, 3)

Alex.walking(2)