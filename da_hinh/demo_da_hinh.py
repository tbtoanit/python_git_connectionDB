class India():
    def capital(self):
        print("Capital India")
    def languages(self):
        print("Language India")

class USA():
    def capital(self):
        print("Capital USA")

    def languages(self):
        print("Languages USA")

obj_india = India()
obj_usa = USA()

for i in (obj_india,obj_usa):
    i.capital()
    i.languages()

