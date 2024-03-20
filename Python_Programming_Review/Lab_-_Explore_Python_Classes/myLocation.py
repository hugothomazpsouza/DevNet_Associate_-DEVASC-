class Location:

    def __init__(self, name, country):
        self.name = name
        self.country = country


    def myLocation(self):
        print(f"Hi, My name is {self.name} and I live in {self.country}.")


loc = Location("Hugo Thomaz", "Brazil")

print(loc.name)
print(loc.country)
print(type(loc))


loc1 = Location("Tomaz", "Portugal")

loc1.myLocation()


