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
#ỨNG với 1 tên phương thức được gọi nhưng sẽ có kết quả thực hiện khác nhau.
#Tùy thuộc vào từng  loại đối tượng.
