class Bird():
    def flight(self):
        print("Bird fly")
    def intro(self):
        print("Bird Intro")
class Sparrow(Bird):
    def flight(self):
        print("Sparrow fly")
class Ostrich(Bird):
     def flight(self):
        print("Ostrich fly")
b = Bird()
s = Sparrow()
o = Ostrich()
b.flight()
b.intro()
s.flight()
s.intro()
o.flight()
o.intro()
