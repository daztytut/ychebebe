#1 задание:
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year #атрибут передаём значение в экземпляр
    def __str__(self):
         return self.title
    def get_info(self):
        print(f"Название книги: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}")
    def get_title(self):
        print(f"Название книги: {self.title}") #получаем все данные экземпляра сверху, тут ток название

book = Book(str(input("Введите название книги:\n")), str(input("Введите автора книги:\n")), str(input("Введите год издания:\n")))
book.get_info()
book.get_title()
print(book)
#2 задание:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius #получаем значение класса

    def set_radius(self, new_radius):
        self.radius = new_radius #изм зн радиуса

    def get_perimetr(self):
        return 2*3.14*float(self.radius)
    def get_ploshad(self):
        return 3.14*float(self.radius)**2
circle = Circle(input("Введите радиус круга:\n"))
print(f"Текцщий радиус круга: {circle.get_radius()}")

circle.set_radius(input("Введите новое значение радиуса:\n"))
print(f"Обновлённое значение радиуса: {circle.get_radius()}")
print(circle.get_perimetr())

