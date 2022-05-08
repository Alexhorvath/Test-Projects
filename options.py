class person:
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
class cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def playing(self):
            print(self.name, "is playing with the cardboard box")

#Person data
alex = person("Alex", 21, 1)
daniel = person("Daniel", 21, 2)
jozef = person("Jozef", 49, 3)
#Cat data
sage = cat("Sage", 6, "Black and White")
angel = cat("Angel", 6, "Brown")

sage.playing()
angel.playing()