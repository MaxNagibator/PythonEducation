print("huy")

class Person:
    def __init__(self, name, age:int):
        self.name = name
        self.age = age
        print("Создан человек с именем", self.name)

    def __del__(self):
        print("Удалён человек с именем", self.name)

    def get_info(self):
        print(self.name, self.age)

def person_info(person: Person):
    person.get_info()

illson = Person("illson", 20)
keaper = Person("keaper", 21)
person_info(illson)
person_info(keaper)
print(1)

def test():
    stherox = Person("stherox", 20)
    chelovek_godzilla = Person("zedroth", 20)

test()
print(2)
