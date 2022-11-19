class Student:
    amount = 0
    print("Є. Я тут")
    def __init__(self, name = None):
        self.name = name
        Student.amount += 1
    def __str__(self):
        return f'мій логін {self.name}'

class Teacher(Student):
    print('А ну роби домашку!')

dima = Student()
andry = Student()
albina = Teacher()
dima = Student(name='DIMAGLOBUS')
print(dima)

class Cat:
    amount = 0
    print("Hello there!")
    def __init__(self, name=None, owner = dima, food = None, words = None):
        self.name = name
        self.owner = owner
        self.food = food
        self.words = words
        Cat.amount += 1
    def __str__(self):
        return f'i`m telling you {self.words}'
murka = Cat()
murka = Cat(words='Mwa')
print(murka)